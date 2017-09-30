$(document).ready(function () {

    // $("#autocomplete").autocomplete({
    //   source: function(request, response){
    //     var url = $('#search-form').attr('action');
    //     console.log(url);
    //     $.ajax({
    //       url: url,
    //       dataType: "jsonp",
    //       data:{
    //         1: 'send send'
    //       },
    //       success: function(data){
    //         response($.map(data.geonames, function(item){
    //           return{
    //             label: item.name + (item.adminName1 ? ", " + item.adminName1 : "") + ", " + item.countryName,
    //             value: item.name
    //           }
    //         }));
    //       }
    //     });
    //   },
    //   minLength: 2
    // });


   $('.item_add').click(function(e) {
       e.preventDefault();
       var productId = e.target.dataset.id;
       var csrfToken = $('#form-cart [name="csrfmiddlewaretoken"]').val();

       var data = {
           product_id: productId,
           csrfmiddlewaretoken: csrfToken
       };
       var url = $('#form-cart').attr('action');

       $.ajax({
           url: url,
           type: 'POST',
           data: data,
           cache: true,
           success: function (data) {
               console.log('OK');
               console.log(data.order_price);
                $('.total_price').text(data.order_price + " $");
           },
           error: function (error) {
               console.log('error');
           }
       })
   });

  $('.cart__clear').click(function(e) {
       e.preventDefault();
       var csrfToken = $('#form-clear-cart [name="csrfmiddlewaretoken"]').val();

       var data = {
           csrfmiddlewaretoken: csrfToken
       };
       var url = $('#form-clear-cart').attr('action');

       $.ajax({
           url: url,
           type: 'POST',
           data: data,
           cache: true,
           success: function (data) {
               console.log(data);
                $('.total_price').text('0 $');
           },
           error: function (error) {
               console.log('error');
           }
       })
   });

  $('.product__amount').click(function(e) {
       e.preventDefault();

       $(this).change(function () {
           var amount = $(this).val();
           var productPrice =  $(this).closest('.check').siblings('.order-item__price').text().slice(1);
           var total_price = parseFloat(productPrice) * Number(amount);
           var subTotal = $(this).closest('.check').siblings('.order-item__subtotal').text('$ ' + total_price.toFixed(2));

           var csrfToken = $('#form-cart [name="csrfmiddlewaretoken"]').val();
           var productId = e.target.dataset.id;

           var data = {
               product_id: productId,
               amount: amount,
               csrfmiddlewaretoken: csrfToken
           };
           var url = $('#form-order').attr('action');
           console.log(data, url);
           $.ajax({
               url: url,
               type: 'POST',
               data: data,
               cache: true,
               success: function (data) {
                    $('.total_price').text(data.order_price + " $");
                    console.log(data);
               },
               error: function (error) {
                   console.log('error');
               }
           });
           $(this).off('change');
       });
   });
});