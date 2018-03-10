$( document ).ready(function(){

  $('form#form-checkout input[type=checkbox]').change(
    function(){
        console.log('checkout')
      let driverId = this.id
      let formData = $(this).parent().serialize();
      if (this.checked) {
        $.ajax({
          type: "POST",
          url: "",
          data: formData,
          success: function(response){
            $('#tr-id-'+ driverId).removeClass("unchecked").addClass("checked grey-text");
          },
          error: function(error){
            console.log(error)
          }
        })
      }
  });

  $('form#form-checkout input[type=checkbox]').change(
    function(){
      console.log("checkout")
      let driverId = this.id
      let formData = $(this).parent().serialize();
      if (!this.checked) {
        $.ajax({
          type: "POST",
          url: "",
          data: formData,
          success: function(response){
              $('#tr-id-'+ driverId).removeClass("checked grey-text").addClass("unchecked");
          },
          error: function(error){
            console.log(error)
          }
        })
      }
  });


})
