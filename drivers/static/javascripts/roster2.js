$(document).ready(function(){

  //https://logistics.amazon.com/internal/capacity/rosterview?serviceAreaId=11&date=2018-03-27
  let myDate = new Date();
  let todayDate = myDate .getFullYear() + "-" + myDate.getDate() + "-" + myDate.getDay();
  let baseRosterUrl = "https://logistics.amazon.com/internal/capacity/rosterview?serviceAreaId=11&date=" + todayDate;
  let baseUrl = "https://dsf3-flex.herokuapp.com/drivers/";
  let localUrl = "http://localhost:8000/drivers/roster";
  let driverUrl = "http://localhost:8000/drivers/";

  function toNode(html){
    var doc = document.createElement('html');
    doc.innerHTML = html;
    return doc;
  }

  function createCORSRequest(method, url) {
    var xhr = new XMLHttpRequest();
    if ("withCredentials" in xhr) {
      // XHR for Chrome/Firefox/Opera/Safari.
      xhr.open(method, url, true);
    } else if (typeof XDomainRequest != "undefined") {
      // XDomainRequest for IE.
      xhr = new XDomainRequest();
      xhr.open(method, url);
    } else {
      // CORS not supported.
      xhr = null;
    }
    return xhr;
  }

  function getRoster(text){
    var script = document.createElement("SCRIPT");
    script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js';
    script.type = 'text/javascript';

    script.onload = function() {
      var $ = window.jQuery;

       var doc = document.createElement('html');
       var body = $('h1');
       console.log(text);
       console.log(doc);
       console.log(body);
      // doc.innerHTML = html;
      // return doc;
      //https://logistics.amazon.com/internal/capacity/rosterview?serviceAreaId=11&date=2018-03-27

      driversArray = []
      let node = $('body');
      let roster = $(node).find('#cspDATable > tbody')[1].children;
      for(let i = 0; i < roster.length; i++){
        let driver = $(roster[i], 'tr')[0].children;
        let driverId = $(driver[0]).text();
        let driverName = $(driver[1]).text();
        let driverCurrentStatus = $(driver[2]).text();
        let driverBlockTime = $(driver[4]).text();
        let driverStartTime = $(driver[5]).text();
        let driverEndTime = $(driver[6]).text();

        driversArray.push({'id': driverId, 'name':driverName, 'blockTime': driverBlockTime, 'startTime': driverStartTime, 'endTime': driverEndTime});
      }

      console.log(driversArray);
      return driversArray;
    };
    document.getElementsByTagName("head")[0].appendChild(script);

  };


  // Make the actual CORS request.
  function makeCorsRequest() {
  // This is a sample server that supports CORS.
    var url = baseRosterUrl;

    var xhr = createCORSRequest('GET', url);
    if (!xhr) {
      alert('CORS not supported');
      return;
    }

    // Response handlers.
    xhr.onload = function() {
      var text = xhr.responseText;
      var roseterData = getRoster(text);
    };

  xhr.onerror = function() {
    alert('Woops, there was an error making the request.');
  };

  xhr.send();
}

makeCorsRequest();

})



//     //https://logistics.amazon.com/internal/capacity/rosterview?serviceAreaId=11&date=2018-03-27
//     let date = new Date()
//     let toDate = date.getFullYear() + "-" + date.getDate() + "-" + date.getDay()
//     let baseRosterUrl = "https://logistics.amazon.com/internal/capacity/rosterview?serviceAreaId=11&date=" + todayDate
//     let baseUrl = "https://dsf3-flex.herokuapp.com/drivers/";
//     let localUrl = "http://localhost:8000/drivers/roster";
//     let driverUrl = "http://localhost:8000/drivers/";
//
//     $.ajax({
//       type: "GET",
//       url: baseRosterUrl,
//       success: function(response){
//           driversArray = []
//           let node = toNode(response)
//           let test = $(node).find('#cspDATable > tbody')[1].children;
//           for(let i = 0; i < test.length; i++){
//             let driver = $(test[i], 'tr')[0].children
//             let driverId = $(driver[0]).text()
//             let driverName = $(driver[1]).text()
//             let driverCurrentStatus = $(driver[2]).text()
//             let driverBlockTime = $(driver[4]).text()
//             let driverStartTime = $(driver[5]).text()
//             let driverEndTime = $(driver[6]).text()
//
//             driversArray.push({'id': driverId, 'name':driverName, 'blockTime': driverBlockTime, 'startTime': driverStartTime, 'endTime': driverEndTime})
//           }
//           var csrftoken = Cookies.get('csrftoken');
//           console.log(csrftoken)
//           $.ajax({
//             type: "POST",
//             data: {
//               data: driversArray,
//                csrfmiddlewaretoken: csrftoken
//             },
//             url: baseUrl,
//             success: function(response){
//               console.log(response)
//             },
//             error: function(response){
//               console.log(response)
//             }
//           })
//
//
//           $('.test').html(JSON.stringify(driversArray))
//           console.log(baseRosterUrl)
//       }
//     })
//
// });


//------------------------------------------------------------------------------

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
