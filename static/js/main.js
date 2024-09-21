$(document).ready(function () {
  $.ajax({
    type: "GET",
    url: "/products/",
    success: function (data) {
      renderProducts(data);
    },
    error: function (error) {
      console.log("Error fetching products:", error);
    }
  });
});


$('#filer').click(function (event) {
  event.preventDefault();

  var selectedValues = {
    "category": [],
    "brand": [],
    "seller": [],
    "warranty": [],
    "productType": [],
    "price": []
  };

  $('input[name="options"]:checked').each(function () {
    var category = $(this).attr('id');
    selectedValues[category].push(parseInt($(this).val()));
  });

  selectedValues["price"].push(parseInt($("#price").val()))
  console.log(selectedValues)

  $.ajax({
    type: "POST",
    url: "/products/filter/",
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    data: JSON.stringify(selectedValues),
    success: function (data) {
      renderProducts(data);
    },
    error: function (error) {
      console.log(error);
    }
  });
})


$('#search_field').click(function () {

  $('input[name="options"]:checked').prop('checked', false);
  $('#price').val('0');

  $('.row').html('');
  let data_search = {}
  data_search["searchValue"] = $('#searchValue').val()
  let url = "/products/search/"
  console.log(data_search)
  $.ajax({
    type: "POST",
    url: url,
    data: JSON.stringify(data_search),
    success: function (data) {
      renderProducts(data);
    },
    error: function (errormsg) {
      console.log(errormsg)
    }
  });
})


function renderProducts(products) {
  $('.row').html('');

  for (let i = 0; i < products.length; i++) {
    $('.row').append(`
        <div class="col-lg-4">
          <img class="thumbnail" src="${products[i].image}" style='width:300px; height:300px;' />
          <div class="box-element product">
            <h6><strong>${products[i].name}</strong></h6>
            <hr />
            <button data-product="" data-action="add" class="btn btn-outline-secondary add-btn update-cart">Add to Cart</button>
            <h4 style="display: inline-block; float: right"><strong>${products[i].price}</strong></h4>
          </div>
        </div>
      `);
  }
}


$('#resetFilters').click(function (event) {
  event.preventDefault();

  $('input[name="options"]:checked').prop('checked', false);
  $('#price').val('0');
  $('#filer').trigger('click');
});
