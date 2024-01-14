_notify = new deciresAlert();

const retrieveProfessionalPublicQuery = `
query professionalRetrievePublicQuery($input: QueryRetrieveUserInput!) {
  psychology {
    getProfessional(input: $input) {
      originalId
      firstName
      lastName
      email
      avatar {
        originalId
        url
        __typename
      }
      genderEnum
      facebookProfile
      instagramProfile
      linkedinProfile
      userCarreerSet {
        originalId
        name
        description
        serviceMethodEnum
        serviceModalityEnum
        truncateExperienceSummary
        __typename
      }
      userSpecializationSet {
        originalId
        name
        description
        __typename
      }
      languagesSet {
        name
        slug
        __typename
      }
      userOfficeSet {
        name
        city {
          name
          __typename
        }
        __typename
      }
      attachmentSet {
        originalId
        url
        description
      }
      isVerifiedProfile
      profileUrl
      __typename
    }
  }
}
`;

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
      $languages += `<li style="list-style: none;"><a href="javascript:void(0)" style="text-decoration: none; color: black;">${$data[$i].languageName} (${$data[$i].levelEnum}).</a></li>`;
    }
    return $languages;
  };
  this.renderSpecializations = () => {
    $data = this.data.userCarreerSet[0].specializations;

    $specializations = "";
    for ($i = 0; $i < $data.length; $i++) {
      $specializations += `<li style="list-style: none;"><a href="javascript:void(0)" style="text-decoration: none; color: black;">${$data[$i].name}.</a></li>`;
    }
    return $specializations;
  };
  this.renderOfficeLocations = () => {
    $data = this.data.officeLocations;

    $locations = "";
    for ($i = 0; $i < $data.length; $i++) {
      $locations += `<li style="list-style: none;"><a href="javascript:void(0)" style="text-decoration: none; color: black;">${$data[$i].name}, ${$data[$i].city.name}.</a></li>`;
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

loadModal = () => {
  $("#masked-input-phone").mask("+54 (999) 999.99.99");

  $("#modal_send_message").modal("show");
  return false;
};

sendMessage = () => {
  alert("qwerty");
  return false;
};
