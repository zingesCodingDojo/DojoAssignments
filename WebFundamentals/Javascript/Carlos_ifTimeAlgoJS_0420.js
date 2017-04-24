// var HOUR = 8;
// var MINUTE = 50;
var PERIOD = "AM";

function TimeUpdate(){
    var hourMinutes = 59;
    var dayHour = 23;
    var minuteCounter = 0;
    var dayCounter = 0;
    var iterateCounter = 0;
    while(iterateCounter <= 23)
    {
        
        var tempHour = dayCounter + 1;
        var tempNormalHours = dayCounter - 12;
        console.log(tempNormalHours)
        //Noon and PM settings!
        if(dayCounter == 12){
            console.log("Noon")
            PERIOD = "PM"
        }

        else if(dayCounter >= 12){
            tempHour = tempNormalHours
            // dayCounter = tempNormalHours
        }

        while(minuteCounter < 60){
            
            if(minuteCounter == 30){
                if(dayCounter == 12){
                    console.log("It is now 12:30 PM!")
                }
                
                else if(tempNormalHours == 2 || tempNormalHours == 12){
                    if(tempNormalHours == 2){
                        console.log("11111111Did you know it is now 12" + ":" + minuteCounter + "PM");
                    }
                    else{
                        console.log("22222Did you know it is now 12" + ":" + minuteCounter + "AM");
                    }
                }
                
                else if(dayCounter >= 11){
                    
                    console.log("3333Did you know it is now " + tempHour + ":" + minuteCounter + PERIOD);
                    
                }
                else{
                    console.log("4444Did you know it is now " + dayCounter + ":" + minuteCounter + PERIOD);
                }
            }
            
            else if(minuteCounter == 25){
                if(dayCounter >= 12){
                    if(dayCounter == 12){
                        console.log("Quarter after Noon.")
                    }
                    else{
                    console.log("Quarter after " + tempHour + PERIOD);
                    }
                }
                else{
                    console.log("Quarter after " + dayCounter + PERIOD)
                }
                
            }
            else if(tempNormalHours == 0 && minuteCounter == 50){
                console.log("Bleh, 10 minutes till 1PM.")
            }
            else if(tempNormalHours == -1 && minuteCounter == 50){
                console.log("Super, only 10 more minutes till: Noon.")
            }
            
            else if(tempNormalHours == 11 && minuteCounter == 50){
                console.log("Nightowl, only 10 more minutes till: Midnight.");
            }
            
            else if(minuteCounter == 50){
                console.log("Wow, only 10 more minutes till: " + tempHour + PERIOD);
            }
            //The muted code below, with the exceptions above, will DISPLAY ALL MINUTES.
            // else{
            //     console.log("It is currently " + dayCounter + ":" + minuteCounter + PERIOD);
            // }
            minuteCounter++
        }
        minuteCounter = 0
        tempNormalHours++
        dayCounter++
        iterateCounter++
    }
}
TimeUpdate()