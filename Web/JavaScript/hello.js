let named = "karim";
let alter = 22;
let altern =22n;
let x;
function isVolljaegrif(person,alter){

    if(named == "karim" && alter >= 18){
        return true
    }
    else {
        return false
    }
}

console.log(isVolljaegrif(named,alter))


let a = 9999999999999999;  // number (über 2**53, deshalb vermutlich ungenau)
let b = 9999999999999999n; // bigint (exakt)
console.log( a); // "number"
console.log(alter === altern); // "bigint"

// Lambda
const say_hello = function (name){
    console.log("Hallo, "+ name);
};

say_hello("karim")

// Arrow Funktion
const addZahl = (a,b) => a + b;

const addZahl2 = (a,b) => {
    return a + b
};


// this
let person = {
  name: "Anna",
  greet: () => {
    console.log("Hallo, ich bin " + this.name);
  }
};


function countBinaryOne(b) {
    let sum = 0;

    while (b !== 0) {
        if (b % 10 === 1){
            sum = sum + 1
        }
        b = Math.trunc(b / 10);
    }
    console.log("Summe: "+sum);
}

countBinaryOne(10010);