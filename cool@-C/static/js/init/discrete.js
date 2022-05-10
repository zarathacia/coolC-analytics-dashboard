$(document).ready(function() {
    fetch_weather()
    fetch_measures()
});

function fetch_weather() {
    $.ajax({
        url: "/api/weather/"
    }).then(function(data) {
        console.log(data.main.temp)
       $('#temperature').html(data.main.temp);
       console.log("here")
    });
}

function fetch_measures() {
    $.ajax({
        url: "api/measure"
    }).then(function(data) {
       console.log(typeof(data))
       $('#hello').html(data[0].Temp);
       console.log("here")
    });
}

function BarChartByday(){
    $.ajax({
        url: "/api/average"
    }).then(function(data) {

       //$('#temperature').html(data.main.temp);
  
    });
}


