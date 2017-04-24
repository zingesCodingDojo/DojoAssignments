//We want to see how many pennies (0.01) a servant will make in 30 days...
//How long will it take to make 10,000?
//One billion?
//Infinity?
//The servant makes 1 penny fiest day, 2 second day, 4 third day, 8, 16, and so on.

var dayPennies = 0.01
var tenThousandPennies = 1000000
var billionPennies = 1000000000
var totalDays = 1
var tempDollar = 100
//Lets check first 30 days.
while(totalDays <= 30){
    dayPennies = dayPennies + dayPennies
    console.log("Servant is getting rich..! Total monies: " + dayPennies + "Pennies!")
    //how many dollars is this?
    
    var tempPennies = dayPennies
    if(dayPennies > 100){
        tempPennies = dayPennies/tempDollar
        console.log("WOW! Servant has: " + Math.trunc(tempPennies) + " Dollars!")
    }
    totalDays++
}

function tenThousand(){
    var dayPennies = 0.01
    var tenThousandPennies = 1000000
    var totalDays = 1
    while(dayPennies <= tenThousandPennies){
        dayPennies = dayPennies + dayPennies
        totalDays++
    }
    console.log("It took me " + totalDays + " days to get over 10,000 pennies.")
    console.log("I have a total of " + dayPennies + " pennies")
}
tenThousand()

function oneBillion(){
    var dayPennies = 0.01
    var totalDays = 1
    var billionPennies = 100000000000
    while(dayPennies <= billionPennies){
        dayPennies = dayPennies + dayPennies
        totalDays++
    }
    console.log("It took me " + totalDays + " days to get over 1,000,000,000 pennies.");
    
}
oneBillion()

function lightyearInfinity(){
    var dayPennies = 0.01
    var totalDays = 1
    while(dayPennies <= Infinity){
        dayPennies = dayPennies = dayPennies
        totalDays++
    }
    console.log("It took the servant " + totalDays + " days to reach infinity... his current penny count is at: " + dayPennies)
}
lightyearInfinity()