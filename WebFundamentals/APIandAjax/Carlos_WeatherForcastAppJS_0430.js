$(document).ready(function(){
    clickWeather();
    // alert("halt!")
});

// I want to get the value from the user input bar.
function clickWeather(){
    $(".search_bar_button").click(function(){
        var getInput = $(".search_bar_input").val();
        // console.log(getInput);
        $.get("http://api.openweathermap.org/data/2.5/weather?q=" + getInput + "&APPID=1c99c00262b32485b28a5644d7236cb6", function(res){
            // console.log(res.weather[0].main);
            showWeather(res.name, res.main.temp, res.weather[0].main);
            // console.log(res.name);
        });
    });
    
}

// I want to append the data I receive from the weather API
function showWeather(name, temp, main){
    // console.log(name);
    // I am making a div to place all the data inside.
    var newDiv = document.createElement("div");
    newDiv.setAttribute("class", "weatherShower");
    $("#master").append(newDiv);
    var newCityTitle = document.createElement("h1");
    newCityTitle.setAttribute("class", "newCity");
    $(newCityTitle).text(name);
    $(newDiv).append(newCityTitle);

    // We have the Div and the city. Next is some stats.

    var newTemperature = document.createElement("h2");
    newTemperature.setAttribute("class", "newTemp");
    temp = temp * 9/5 - 459.67;
    var shorterTemp  = temp.toFixed(2);
    $(newTemperature).text("Temperature: " + shorterTemp + " °F");
    $(newDiv).append(newTemperature);
    
    var newMainTrend = document.createElement("p");
    newMainTrend.setAttribute("class", "newTrend");
    $(newMainTrend).text("Main weather trend... " + main);
    $(newDiv).append(newMainTrend);
}