

document.getElementById("btnLeistung").addEventListener("click",addLeistung);

function addLeistung() {
    const li = document.createElement("li");
    li.textContent = document.getElementById("inputLeistung").value;;
    document.getElementById("listLeistung").appendChild(li);

    hervorheben();
}

function hervorheben() {
    const eintraege = document.querySelectorAll("ul li")

    for(i = 0; i < eintraege.length; i++) {
        const eintrag = eintraege[i];
        eintrag.textContent = "✔️" + eintrag.textContent
    }
}