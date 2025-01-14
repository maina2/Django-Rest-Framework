

let firstCard = getRandomCard()
let secondtCard = getRandomCard()
let thirdCard = getRandomCard()

let cards = [firstCard, secondtCard, thirdCard]



for (let i = 0; i <= cards.length; i++) {
    sum = + cards[i]

}

// let sentence = ["Hello","my","name","is","Chanzu"]

// let greetingEl = document.querySelector("#greeting-el");

// for(let i=0;i<sentence.length;i++){
//     greetingEl.textContent +=sentence[i]+" "; 
// }



let hasBlackjack = false;
let isAlive = true;

let message = "";


if (sum > 21) {
    message = "You can continue...";

}
else if (sum < 21) {
    message = "You lose"
    isAlive = false;
}
else {
    message = "Blackjack!";
    hasBlackjack = true;
}
console.log(message);
console.log(cards);


function getRandomCard() {
    let flooredNumber = Math.floor(Math.random() * 12) + 1;
    return flooredNumber;
}


let person = {
    name: "Pier",
    age: 22,
    country: "Kenya"
}

function logData() {
    let string = person.name + " " + "is" + " " + person.age + " " + "years old and lives in " + person.country;
    console.log(string);
}
logData();

let age = 75;

if (age < 6) {
    console.log("free")
}
else if (age > 6 && age < 17) {
    console.log("child discount")
}
else if (age > 18 && age < 26) {
    console.log("student discount")
}
else if (age > 27 && age < 66) {
    console.log("full price")
}
else {
    console.log("senior citizen discount")
}

let largeCountries = ["China", "India", "USA", "Indonesia", "Pakistan"];

// for(i=0;i<largeCountries.length;i++){
//     console.log("-"+" "+largeCountries[i])
// }

function getHand() {
    let randomIndex = Math.floor(Math.random() * 5)
    // let i = randomIndex;
    console.log(largeCountries[randomIndex]);
}

getHand();


let fruit = ["🍉", "🍉", "🍉", "🍉", "🍎", "🍎", "🍎"];

let watermelonShelf = document.getElementById("watermelons")
let appleShelf = document.getElementById("apples")

function arrangeFruits() {


    for (let i = 0; i < fruit.length; i++) {
        if (fruit[i] === "🍎") {
            appleShelf.textContent  += "🍎"

        }
        else if(fruit[i]==="🍉") {
            watermelonShelf.textContent += "🍉"
        }


    }


}
arrangeFruits();
