$(document).ready(function () {
  $(".default-select2").select2({
    width: "100%",
    placeholder: "Seleccione una opción",
  });
  // $(".multiple-select2").select2({
  //   width: "100%",
  //   placeholder: "Seleccione sus opciones",
  //   multiple: true,
  // });

  $(".multiple-select2").select2({
    width: "resolve",
    allowClear: true,
    placeholder: "Seleccione sus opciones",
    multiple: true,
  });
});
