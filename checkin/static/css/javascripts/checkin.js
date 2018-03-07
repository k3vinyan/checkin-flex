$( document ).ready(function(){

  let time = $('.timepicker').pickatime({
    default: 'now', // Set default time: 'now', '1:30AM', '16:30'
    fromnow: 0,       // set default time to * milliseconds from now (using with default = 'now')
    twelvehour: true, // Use AM/PM or 24-hour format
    donetext: 'OK', // text for done-button
    cleartext: 'Clear', // text for clear-button
    canceltext: 'Cancel', // Text for cancel-button
    autoclose: false, // automatic close timepicker
    ampmclickable: true, // make AM PM clickable
    aftershow: function(something){
      console.log("the aftershow function")
    } //Function for after opening timepicker
  });


  $("form.form-checkin input[type='checkbox']").change(
    function(){
      let driverId = $(this)[0].id.split("-")[1]
      let formData = $(this).parent().serialize();
      console.log("monkey dog")
      if (this.checked) {
        $.ajax({
          type: "POST",
          url: "checkin",
          data: formData,
          success: function(response){
            console.log("successfful")
            $("#tr-id-" + driverId).removeClass("unchecked").addClass("checked grey-text");
            let checkinLabel = $("label[for=checkin-"  + driverId + "]")[0];
            let nowShowLabel = $("label[for=noShow-"  + driverId + "]")[0];
            let input = $('#noShow-' + driverId);

            $(checkinLabel).removeClass("black-text");
            $(nowShowLabel).removeClass("black-text");
            input.attr("disabled", "disabled")
          },
          error: function(error){
            console.log(error)
          }
        })
      }
  });



  $('form.form-checkin input[type=checkbox]').change(
    function(){
        let driverId = $(this)[0].id.split("-")[1]
      let formData = $(this).parent().serialize();
      if (!this.checked) {
        $.ajax({
          type: "POST",
          url: "checkin",
          data: formData,
          success: function(response){
              $('#tr-id-'+ driverId).removeClass("checked grey-text").addClass("unchecked");
              let checkinLabel = $("label[for=checkin-"  + driverId + "]")[0];
              let nowShowLabel = $("label[for=noShow-"  + driverId + "]")[0];
              let input = $('#noShow-' + driverId);

              $(checkinLabel).addClass("black-text");
              $(nowShowLabel).addClass("black-text");
              input.attr("disabled", "disabled");
              input = $('#noShow-' + driverId);
              input.removeAttr("disabled");
          },
          error: function(error){
            console.log(error)
          }
        })
      }
  });

  $("form.form-noShow input[type='checkbox']").change(
    function(){
      let driverId = $(this)[0].id.split("-")[1]
      let formData = $(this).parent().serialize();

      if (this.checked) {
        $.ajax({
          type: "POST",
          url: "noShow",
          data: formData,
          success: function(response){
            $("form-noShow-" + driverId).removeClass("unchecked").addClass("checked grey-text2");
            let checkinLabel = $("label[for=checkin-"  + driverId + "]")[0];
            let nowShowLabel = $("label[for=noShow-"  + driverId + "]")[0];
            let input = $('#checkin-' + driverId);

            $(checkinLabel).removeClass("black-text");
            $(nowShowLabel).removeClass("black-text");
            input.attr("disabled", "disabled")
          },
          error: function(error){
            console.log(error)
          }
        })
      }
  });



  $('form.form-noShow input[type=checkbox]').change(
    function(){
        let driverId = $(this)[0].id.split("-")[1]
      let formData = $(this).parent().serialize();
      if (!this.checked) {
        $.ajax({
          type: "POST",
          url: "noShow",
          data: formData,
          success: function(response){
              $('#form-nowShow-'+ driverId).removeClass("checked grey-text2").addClass("unchecked");
              let checkinLabel = $("label[for=checkin-"  + driverId + "]")[0];
              let nowShowLabel = $("label[for=noShow-"  + driverId + "]")[0];
              let input = $('#checkin-' + driverId);

              $(checkinLabel).addClass("black-text");
              $(nowShowLabel).addClass("black-text");
              input.attr("disabled", "disabled");
              input = $('#checkin-' + driverId);
              input.removeAttr("disabled");
          },
          error: function(error){
            console.log(error)
          }
        })
      }
  });


})
