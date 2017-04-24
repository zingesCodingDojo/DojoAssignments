/*
We are making a Numbers Only array.
First, design a function that will look into an array and copy over data type number only.
This means, we are creating a new array that would host the old arrays number datatype.
Any strings, booleans, objects would NOT be in the new array.
The bonus feature is to REMOVE anything that is not a number from the original
array and return the new array...
*/

var dummyArray = [0, "Ninja", 3, "Coding", "monday", 5, 10, "clasroom"];

function NumbersOnly(arr){
    var newArray = [];
    for(var i = 0; i < arr.length; i++){
        if(typeof arr[i] === "number"){
            newArray.push(arr[i])
        }
    }
  console.log(newArray);
  return newArray
}

NumbersOnly(dummyArray);

/*
Using the pop feature to remove items from an array does not work if its under a while
conditional and or for loop. This is because the index is constantly changing.
I think we can solve this problem if we switch the non-number data type to the END of
the array and then pop... maybe.
*/
function PopStringsFromArray(arr){
    
    for(var i = arr.length - 1; i > -1; i--){
        if(typeof arr[i] !== "number"){
            console.log(arr[i])
            var tempArrayNumber = arr[arr.length - 1]
            arr[arr.length - 1] = arr[i]
            arr[i] = tempArrayNumber
            console.log(tempArrayNumber)
            arr.pop()
        }
    }

    console.log(arr);
}

PopStringsFromArray(dummyArray);
