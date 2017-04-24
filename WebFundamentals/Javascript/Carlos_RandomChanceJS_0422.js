/*
We want to make a Random Chance function. It should be able to tell if a randomly
generated number equates to the player winning. Winning prize is anything from 50-100 quarters.
*/
function RandomChance(tries){
    console.log("Accepting: " + tries + " quarters! Let us play a game of chance!");
    for(var quarter = 1; quarter < tries; quarter++){  //Tries the player has attempted.S
        var randomWinnder = Math.floor(Math.random() * 100) + 1
        
        var quarterWinnings = Math.floor(Math.random() * 50) + 50; //Number of quarters the player wins.
        console.log(quarterWinnings);
        var quartersLeft = tries - quarter //Number of tries left!
        var newEarnigs = quartersLeft + quarterWinnings //Total earnings with quarters remaining.
        if(randomWinnder == 42){
            console.log("Winner!!! You have won: " + quarterWinnings + " quarters! It only took you: " + quarter + " tries. This means you had: " + quartersLeft + " quarters remaining. You now have: " + newEarnigs + " quarters!!! What a rich guy.");
            var earningsConversion = newEarnigs/4 //I want to know the dollar amount.
            if(earningsConversion > 0){
                console.log("This means... " + earningsConversion + " dollars!")
            break;
            }
        }
        else{
            console.log("Try again...")
        }
    }    
}
RandomChance(200);