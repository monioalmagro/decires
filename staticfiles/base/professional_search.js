$request_values = DecireslocalStorage.get("request_values");

const filter_type_especializations = 1;
const filter_type_language = 2;
/**
 * GraphQL query to retrieve the list of public professionals.
 */
const listProfessionalPublicQuery = `
query listProfessionalPublicQuery ($input: QueryListUserInput!) {
  psychology {
    getProfessionalList (input: $input){
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
        truncateExperienceSummary
        __typename
      }
      languagesSet {
        languageName
        languageEnum
        levelEnum
        __typename
      }
      isVerifiedProfile
      __typename
    }
  }
}
`;

/**
 * Generates HTML for an item row.
 */
getItemRow = (items) => {
  return `<div class="item-row">${items}</div>`;
};
/**
 * Generates HTML for an item.
 */
getItem = (obj) => {
  const specializations = obj.userCarreerSet
    .flatMap((item) => item.specializations.map((spec) => spec.name))
    .join(", ");

  let specialization_word =
    obj.userCarreerSet[0].specializations.length > 1 ? "Especialidades:" : "Especialidad:";

  return `<div class="item item-thumbnail">
            <a href="javascript:void(0)" class="item-image">
              <img src="${obj.avatar}" alt="${obj.firstName} ${obj.lastName}" />
            </a>
            <div class="item-info">
              <h4 class="item-title">
                <a href="javascript:void(0)">${obj.firstName} ${obj.lastName} (${obj.userCarreerSet[0].carreer.name})</a>
              </h4>
              <p class="item-desc">${specialization_word}</p>
              <div class="item-price">${specializations}</div>

            </div>
          </div>`;
};
/**
 * Generates HTML for sidebar items.
 */
getSideBarItems = (item, quantity, type) => {
  return `<li><a href="#" onclick="professional_filter_select('${item}', ${type});">${item} <span class="pull-right">(${quantity})</span></a></li>`;
};
/**
 * Filters results based on selected criteria.
 */
professional_filter_select = (item) => {
  // Verificar si el elemento ya está presente en el array
  const isDuplicate = professionalSearchController.filter_list.includes(item);

  // Agregar el elemento solo si no es un duplicado
  if (!isDuplicate) {
    professionalSearchController.filter_list.push(item);
  }

  return false;
};

professional_filter_results = () => {
  if (professionalSearchController.filter_list.length > 0) {
    professionalSearchController.getFilteredResults();
    professionalSearchController.updatePagination();
    professionalSearchController.filter_list = [];
  }
  return false;
};

/**
 * Restores filters to the initial state.
 */
restore_filters = () => {
  professionalSearchController.filter_list = [];
  professionalSearchController.getInitialSearchResults();
  return false;
};

/**
 * Controller class for managing professional search functionality.
 */
let professionalSearchController = {
  data: null,
  total_count: null,
  filtered_total_count: null,
  filter_list: [],
  currentPage: 1,
  itemsPerPage: 12,

  /**
   * Initializes the controller with data.
   */
  init: function ($data) {
    this.data = $data;
  },
  /**
   * Gets the total count of items and updates the UI.
   */
  getTotalCount: function () {
    this.total_count = this.data.length;
    this.filtered_total_count = this.data.length;
    $("#total_count").text(this.filtered_total_count + " de " + this.total_count);
    return false;
  },
  /**
   * Generates sidebar items for specializations and updates the UI.
   */
  getSideBarSpecializations: function (key, html_id) {
    const itemCountMap = {};
    const itemSet = new Set();

    this.data.forEach((items) => {
      items.userCarreerSet[0][key].forEach((items2) => {
        const itemName = items2.name;

        itemSet.add(itemName);

        itemCountMap[itemName] = (itemCountMap[itemName] || 0) + 1;
      });
    });

    $side_bar_html = "";

    for (const especializacion of itemSet) {
      $side_bar_html += getSideBarItems(
        especializacion,
        itemCountMap[especializacion],
        filter_type_especializations
      );
    }
    $(html_id).empty().append($side_bar_html);
    return false;
  },
  /**
   * Generates sidebar items for languages and updates the UI.
   */
  getSideBarLanguages: function (html_id) {
    const itemCountMap = {};
    const itemSet = new Set();

    this.data.forEach((items) => {
      items.languagesSet.forEach((items2) => {
        const itemName = items2.languageName;

        itemSet.add(itemName);

        itemCountMap[itemName] = (itemCountMap[itemName] || 0) + 1;
      });
    });

    $side_bar_html = "";

    for (const especializacion of itemSet) {
      $side_bar_html += getSideBarItems(
        especializacion,
        itemCountMap[especializacion],
        filter_type_language
      );
    }
    $(html_id).empty().append($side_bar_html);
    return false;
  },
  /**
   * Filters results based on the selected item and type.
   */
  getFilteredResults: function () {
    $data = this.filterData(this.data, this.filter_list);
    this.filtered_total_count = $data.length;
    $("#total_count").text(this.filtered_total_count + " de " + this.total_count);
    this.prepareResults($data);
    return false;
  },
  /**
   * Retrieves the initial search results.
   */
  getInitialSearchResults: function () {
    this.getTotalCount();
    this.prepareResults(this.data);
    return false;
  },
  /**
   * Prepare results.
   */
  prepareResults: function ($data) {
    $item_rows = ``;
    $html_items = [];

    for ($i = 0; $i < $data.length; $i++) {
      $html_items.push(getItem($data[$i]));
    }
    for ($j = 0; $j < $html_items.length; $j += 3) {
      $item_rows += getItemRow($html_items.slice($j, $j + 3));
    }
    $("#professional_list").empty().append($item_rows);
    return false;
  },

  filterData: function ($data, filterList) {
    return $data.filter((professional) => {
      return filterList.some((filter) => {
        const specializationMatch = professional.userCarreerSet[0].specializations.some(
          (s) => s.name === filter
        );
        const languageMatch = professional.languagesSet.some((l) => l.languageName === filter);
        return specializationMatch || languageMatch;
      });
    });
  },
  /**
   * Actualiza la paginación.
   */
  updatePagination: function () {
    const totalPages = Math.ceil(this.filtered_total_count / this.itemsPerPage);
    const paginationElement = $("#pagination");
    paginationElement.empty();

    // Crea el botón "Previo"
    paginationElement.append(
      `<li class="page-item ${
        this.currentPage === 1 ? "disabled" : ""
      }"><a href="javascript:;" class="page-link" onclick="professionalSearchController.changePage(${
        this.currentPage - 1
      })">Previo</a></li>`
    );

    // Crea los botones para cada página
    for (let i = 1; i <= totalPages; i++) {
      paginationElement.append(
        `<li class="page-item ${
          this.currentPage === i ? "active" : ""
        }"><a class="page-link" href="javascript:;" onclick="professionalSearchController.changePage(${i})">${i}</a></li>`
      );
    }

    // Crea el botón "Siguiente"
    paginationElement.append(
      `<li class="page-item ${
        this.currentPage === totalPages ? "disabled" : ""
      }"><a href="javascript:;" class="page-link" onclick="professionalSearchController.changePage(${
        this.currentPage + 1
      })">Siguiente</a></li>`
    );
  },

  /**
   * Cambia a la página especificada y actualiza la paginación.
   */
  changePage: function (page) {
    this.currentPage = page;
    this.prepareResults(this.data.slice((page - 1) * this.itemsPerPage, page * this.itemsPerPage));
    this.updatePagination();
  },
};

initialRequest = () => {
  $.ajax({
    url: Django.graphql_url,
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      query: listProfessionalPublicQuery,
      variables: $request_values,
    }),
    success: function (response) {
      $data = [];

      if (
        response.data &&
        response.data.psychology &&
        response.data.psychology.getProfessionalList
      ) {
        $data = response.data.psychology.getProfessionalList;

        Promise.resolve(
          professionalSearchController.init($data),
          professionalSearchController.getSideBarSpecializations(
            "specializations",
            "#specialization_list"
          ),
          professionalSearchController.getSideBarLanguages("#language_list")
        ).then(function () {
          professionalSearchController.getInitialSearchResults();
          professionalSearchController.updatePagination();
        });
      } else {
        setTimeout(function () {
          location.href = "/";
        }, 40);
      }
    },
    error: function (xhr, status, error) {
      console.error("Error en la solicitud AJAX:", status, error);
      setTimeout(function () {
        location.href = "/";
      }, 40);
    },
  });
};

initialRequest();
