document.addEventListener("DOMContentLoaded", function () {
    // Execute code after the DOM is fully loaded

    // Example: Fetch latest fuel logs from an API endpoint
    function fetchLatestFuelLogs() {
        // Replace 'your-api-endpoint' with the actual API endpoint
        const apiUrl = '/api/latest_fuel_logs/';

        // Fetch data from the API endpoint
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                // Process the fetched data
                displayFuelLogs(data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }

    // Example: Display fuel logs in the HTML
    function displayFuelLogs(fuelLogs) {
        const fuelLogsContainer = document.getElementById('fuelLogsContainer');

        // Clear previous content
        fuelLogsContainer.innerHTML = '';

        // Iterate through fuel logs and create HTML elements
        fuelLogs.forEach(log => {
            const logElement = document.createElement('div');
            logElement.innerHTML = `<p><strong>Date:</strong> ${log.date}, <strong>Equipment:</strong> ${log.equipment}, <strong>Fuel Units:</strong> ${log.fuel_units}</p>`;
            fuelLogsContainer.appendChild(logElement);
        });
    }

    // Call the fetchLatestFuelLogs function
    fetchLatestFuelLogs();
});
