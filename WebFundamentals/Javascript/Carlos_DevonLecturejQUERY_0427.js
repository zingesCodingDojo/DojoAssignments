$(document).ready(function(){
    //
    var numPokemon = prompt("How many pokemons");
    GetThePokemons(numPokemon);
    $("#container").on("click", ".pokeButton", function(){
    MorePokeInfo($(this).attr("data-id"));
        });
})


function GetThePokemons(numPokemon){
    for(var i = 1; i <= numPokemon; i++){
        $.get("http://pokeapi.co/api/v2/pokemon/" + i, function(res){
            console.log(res.sprites.front_default);
            ResThePokemon(res.sprites.front_default, res.id);
        });
    }
};

function ResThePokemon(src, id){
    // var myImg = document.createElement("img");
    // myImg.setAttribute("src", src)
    // $("#container").append("<img src='" + src + "' alt=''>");
    // $("#container").append(myImg);
    var someButton = document.createElement("button");
    someButton.setAttribute("class", "pokeButton");
    someButton.setAttribute("data-id", id);
    $("#container").append(someButton);
    $(someButton).append("<img src='" + src + "' alt=''>");
};

function MorePokeInfo(id){
    console.log(id, "Got this ID from MorePokeInfo")
    $.get("http://pokeapi.co/api/v2/pokemon/" + id, function(res){
        console.log(res);
        //build an h1
        //build an image
        //build an ul from array(moves)

        //build an h2 (weight)
    });
};

function SetMoves(moves){
    // create an ul
    var ul = "";
    // loop through moves
        // create lis
        // set inner text to move
}