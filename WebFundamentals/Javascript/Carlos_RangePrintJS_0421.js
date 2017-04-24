//Range Print! We are using the range function in JS!
function randomPrinting(start, end, skips){
    // var newValues = []
    var tempSkips = 0
    var initialSkip = start + skips
    if(end < 0 || skips < 0){
        console.log("Do you want count negative numbers?")
        randomNegativePrinting(start, end, skips);
        
    }
    else if(start >= end){
        console.log("WOW your START is greater than your END. Give me a start integer SMALLER than your END number.")
    }

    else if(initialSkip>=end){
        console.log("I cannot exceed the final number and adding the skipper to the start violates this rule.")
    }
    else if(skips == 0){
        console.log("You failed to give me a skipping number... I will add 1 until I reach the end.")
        while(start <=end){
            console.log(start + " out of " + end)
            start++
        }   
    }
    else if(skips >0){
        
        console.log(start + " is the first number!")

        while(initialSkip < end){
            var tempChecker = initialSkip + skips
            if(initialSkip >= end || tempChecker >= end){
                break
            }
            else{
                
                console.log(initialSkip + " going all the way to... " + end)
            }
            initialSkip += skips
        }
        console.log(initialSkip + " was the final number before hitting " + end)
    }
    
}
randomPrinting(55, -90, -1);

function randomNegativePrinting(start, end, skips){
    // var newValues = []
    var tempSkips = 0
    var initialSkip = start + skips
    if(start < end){
        console.log("... I am too lazy to add another function for now.")
    }
    else if(skips > 0){
        console.log("Please enter a negative skips value if you want to go backwards...")
    }
    else if(start > end){
        console.log("Going backwards..")
        while(initialSkip > end){
            var tempChecker = initialSkip + skips
            if(initialSkip <= end || tempChecker <= end){
                break
            }
            else{
                console.log(initialSkip + " am i going backwards to " + end + " ?")
            }
            initialSkip += skips
        }
        console.log(initialSkip + " was the final number before negatively hitting " + end)

    }
}
// randomNegativePrinting(-1, -5, -1)