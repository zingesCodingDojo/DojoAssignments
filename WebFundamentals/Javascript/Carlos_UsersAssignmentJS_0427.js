$(document).ready(function(){
    stopSubmit();
});

function stopSubmit(){
    $("#user_input_form").submit(function(e){
        console.log("Hello")
        e.preventDefault();
        GimmeValues(e.target.children);
    });
}

function GimmeValues(data){
    var firstName = data.first_name_input.value; var li1 = document.createElement("li");
    var lastName = data.last_name_input.value; var li2 = document.createElement("li");
    var emailInfo = data.email_input.value; var li3 = document.createElement("li");
    var phoneNumber = data.phone_input.value; var li4 = document.createElement("li");

    // li1.innerText = data.firstName.value;
    $(li1).text(firstName);
    $(li2).text(lastName);
    $(li3).text(emailInfo);
    $(li4).text(phoneNumber);
    
    $(".first_name_output").append(li1);
    $(".last_name_data_output").append(li2);
    $(".email_data_output").append(li3);
    $(".contact_number_output").append(li4);

}
