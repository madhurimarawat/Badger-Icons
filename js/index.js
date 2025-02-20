/*
*********************************************************************************************
* File: index.js
* Author: Madhurima Rawat
* Date: February 20, 2025
* Description: JavaScript functionality for the Badger-Icons platform, dynamically loading 
*              categories, subcategories, and images from a JSON file. The script formats 
*              category names, generates image cards, and provides an "Embed Code" feature 
*              for easy integration.
* Version: 1.0
* GitHub Repository: https://github.com/madhurimarawat/Badger-Icons
* Issues/Bugs: For any script-related issues, visit the GitHub repository's 
*              [Issues](https://github.com/madhurimarawat/Badger-Icons/issues) section.
* Comments: This script efficiently loads and structures data, ensuring a responsive and 
*           user-friendly experience.
* Dependencies:
    - **Bootstrap 4.5.2**: Provides a responsive layout and prebuilt UI components.
    - **Font Awesome 6.0.0-beta3**: Used for icons.
    - **JSON Data File (directory-structure.json)**: Contains directory and image information.
* Functionality:
    - **Dynamic Content Loading**: Fetches and parses JSON to populate categories, 
      subcategories, and images dynamically.
    - **Image Cards**: Generates structured cards for each image, displaying descriptions 
      and embed options.
    - **Clipboard Functionality**: Allows users to copy an HTML embed code for each image.
    - **Error Handling**: Includes checks for missing or invalid data and handles fetch 
      failures gracefully.
*********************************************************************************************
*/

document.addEventListener("DOMContentLoaded", function () {
    const imageContainer = document.querySelector(".container .row");

    // Function to clean category/subcategory names
    function formatName(name) {
        return name
            .replace(/[-_]/g, " ") // Remove underscores and hyphens
            .replace(/\b\w/g, char => char.toUpperCase()); // Capitalize first letter of each word
    }

    // Fetch the JSON data
    fetch("js/directory-structure.json")
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("✅ JSON Loaded Successfully:", data);

            if (!data.directories || Object.keys(data.directories).length === 0) {
                console.warn("⚠ No directories found in JSON.");
                return;
            }

            for (const category in data.directories) {
                if (category === "_description") continue; // Skip descriptions at category level

                const categoryData = data.directories[category];
                if (!categoryData || typeof categoryData !== "object") continue;

                // ✅ Create a div container for category
                const categoryContainer = document.createElement("div");
                categoryContainer.classList.add("category-section", "col-12");

                // ✅ Create H2 for Category
                const categoryTitle = document.createElement("h2");
                categoryTitle.textContent = formatName(category);
                categoryTitle.classList.add("category-heading");
                categoryContainer.appendChild(categoryTitle);

                // Append category container
                imageContainer.appendChild(categoryContainer);

                for (const subcategory in categoryData) {
                    if (subcategory === "_description") continue; // Skip category descriptions

                    const subcategoryData = categoryData[subcategory];
                    if (!subcategoryData || typeof subcategoryData !== "object") continue;

                    // Fetch subcategory description
                    const subcategoryDesc = subcategoryData["_description"] || "";

                    // ✅ Create a div container for subcategory
                    const subcategoryContainer = document.createElement("div");
                    subcategoryContainer.classList.add("subcategory-section", "col-12");

                    // ✅ Create H3 for Subcategory
                    const subcategoryTitle = document.createElement("h3");
                    subcategoryTitle.textContent = formatName(subcategory);
                    subcategoryTitle.classList.add("subcategory-heading");
                    subcategoryContainer.appendChild(subcategoryTitle);

                    // ✅ Add description below subcategory title
                    if (subcategoryDesc) {
                        const subcategoryDescElement = document.createElement("p");
                        subcategoryDescElement.textContent = subcategoryDesc;
                        subcategoryDescElement.classList.add("subcategory-description");
                        subcategoryContainer.appendChild(subcategoryDescElement);
                    }

                    // Append subcategory container
                    imageContainer.appendChild(subcategoryContainer);

                    // ✅ Process Image Files
                    if (subcategoryData.files && Array.isArray(subcategoryData.files)) {
                        subcategoryData.files.forEach((fileDescription, index) => {
                            if (!fileDescription) return;

                            // Extract filename and description
                            const [imagePath, imageDesc] = fileDescription.split(" (");
                            const cleanedImageDesc = imageDesc ? imageDesc.replace(")", "") : "";

                            // Create a card div
                            const card = document.createElement("div");
                            card.classList.add("col-md-4", "mb-3", "px-1");

                            const buttonClass = index % 2 === 0 ? "button-mint" : "button-coral";

                            // ✅ Corrected Image Path
                            const imageSrc = `assets/${category}/${subcategory}/${imagePath}`;
                            console.log(`🔹 Image Path: ${imageSrc}`);

                            card.innerHTML = `
    <div class="card text-center">
        <a href="https://github.com/madhurimarawat/Badger-Icons" target="_blank">
            <img src="${imageSrc}" title="${cleanedImageDesc}" alt="${imagePath}" width="50" height="50">
        </a>
        <div class="card-body">
            <p class="image-description">${cleanedImageDesc}</p>
            <button class="${buttonClass}" onclick="copyEmbedCode('${imageSrc}', '${cleanedImageDesc}', '${imagePath}')">Copy Embed Code</button>
        </div>
    </div>
`;

                            // Append each card
                            imageContainer.appendChild(card);
                        });
                    }

                    // ✅ Append Separator Below Each Subcategory
                    const separator = document.createElement("hr");
                    imageContainer.appendChild(separator);
                }
            }
        })
        .catch(error => console.error("❌ Error loading JSON:", error));
});

// ✅ Function to Copy Image Link
function copyEmbedCode(imageSrc, title, alt) {
    const embedCode = `<a href="https://github.com/madhurimarawat/Badger-Icons"><img src="${imageSrc}" title="${title}" alt="${alt}" width="50" height="50"></a>`;

    navigator.clipboard.writeText(embedCode)
        .then(() => alert("✅ Embed code copied!"))
        .catch(err => console.error("❌ Failed to copy:", err));
}
