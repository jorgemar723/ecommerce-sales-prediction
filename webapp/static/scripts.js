document.addEventListener("DOMContentLoaded", function () {
    // 🌙 Dark Mode Toggle
    const darkModeToggle = document.getElementById("darkModeToggle");

    if (localStorage.getItem("darkMode") === "enabled") {
        document.body.classList.add("dark-mode");
    }

    darkModeToggle.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode");
        localStorage.setItem("darkMode", document.body.classList.contains("dark-mode") ? "enabled" : "disabled");
    });

    // 🎯 Handle Prediction Form
    document.getElementById("predictionForm").addEventListener("submit", async function(event) {
        event.preventDefault();

        document.getElementById("loadingMessage").style.display = "block"; // Show loading message

        const formData = new FormData(this);
        const jsonData = {};
        formData.forEach((value, key) => jsonData[key] = value);

        try {
            const response = await fetch("/predict", {
                method: "POST",
                body: new URLSearchParams(jsonData),
                headers: { "Content-Type": "application/x-www-form-urlencoded" }
            });

            const result = await response.json();
            document.getElementById("loadingMessage").style.display = "none"; // Hide loading message

            if (result.prediction) {
                document.getElementById("predictionOutput").textContent = `Predicted Units Sold: ${result.prediction}`;
                updateHistory(jsonData, result.prediction);
            } else {
                alert("Error: " + result.error);
            }
        } catch (error) {
            document.getElementById("loadingMessage").style.display = "none"; // Hide loading message
            alert("Failed to send request. Please check input values.");
        }
    });

    // 📝 Update Prediction History
    function updateHistory(inputData, prediction) {
        const historyList = document.getElementById("history");
        const listItem = document.createElement("li");

        let formattedInputs = "<ul>";
        for (const key in inputData) {
            formattedInputs += `<li><strong>${key}:</strong> ${inputData[key]}</li>`;
        }
        formattedInputs += "</ul>";

        listItem.innerHTML = `
            <div class="history-item">
                <strong>Prediction:</strong> <span class="highlight">${prediction} units</span>
                <br>
                <strong>Inputs:</strong> ${formattedInputs}
            </div>
        `;
        historyList.prepend(listItem);
    }

    // 🚀 Clear History Button
    document.getElementById("clearHistory").addEventListener("click", function() {
        document.getElementById("history").innerHTML = "";
    });
});
