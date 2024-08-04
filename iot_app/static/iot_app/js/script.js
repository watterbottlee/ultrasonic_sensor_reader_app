// Get references to the meter elements
const meter = document.getElementById('meter');
const needle = document.getElementById('needle');
const meterValue = document.getElementById('meterValue');

// Update meter animation based on sensor data
function updateMeter(distance) {
    console.log(`Distance: ${distance} cm`);
    meterValue.innerHTML = `${distance} cm`;

    // Calculate the rotation angle for the needle
    const maxDistance = 100; // Adjust this value based on your sensor's max range
    const angle = (distance / maxDistance) * 180; // Map distance to angle (0 to 180 degrees)
    needle.style.transform = `translateX(-50%) rotate(${angle}deg)`;
}

// Function to retrieve the latest sensor data
function getSensorData() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/latest-distance/', true);  // Updated URL to fetch latest distance
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            var sensorData = response.distance;  // Get distance from response
            updateMeter(sensorData);
        } else {
            console.error('Error fetching sensor data:', xhr.statusText);
        }
    };
    xhr.send();
}

// Call the function to retrieve the sensor data every 500ms
setInterval(getSensorData, 500);