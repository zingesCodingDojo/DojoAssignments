$(document).ready(function(){
    // alert("You are now working with jQuery!");
    listTheHosues();
});

// I want to click the image and get information about the house using the Game of Thrones API
// Need HOUSE NAME, WORDS, TITLES
function listTheHosues(){
    
    if($(".btn-baratheon").click(function(){
        clearNames();
        $.get("https://anapioficeandfire.com/api/houses/17", function(res){
            houseDetails(res.name, res.words, res.titles);
        });
    }));
    if($(".btn-lannister").click(function(){
        clearNames();
        $.get("https://www.anapioficeandfire.com/api/houses/229", function(res){
            houseDetails(res.name, res.words, res.titles);
        });
    }));
    if($(".btn-stark").click(function(){
        clearNames();
        $.get("https://www.anapioficeandfire.com/api/houses/362", function(res){
            houseDetails(res.name, res.words, res.titles);
        });
    }));
    if($(".btn-targaryen").click(function(){
        clearNames();
        $.get("https://www.anapioficeandfire.com/api/houses/378", function(res){
            houseDetails(res.name, res.words, res.titles);
        });
    }));
    addSpaceAfterComma();
};

// Getting details
function houseDetails(name, words, titles){
    // console.log(name);
    // I am making a div to place all the data inside.
    $(".houseName").text(name);
    $(".houseWords").text(words);
    for(var i = 0; i < titles.length; i++){
        if(i + 1 == titles.length){
            $(".houseTitles").append(titles[i] + ".");
        }
        else{
            $(".houseTitles").append(titles[i] + ",<br>");
        };
    };
}

// I want to add a space after a comma for all P tags
function addSpaceAfterComma(){
    $("p").text(function(i, val){
        console.log("I am inside the P tags!")
        return val.replace(/,/g, ", ");
    })
}

function clearNames(){
    $(".houseTitles").empty();
}