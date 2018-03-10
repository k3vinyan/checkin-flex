$(document).ready(function(){

    let transporterId, DAName, availability, duration, startTime, endTime, isSameDayRequest;

    //Not Arrived, Finished, DRIVING, Active

    function Driver(transporterId, DAName, availability, duration, startTime , endTime, isSameDayRequest){
      this.transporterId = transporterId;
      this.DAName = DAName;
      this.availability = availability;
      this.duration = duration;
      this.startTime = startTime;
      this.endTime = endTime;
      this.isSameDayRequest = isSameDayRequest;
    };

    let isAvailable = function(){

    }
    $.ajax({
      type: "GET",
      url: "roster",
      success: function(response){
        let html = response;
      },
      error: function(error){
        console.log(error)
      }
    })

});
