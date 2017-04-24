/*
The purpose of this assignment is to display an array index number + user string + array index value.
It is optional to allow the array to be reversed. We are adding this feater!
We will also add a feature to make sure an array and a string are passed into the function.
*/
var userPick = "";
var arr = [];
var backwards = false

function superTest(arr, userPick, backwards){
    var zeroCounter = 0;
    var minusCounter = arr.length-1;
    var tempArror = "-->"
    if(userPick.length == 0){
        console.log("Inserting " + tempArror + "...");
        userPick = tempArror;
    }

    if(backwards){
        console.log("Giving array in reversed order...")
        for(var i = arr.length-1; i > -1; i--){
            console.log(minusCounter + " " + userPick + " " + arr[i]);
            minusCounter--;
        }
    }
    else{
        console.log("Giving array in forwards order...")
        for(var n = 0; n < arr.length; n++){
            console.log(zeroCounter + " " + userPick + " " + arr[n]);
            zeroCounter++;    

        }
    }
}
//The variable fancyArray is a placeholder for testing the code above. But, any array should work.
var fancyArray = ["James", "Jill", "Jane", "Jack"];
superTest(fancyArray, "---->", backwards=true);