/*
CountDown
Create a function that accepts a number as an input. Return the new array that counts down by one,
from the number (as array's zero'th element) down to 0 (as the last element). How long is this array?
*/
function CountDown(x){
    var newArray = [];
    while(x >-1){
        newArray.push(x);
        x--
    }
    console.log(newArray);
    return newArray;
}
// CountDown(50); --- Enable me to try the CountDown function!

/*
Print and Return
Your function will receive an array with two numbers. Print the first value, and reutrn the second.
 */
function PrintandReturn(arr){
    var endArray = arr.length - 1
    console.log(arr[0]);
    return endArray;
}
// var usefulArray = CountDown(50); --- Enable me to try the Print and Return function!
// var pringtingTemp = PrintandReturn(usefulArray); --- Enable me to try the Print and Return function!
// Printandreturn();

/*
First Plus Length
Given an array, return the sum of the first value in the array, plus the array's length. What happens
if the array's first value is NOT a number, but a string(like "what?") or a boolean (like flase).
*/
function FirstPlusLength(x){
    var arrLength = x.length - 1
    if(typeof x[0] == "number"){
        var newValue = x[0] + arrLength
        console.log("Value of arr[0] and arr.length is: " + newValue)
        return newValue
    }
    else{
        console.log("Your arr[0] is not a number datatype! So, I will tell you that your array.length is: " + arrLength)
    }

}
//var zeroAndLength = FirstPlusLength(usefulArray); // YOU MUST ENABLE usefulArray variable!!!

/*
Values Greater than Second
For [1, 3, 5, 7, 9, 13], print values greater than its second value. Return how many values this is.
*/
var valuesArray = [1, 2, 3, 5, 7, 9, 13]
function ValuesGreaterThanSecond(arr){
    var tempCounter = 0;
    for(var i = 0; i < arr.length; i++){
        if(i > 1){
            tempCounter++;
            console.log("Past arr[1]! Your current value is: " + arr[i]);
        }
    }
    console.log("Your array length past its second value is: " + tempCounter);
    return tempCounter;
}
//ValuesGreaterThanSecond(valuesArray);  --- Enable me to test out ValuesGreaterThanSecond!

/*
Values Greater than Second, Generalized
Write a function that accepts ANY array, and returns a new array with the array values greater
than its second value. Print how many values this is. What will you do if the array is only one element long?
*/
function GreaterThanSecondGeneralized(arr){
    var newArray = [];
    var tempCounter = 0;
    if(arr.length < 1){
        console.log("Your array has zero elements... we are returning a false value...")
        return false
    }
    else if(arr.length < 3){
        console.log("You have 2 or less elements in your array... returning false.")
        return false
    }
    else{
        for(var i = 0; i < arr.length; i++){
            if(i>1){
                tempCounter++
                console.log("Adding... " + arr[i] + " to your new array!")
                newArray.push(arr[i])
            }
        }
    return newArray
    }
}
var emptyArray = [1, 2, 3]
//GreaterThanSecondGeneralized(emptyArray); --- Enable me to test out Values Greater than Second, Generalized!

/*
This Length, That Value
Given two numbers, return the array of length num1 with each value num2. Print "Jinx" if they are the same.
*/
function ThisLengthThatValue(arr){
    var newArray = [];
    for(var i = 0; i < arr.length ; i++){
        if(arr[i] == arr.length){
            console.log("Your current array index value is: " + arr[i], "Your array length is: " + arr.length);
            console.log("Jinx!");
            newValue.push(arr[i])
        }
    }
    return newArray
}
//ThisLengthThatValue(emptyArray); --- Enable me to test out ThisLengthThatValue!

/*
FitTheFirstValue
Your function should accept an array. If this value at [0] is greater than array's length, print "Too big!",
if value [0] is less than array's length, print "Too small!", otherwise print "Just right!"
*/
function FitTheFirstValue(arr){
    var minIndex = arr[0]
    var maxIndex = arr.length - 1
    if(minIndex == maxIndex){
        console.log("Just right!")
    }
    else if(minIndex > maxIndex){
        console.log("Too big!")
    }
    else if(minIndex < maxIndex){
        console.log("Too small!")
    }
}
var tooBigArray = [5, 0, 2, 4]
var justRightArray = [3, 0, 2, 4]
//FitTheFirstValue(emptyArray); --- Enable me to test out FitTheFirstValue!

/*
Fahrenheit to Celcius
Kelvin wants to convert between temperature scales. Create farenheitToCelcius(fDegrees)
that accepts a number of degrees in Fahrenheit, and returns the equivalent temperature as expressed
in Celcius degees. For review, Fahrenheit = (9/5 * Celcius) + 32.
*/
function FahrenheitTofahrenheitToCelcius(fDegrees){
    var celciusConverter = (fDegrees - 32) * 5/9
    var fahrenheitConverter = (9/5 * celciusConverter) + 32
    console.log("Celsius temp: " + celciusConverter, "Fahrenheit temp: " + fahrenheitConverter)
}
//FahrenheitTofahrenheitToCelcius(40); --- Enable me to test out FahrenheitTofahrenheitToCelcius!

/*
Celcius to Fahrenheit
Create celciusToFahrenheit(cDegrees) that accepts number of degrees Celcius, and returns
the equivalent temperature expressed in Fahrenheit degrees.
(optional) Do Fahrenheit and Celsius values equate at a certain number? Scientific calculation can be
complex, so for this challenge just try a series of Celsius integer values starting at 200, going downward
(descending), checking whether it is euqal corresponding Fahrenheit value.
*/
function celsiusToFahrenheit(cDegrees){
    // var fahrenheitConverter = (9/5 * cDegrees) + 32
    while(cDegrees > -200){
        var fahrenheitConverter = (9/5 * cDegrees) + 32
        console.log("Did you know the current temeperature, in fahrenheit, is: " + fahrenheitConverter,
        "In celcius, it is: " + cDegrees)
        if(cDegrees == Math.trunc(fahrenheitConverter)){
            console.log("WOW! The temperatures are the same number! " + "celsius: " + cDegrees + " fahrenheit: " + fahrenheitConverter)
            break
        }
        cDegrees--
    }
}
celsiusToFahrenheit(200);