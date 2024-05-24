function generateDistribution() {
    var formData = new FormData(document.getElementById("beltForm"));
    fetch("/generate_distribution", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("packs").innerHTML = "";
        data.forEach((pack, index) => {
            var packDiv = document.createElement("div");
            packDiv.className = "pack";
            var packHeader = document.createElement("div");
            packHeader.className = "pack-header";
            packHeader.textContent = `Paquet ${index + 1}`;
            packDiv.appendChild(packHeader);

            var packContent = document.createElement("div");
            packContent.innerHTML = `
                <p>Ceintures GT    : ${pack[0]}</p>
                <p>Ceintures 125 cm: ${pack[0]}</p>
                <p>Ceintures 120 cm: ${pack[1]}</p>
                <p>Ceintures 115 cm: ${pack[2]}</p>
                <p>Ceintures 110 cm: ${pack[3]}</p>
                <p>Ceintures 105 cm: ${pack[4]}</p>
                <p>Ceintures 100 cm: ${pack[5]}</p>
            `;
            packDiv.appendChild(packContent);

            document.getElementById("packs").appendChild(packDiv);
        });
        document.getElementById("distributionResult").classList.remove("hidden");
    })
    .catch(error => console.error("Erreur:", error));
}
