// We are making a counter that will iterate through each minute of each hour in a day!
// This does not actually keep track of time. It just goes through time values... not actual time.
function timeannoyer(){
    var tempMinute = 0
    var tempHour = 0
    var am = "AM"
    var pm = "PM"
    var fullDay = 0
    while(fullDay < 24){

        if(tempHour >=12){
            am = pm
            if(tempHour == 13){
                tempHour = 1
            }
            
        }
        if(fullDay == 12){
            console.log("It is now NOON!")
        }
        
        var addanHour = tempHour + 1
        while(tempMinute <60)
        {
            if(tempMinute == 15){
                console.log("Quarter past.. " + tempHour + am)
            }
            
            else if(tempMinute == 30){
                console.log("We reached middle of the hour... " + tempHour + ":" + tempMinute + am)
            }

            else if(tempMinute == 45){
                if(fullDay == 12){
                    console.log("We are 15 minutes away from: 1PM!")
                }
                else{
                    console.log("We are 15 minutes away from: " + addanHour + am)
                }
            }
            // The code below is meant to show each minute....
            else{
                // console.log("It is now " + tempHour + ":" + tempMinute + am)
            }
            tempMinute++
        }
        tempMinute = 0
        tempHour++

        fullDay++
    }
    console.log("Midnight.")
}
timeannoyer()