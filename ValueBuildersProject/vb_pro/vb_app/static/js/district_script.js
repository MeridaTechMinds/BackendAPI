
        document.addEventListener("DOMContentLoaded", function() {
                
                // Get the state field element
                var stateField = document.getElementById("id_state"); // Replace "id_state" with the actual ID of your state field
                var districtField = document.getElementById("id_District"); // Replace "id_district" with the actual ID of your district dropdown
        
                // Add an event listener to the state field
                stateField.addEventListener("change", function () {
                    // Get the selected value from the state field
                    var selectedValue = stateField.value;
        
                    // Log the selected value to the console
                    console.log("Selected State:", selectedValue);
        
                    // Function to fetch districts based on the selected state from the API
                    function getDistricts(stateName) {
                        var api_url = "http://api.nightlights.io/districts";
        
                        // Fetch data from the API
                        return fetch(api_url)
                            .then(function (response) {
                                if (!response.ok) {
                                    throw new Error(`HTTP error! Status: ${response.status}`);
                                }
                                return response.json();
                            })
                            .then(function (data) {
                                // Extract districts for the specified state from the API response
                                var districts = [];
        
                                data.regions.forEach(function (region) {
                                    if (region.state_name === stateName) {
                                        var districtName = region.district_name;
                                        districts.push([districtName, districtName]);
                                    }
                                });
        
                                return districts;
                            });
                    }
        
                    // Example usage
                    getDistricts(selectedValue)
                        .then(function (districts) {
                            console.log("Districts:", districts);
        
                            // Clear existing options in the district dropdown
                            districtField.innerHTML = '';
        
                            // Populate the district dropdown with new options
                            districts.forEach(function (district) {
                                var option = document.createElement("option");
                                option.value = district[0];
                                option.text = district[1];
                                districtField.add(option);
                            });
                        })
                        .catch(function (error) {
                            console.error("Error fetching districts:", error);
                        });
                });
            });
        