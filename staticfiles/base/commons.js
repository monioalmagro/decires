loadSelect2 = (graphqlQuery, jquery_id, option_label_tag, select2_tag = "carreers") => {
  // Configurar la petición Ajax
  $.ajax({
    url: Django.graphql_url,
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify({ query: graphqlQuery }),
    success: function (response) {
      console.log(response);
      if (select2_tag == "carreers") {
        $data = response.data.select2.carreers;
      } else if (select2_tag == "cities") {
        $data = response.data.select2.cities;
      } else if (select2_tag == "zones") {
        $data = response.data.select2.zones;
      }

      $options = `<option value="" selected>${option_label_tag}</option>`;
      for ($i = 0; $i < $data.length; $i++) {
        $options += `<option value="${$data[$i].id}">${$data[$i].text}</option>`;
      }
      $(jquery_id).empty().append($options);
    },
    error: function (error) {
      // Manejar errores
      console.error(error);
    },
  });
  return 0;
};

uploadImage = () => {
  var input = $("#avatar")[0];
  var file = input.files[0];

  if (file) {
    var reader = new FileReader();

    reader.onload = function (e) {
      var imageContainer = $("#image-container");
      imageContainer.html(
        '<img src="' +
          e.target.result +
          '" alt="Avatar" style="max-width: 200px; max-height: 200px;"/>'
      );
    };

    reader.readAsDataURL(file);
  }
};
