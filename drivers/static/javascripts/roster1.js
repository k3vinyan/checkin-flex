$(document).ready(function(){

    // let transporterId, DAName, availability, duration, startTime, endTime, isSameDayRequest;
    //
    // //Not Arrived, Finished, DRIVING, Active
    //
    // function Driver(transporterId, DAName, availability, duration, startTime , endTime, isSameDayRequest){
    //   this.transporterId = transporterId;
    //   this.DAName = DAName;
    //   this.availability = availability;
    //   this.duration = duration;
    //   this.startTime = startTime;
    //   this.endTime = endTime;
    //   this.isSameDayRequest = isSameDayRequest;
    // };
    //
    // let isAvailable = function(){
    //
    // }
    // $.ajax({
    //   type: "GET",
    //   url: "roster",
    //   success: function(response){
    //     let html = response;
    //   },
    //   error: function(error){
    //     console.log(error)
    //   }
    // })

    function toNode(html){
      var doc = document.createElement('html');
      doc.innerHTML = html;
      return doc;
    }

    //https://logistics.amazon.com/internal/capacity/rosterview?serviceAreaId=11&date=2018-03-27
    let date = new Date()
    let todayDate = date.getFullYear() + "-" + date.getDate() + "-" + date.getDay()
    baseRosterUrl = "https://logistics.amazon.com/internal/capacity/rosterview?serviceAreaId=11&date=" + todayDate

    $.ajax({
      type: "GET",
      url: "http://localhost:8000/drivers/roster",
      success: function(response){
          driversArray = []
          let node = toNode(response)
          let test = $(node).find('#cspDATable > tbody')[1].children;
          for(let i = 0; i < test.length; i++){
            let driver = $(test[i], 'tr')[0].children
            let driverId = $(driver[0]).text()
            let driverName = $(driver[1]).text()
            let driverCurrentStatus = $(driver[2]).text()
            let driverBlockTime = $(driver[4]).text()
            let driverStartTime = $(driver[5]).text()
            let driverEndTime = $(driver[6]).text()

            driversArray.push({'id': driverId, 'name':driverName, 'blockTime': driverBlockTime, 'startTime': driverStartTime, 'endTime': driverEndTime})
          }
          var csrftoken = Cookies.get('csrftoken');
          console.log(csrftoken)
          $.ajax({
            type: "POST",
            data: {
              data: driversArray,
               csrfmiddlewaretoken: csrftoken
            },
            url: "http://localhost:8000/drivers/",
            success: function(response){
              console.log(response)
            },
            error: function(response){
              console.log(response)
            }
          })


          $('.test').html(JSON.stringify(driversArray))
          console.log(baseRosterUrl)
      }
    })

});
