// constants

const carrersQuery = `
  query select2Queries {
    select2 {
      carreers {
        id
        text
        __typename
      }
    }
  }
`;

// generics

$("#ciudad").hide();
$("#zona").hide();

$("#select_modalidad").on("change", function () {
  $value = $(this).val();
  if ($value == Django.select2_all) {
    $("#ciudad, #zona").hide();
  } else {
    $("#ciudad").show();
  }
});

$("#select_ciudad").on("change", function () {
  $value = $(this).val();
  if ($value == Django.select2_all) {
    $("#zona").hide();
  } else {
    $("#zona").show();
  }
});

// functions

loadModal = () => {
  $.when(loadSelect2(carrersQuery, "#profesionales", "Profesionales")).then(
    $("#modal_search_proffessionals").modal("show")
  );
};

searchProffessional = () => {
  $profesionales = $("#profesionales").val();
  $modalidad = $("#select_modalidad").val();

  if ($profesionales == Django.select2_all || $modalidad == Django.select2_all) {
    alert("No puedes lanzar la perticion");
  } else {
    alert("PETICION AJAX CON REDIRECT ");
    $("#modal_search_proffessionals").modal("hide");
  }

  return 0;
};

a = {
  "caba": [
    "Abasto",
    "Agronomía",
    "Almagro",
    "Balvanera (Once)",
    "Barracas",
    "Belgrano",
    "Boedo",
    "Caballito",
    "Chacarita",
    "Coghlan",
    "Colegiales",
    "Congreso - Tribunales",
    "Constitución",
    "Flores",
    "Floresta",
    "La Boca",
    "La Paternal",
    "Liniers",
    "Mataderos",
    "Monserrat",
    "Monte Castro",
    "Nueva Pompeya",
    "Núñez",
    "Palermo",
    "Parque Avellaneda",
    "Parque Chacabuco",
    "Parque Chas",
    "Parque Patricios",
    "Puerto Madero",
    "Recoleta - Barrio Norte",
    "Retiro",
    "Saavedra",
    "San Cristobal",
    "San Nicolas",
    "San Telmo",
    "Vélez Sarsfield",
    "Versalles",
    "Villa Crespo",
    "Villa del Parque",
    "Villa Devoto",
    "Villa General Mitre",
    "Villa Lugano",
    "Villa Luro",
    "Villa Ortúzar",
    "Villa Pueyrredón",
    "Villa Real",
    "Villa Riachuelo",
    "Villa Santa Rita",
    "Villa Soldati",
    "Villa Urquiza",
  ],
};
