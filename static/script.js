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
            packDiv.className = "list-group-item";
            packDiv.textContent = `Paquet ${index + 1}: ${pack.join(", ")}`;
            document.getElementById("packs").appendChild(packDiv);
        });
        document.getElementById("distributionResult").classList.remove("hidden");
    })
    .catch(error => console.error("Erreur:", error));
}
