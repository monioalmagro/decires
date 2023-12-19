_notify = new deciresAlert();

const retrieveProfessionalPublicQuery = `query retrieveProfessionalPublicQuery($input: QueryRetrieveUserInput!) {
  psychology {
    getProfessional(input: $input) {
      originalId
      firstName
      lastName
      avatar
      userCarreerSet {
        originalId
        carreer {
          name
          description
        }
        specializations {
          originalId
          name
          description
          __typename
        }
        serviceMethodEnum
        serviceModalityEnum
        experienceSummary
        __typename
      }
      languagesSet {
        languageName
        languageEnum
        levelEnum
        __typename
      }
      officeLocations {
        name
        city {
          name
          __typename
        }
        __typename
      }
      isVerifiedProfile
      __typename
    }
  }
}`;

function htmlComponentDisplay($data) {
  this.data = $data;

  this.splitParagraph = (paragraph) => {
    let $paragraph = paragraph.split(/\. (?=[A-Z])/);

    var outParagraph = "";

    for (var i = 0; i < $paragraph.length; i++) {
      outParagraph += `<p class="about-me-desc" style="text-align: justify;">${$paragraph[i]}</p>`;
    }
    return outParagraph;
  };
  this.renderProfile = () => {
    obj = this.data;
    userCarreer = obj.userCarreerSet[0];

    expParagraph = this.splitParagraph(userCarreer.experienceSummary);

    return `<div class="post-image" style="text-align: center;">
                <img style="max-width: 200px; height: auto;" src="${obj.avatar}" class="img-fluid">
            </div>
            </br>
            <h2 class="content-title">${obj.firstName} ${obj.lastName} (${userCarreer.carreer.name})</h2>
            <hr>
            <h4 class="content-title">Tipo de atención: <small>${userCarreer.serviceMethodEnum}</small></h4>
            <h4 class="content-title">Modalidad de atención: <small>${userCarreer.serviceModalityEnum}</small></h4>
            <br>
            <h3 class="content-title">Sobre Mi</h3>
            <br>
            <div class="parrafos">
                ${expParagraph}
            </div>
            <br>`;
  };
  this.renderLanguages = () => {
    $data = this.data.languagesSet;

    $languages = "";
    for ($i = 0; $i < $data.length; $i++) {
      $languages += `<li><a href="javascript:void(0)">${$data[$i].languageName} (${$data[$i].levelEnum}).</a></li>`;
    }
    return $languages;
  };
  this.renderSpecializations = () => {
    $data = this.data.userCarreerSet[0].specializations;

    $specializations = "";
    for ($i = 0; $i < $data.length; $i++) {
      $specializations += `<li><a href="javascript:void(0)">${$data[$i].name}.</a></li>`;
    }
    return $specializations;
  };
  this.renderOfficeLocations = () => {
    $data = this.data.officeLocations;

    $locations = "";
    for ($i = 0; $i < $data.length; $i++) {
      $locations += `<li><a href="javascript:void(0)">${$data[$i].name}, ${$data[$i].city.name}.</a></li>`;
    }
    return $locations;
  };
}

initialRequest = () => {
  $.ajax({
    url: Django.graphql_url,
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      query: retrieveProfessionalPublicQuery,
      variables: {
        input: {
          originalId: originalId,
        },
      },
    }),
    success: function (response) {
      $data = [];

      if (response.data && response.data.psychology && response.data.psychology.getProfessional) {
        $data = response.data.psychology.getProfessional;

        html = new htmlComponentDisplay($data);
        $profile = html.renderProfile();
        $languages = html.renderLanguages();
        $specializations = html.renderSpecializations();
        $office_locations = html.renderOfficeLocations();

        $("#profile").empty().append($profile);
        $("#languages").empty().append($languages);
        $("#specializations").empty().append($specializations);
        $("#office_locations").empty().append($office_locations);
      } else {
        setTimeout(function () {
          location.href = Django.urls.home;
        }, 40);
      }
    },
    error: function (xhr, status, error) {
      console.error("Error en la solicitud AJAX:", status, error);
      setTimeout(function () {
        location.href = Django.urls.home;
      }, 40);
    },
  });
};

initialRequest();
