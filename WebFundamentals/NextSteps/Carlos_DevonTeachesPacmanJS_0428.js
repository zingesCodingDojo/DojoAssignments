$(document).ready(function(){
    // alert("hello");
    console.log(Row());
    RenderMap(map_01);
});
// Keydown tracker!
$(document).keydown(function(e){
    console.log(e)
    switch(e.keyCode){
        // move pacman left
        case 37:
            break;
        // move pacman right!
        case 39:
            break;
        // move pacman up!
        case 38:
            break;
        // move pacman down
        case 40:
            break;
        
        default:
    }
})

// define pacman object
var pacman = {
    x: 1,
    y: 1
}

// define map as array
var map_01 = [
    [2,2,2,2,2,2,2,2,2,2,2],
    [2,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,3,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,2],
    [2,2,2,2,2,2,2,2,2,2,2]
];

// iterate array and create elements and append
function RenderMap(map){
    map[pacman.y][pacman.x] = 0;
    for(var i = 0; i < map.length; i++){
        var newRow = Row();
        for(var j = 0; j < map[i].length; j++){
            // initialize tile element
            var tile;
            // set tile based on array value
            if(map[i][j] == 2){
                $(newRow).append(Brick());
            }
            else if(map[i][j] == 1){
                $(newRow).append(Coin());
            }
            else if (map[i][j] == 3){
                $(newRow).append(Empty());
            }
            else{
                pacman.x = j;
                pacman.y = i;
                $(newRow).append(Pacman());
            }
            
            // console.log(map[i][j])
        }
        $("#board").append(newRow);
    }
}


// Three helper functions
// build row Element and return it
function Row(){
    var row = $("<div class='row'></div>");
    console.log(row)
    return row;

}

// build a brick and return it
function Brick(){
    return $("<div class='brick'></div>");
}

// build a coin and return it
function Coin(){
    return $("<div class='coin sprite'></div>");
}

// empty space element
function Empty(){
    return $("<div class='sprite'></div>")
}

// build a pacman and return itfunction Brick(){
function Pacman(){
    return $("<div class='pacman'></div>");
}