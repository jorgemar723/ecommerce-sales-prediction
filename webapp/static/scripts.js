document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("predictionForm");
    const predictionOutput = document.getElementById("predictionOutput");
    const historyList = document.getElementById("history");
    const toggleBtn = document.getElementById("darkModeToggle");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        fetch("/predict", {
            method: "POST",
            body: new URLSearchParams(formData),
        })
        .then((response) => response.json())
        .then((result) => {
            if (result.prediction !== undefined) {
                const rounded = parseFloat(result.prediction).toFixed(2);
                predictionOutput.textContent = `Predicted Units Sold: ${rounded}`;

                const historyItem = document.createElement("li");
                historyItem.className = "history-entry";

                const now = new Date().toLocaleString();
                const formattedInputs = Object.entries(data)
                    .map(([key, value]) => `${key}: ${value}`)
                    .join("<br>");

                historyItem.innerHTML = `
                    <div class="history-header">
                        <strong>Prediction:</strong> ${rounded} units
                        <small style="float:right">${now}</small>
                    </div>
                    <em>Inputs:</em><br>
                    ${formattedInputs}
                `;
                historyList.prepend(historyItem);
            } else {
                predictionOutput.textContent = "Prediction failed.";
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            predictionOutput.textContent = "Error occurred.";
        });
    });

    toggleBtn.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");

        const isDark = document.body.classList.contains("dark-mode");
        toggleBtn.textContent = isDark ? "🌞 Toggle Light Mode" : "🌙 Toggle Dark Mode";
    });
});

function clearHistory() {
    const historyList = document.getElementById("history");
    historyList.innerHTML = "";
}
