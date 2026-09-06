

document.getElementById("btn1").addEventListener("click",greet)
function greet(){
    let inpName = document.getElementById("input").value;

    document.getElementById("lblWelcome").textContent  = "Willkommen bei der Softwareschmiede ProPy, " + inpName + "!";
}