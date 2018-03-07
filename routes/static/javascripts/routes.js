$(document).ready(function(){
    // the "href" attribute of the modal trigger must specify the modal ID that wants to be triggered
    $('.delete').modal();
    $('.addRouteModal').modal();
    $('.copyTBAS').modal();

    $("button[type='submit']").on("click", function(){
      $('#loader').removeClass('hide');
       $(".overlay").show();
      })
  });
