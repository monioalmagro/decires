// constants
let object_data = {};
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

const citiesQuery = `query select2Queries {
  select2 {
    cities {
      id
      text
      __typename
    }
  }
}`;

get_zones_query = (cityId) => {
  return `query select2Queries {
    select2 {
      zones (cityId: ${cityId}){
        id
        text
        __typename
      }
    }
  }`;
};
// generics

$("#ciudad").hide();
$("#zona").hide();

$("#select_modalidad").on("change", function () {
  $value = $(this).val();
  if ($value == Django.select2_all) {
    $("#ciudad, #zona").hide();
  } else {
    loadSelect2(citiesQuery, "#select_ciudad", "Ciudad", "cities");
    $("#ciudad").show();
  }
});

$("#select_ciudad").on("change", function () {
  $value = $(this).val();
  if ($value == Django.select2_all) {
    $("#zona").hide();
  } else {
    loadSelect2(get_zones_query($value), "#select_zona", "Zonas", "zones");
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
