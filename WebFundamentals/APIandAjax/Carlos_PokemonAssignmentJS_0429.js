$(document).ready(function(){
    clickRandomButton();
    // alert("turd")
    pokeDorkPopulation();
    
});

// I want to generate a random pokedork!
function returnRandomPokemon(){
    var randomPokemon = Math.trunc(Math.random()* 151)+1
    // console.log(randomPokemon)
    return randomPokemon
}

// After generating a random pokedok, I must trieve it from the API and then create the sprite in getPokemonSprite!
function clickRandomButton(){
    $(".btn_randoPokeDORK").click(function(){
        $.get("http://pokeapi.co/api/v2/pokemon/" + returnRandomPokemon(), function(res){
            // console.log(res.name);  This was used for checking if the name worked when pinging the API.
            // console.log(res.sprites.front_default) This was used to ping for the POKEDORK picture URL.
            // console.log(res.types[1]["type"].name) This was used for pinging the secondary TYPE of a pokemon.
            // At this version, the software will CRASH if the pokemon has only ONE type. So, we are disabling the second type.
            getPokemonSprite(res.sprites.front_default, res.id, res.name, res.height, res.weight);//, res.types[1]["type"].name);
            getPokeDORKtypes(res);
           
        }); 
    })
};

// Since I am pulling the types function in two different places, lets make a function.
function getPokeDORKtypes(res){
    // I want to get the pokeDORK type!
    for(var items in res.types){

        // Since it is possible the pokemon won't have a type via the API, lets make generic values.
        if(res.types[items]["type"].name == undefined){
            // console.log("Nothing to see...")
            $(".typePrimary").text("Herp derp. Nothing.");
            $(".typeSecondary").text("Herp derp. Nothing.");
            break
        }

        // If there is a first POKEDORK type, this will display it for primary type.
        if(items == 0){
            $(".typePrimary").text(res.types[items]["type"].name);
            // console.log("First item!");
            $(".typeSecondary").text("Only: " + res.types[items]["type"].name);
        }

        // If tehre is a secondary type, this will display it for the secondary type.
        else if(items == 1){
            $(".typeSecondary").text(res.types[items]["type"].name);
            // console.log("Second")
        }
        // console.log(res.types[items]["type"].name);
    }
}


// I want to get the sprite of the pokemon!
function getPokemonSprite(src, id, name, height, weight){ //
    // console.log(type1);
    // var someDorkName = document.getElementsByClassName("pokeDorkName");
    // changes pokeDORK name
    $(".pokeDorkName").text(name); 
    // adds pokeDORK weight
    $(".weight").text(weight);
    $(".height").text(height);
    // adds pokeDORK type2
    // $(".typeSecondary").text(type2);
    // console.log($(".weight").text(weight + " POUNDS!"))
    // Adds pokeDORK img
    $("#img_pokeDORK").attr("src", src);
}

// This will get ALL pokeDORKs to quickly populate the page.
function pokeDorkPopulation(){
    // console.log("I have entered Pokedork Button")
    var getAllPokedorks = "http://pokeapi.co/api/v2/pokemon/"
    for(var i = 1; i < 152; i++){
        $.get(getAllPokedorks + i, function(res){
            // getAllPokedorks = getAllPokedorks + i;
            var newPokemonButton = document.createElement("button");
            newPokemonButton.setAttribute("type", "button" + i);
            newPokemonButton.setAttribute("class", "newPokeDorkbutton" + i);
            
            $("#manual_mode").append(newPokemonButton);
            $(newPokemonButton).append("<img src='" + res.sprites.front_default +"' alt='temp'>");
            $(newPokemonButton).click(function(){
                $(".pokeDorkName").text(res.name);
                $(".weight").text(res.weight);
                $(".height").text(res.height);
                getPokeDORKtypes(res);
                $("#img_pokeDORK").attr("src", res.sprites.front_default);
            })
        });
    };
;}