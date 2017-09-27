$(document).ready(function () {

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
               console.log(data.total_price);
                $('.total_price').text(data.total_price + " $");
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



});