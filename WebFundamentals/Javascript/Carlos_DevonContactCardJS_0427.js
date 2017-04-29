$(document).ready(function(){
    newCall();
});

function newCall(){ $("#theForm").submit(function(e){
    e.preventDefault();
    console.log(e.target.children);
    // console.log(e.children.desc.value);
    buildACard(e.target.children);
})};

function buildACard(data){
    console.log(data);
    // build the card div
    var card = document.createElement("div");
    // $("#container").append("<div></div>").addClass("contact-card");
    // console.log(card)
    // build the first name
    var name = document.createElement("h1");
    // name.innerText = data.firstName + " " + lastName;
    $(name).text(data.firstName.value + " " + data.lastName.value)
    // var firstname = $(card).append("<h1></h1>").text(data.firstName);
    // console.log(firstName)
    // build the last name

    // build the desc
    var desc = document.createElement("p");
    $(desc).text(data.desc.value)

    // append content to card
    card.appendChild(name).appendChild(desc);

    // access container and append to our card to it
    var cont = document.getElementById("container");
    
    cont.appendChild(card)
}