$(document).ready(function() {
   $('select').material_select();

   //disabled assigned routes at start
   let dropdowns = $("input.select-dropdown");

   for(let i = 0; i < dropdowns.length; i++){
     if(dropdowns[i].value != "Choose your option"){
       let dpValue = dropdowns[i].value;
       let driverId = $(dropdowns[i]).siblings()[2].name;
       $("input[value=\'" + dpValue + "\']").prop("disabled", true);
       $("input[value=\'" + dpValue + "\']").attr('driver-id', driverId);
     }
   }

   $("select").change(function(element){

     let route = element.target.value;
     let driverId = $(this).attr('name');
     let token =  $("input[type='hidden']")[0].value
     console.log(route)
     let object = {'route': route, 'driverId': driverId, 'csrfmiddlewaretoken': token}

     $.ajax({
       type: "POST",
       url: "",
       data: object,
       success: function(response){
         $('body').html(response)
       },
       error: function(error){
         console.log(error)
       }
     })

 })

 $('a.changeRouteBtn').on("click", function(element){
   let driverId = element.target.dataset.id
   $("input[driver-id=\'" + driverId + "\']").prop("disabled", false);
 })
 let selectedChange = document.getElementById("routeSelector");

 selectedChange.addEventListener("change", function(){

  }, false);
});
