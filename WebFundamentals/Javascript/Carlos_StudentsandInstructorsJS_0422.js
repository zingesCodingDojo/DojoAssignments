/*
Create a program that outputs:
Michael Jordan
John Rosales
Mark Guillen
KB Tonel
*/

var students = [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]

function arraywithObjects(arr){
    for(var items in arr){
        console.log(arr[items].first_name + " " + arr[items].last_name)
    }
}
arraywithObjects(students);

/*
Expected results:
Michael Jordan
John Rosales
Mark Guillen
KB Tonel
*/


/*
Create a program that prints the folowing format
including the number of characters in each combined name:
*/
var users = {
 'Students': [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }

function orgArrayObject(arr){
    for(var items in arr){
        console.log(items)
        var counter = 1;
        var tempItem = arr[items];
        //console.log(tempItem.length);
        for(var key in tempItem){
            var tempKey = tempItem[key];
            var namesLength = (tempItem[key].first_name).length + (tempItem[key].last_name).length;
            console.log(counter + " - " + tempItem[key].first_name + " " + tempItem[key].last_name + " - " + namesLength);
            for(var value in tempKey){
                //console.log(counter + " - " + tempKey[value].first_name)
                counter++;
            }
        }
    }
}
orgArrayObject(users);

/*
Expected results:
Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13
*/