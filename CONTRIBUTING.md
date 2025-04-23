# 🎨🚀 Contributing Guidelines for Badger-Icons  

Thank you for contributing to the **Badger-Icons** project! Your support helps expand and enhance this collection of beautifully styled icons and logos. 💖  

## 📝 Table of Contents  

1. [📌 How You Can Contribute](#-how-you-can-contribute)  
   - [1️⃣ Share This Project](#share-this-project)  
   - [2️⃣ Suggest New Categories or Designs](#-suggest-new-categories-or-designs)  
   - [3️⃣ Add New Icons or Logos](#3-add-new-icons-or-logos)  
   - [4️⃣ Update the Website](#4-update-the-website)  
   - [5️⃣ Show Off Your Usage](#5-show-off-your-usage)  
   - [6️⃣ Become a Contributor](#6-become-a-contributor)  
   - [7️⃣ Modifying `index.html`](#7-modifying-indexhtml)  

2. [📢 Issues & Discussions](#-issues--discussions)  

3. [✨ Try Your Own Icon Styling!](#-try-your-own-icon-styling)

---

## 📌 How You Can Contribute  

<a name="share-this-project"></a>

### 1️⃣ Share This Project  
Spread the word! Share this project on social media, with friends, or in your developer community. More visibility means more contributors and better icons! 💡  

### 2️⃣ Suggest New Categories or Designs  
Got ideas for new categories? Open an [issue](https://github.com/madhurimarawat/Badger-Icons/issues) and share your thoughts!  

### 3️⃣ Add New Icons or Logos  
Follow these steps to contribute new icons:  

### ➕ **Adding Icons for a New Category**  

1. **Create a folder** inside `assets/` for the new category (e.g., `assets/new_category/`).  
2. **Ensure Each Icon Has Two Versions**:  
   - A **transparent** version (without background).  
   - A **plain** version (with a solid background).  
3. **Save the Icons & Logos in PNG Format**:  
   - Name files properly (e.g., `concept-icon-1.png`, `concept-icon-1-transparent.png`).  
4. **Update the JSON File**:  
   - Each category should have a JSON file inside its folder (e.g., `assets/new_category/icons.json`).  
   - The JSON file should include:  
     ```json
     {
       "name": "Example Icon",
       "category": "new_category",
       "icons": [
         {
           "type": "transparent",
           "file": "concept-icon-1-transparent.png",
           "description": "A transparent version of Example Icon."
         },
         {
           "type": "plain",
           "file": "concept-icon-1.png",
           "description": "A plain version of Example Icon with background."
         }
       ]
     }
     ```  
5. **Update the README File**:  
   - Add a new row in the respective section (`Job Roles`, `Programming Languages`, etc.).  
6. **Submit a Pull Request (PR)**:  
   - Ensure all icons, JSON files, and the `README.md` file are updated.  
   - Provide a short description of the changes made in the PR.  

---

### 🔄 **Updating an Existing Category**  

1. **Place new icons in the correct folder**  
2. **Follow Naming Convention**  
   - If an icon already exists, name the new one sequentially:  
     - `concept-icon-2.png`, `concept-icon-2-transparent.png`  
3. **Update the JSON File**  
4. **Update the README Table**  
5. **Submit a Pull Request (PR)**  

### 4️⃣ Update the Website  
If adding a new category, edit **index.html** and update the description. Also, update the README file.  

### 5️⃣ Show Off Your Usage  
Have you used **Badger-Icons** in your project? Add your showcase to `README.md`!  
[Submit your usage](https://github.com/madhurimarawat/Badger-Icons/issues).  

### 6️⃣ Become a Contributor  
If you contribute icons, logos, or suggestions, we’ll add your name to the **Contributors** section!  

### 7️⃣ Modifying `index.html`  
If you are editing `index.html`, **update these sections**:  

- **File Header:**  
  ```html
  <!--
  *********************************************************************************************
  * File: index.html
  * Author: Madhurima Rawat
  * Date: February 21, 2025
  * Description: Main HTML page for the Badger-Icons platform, providing a collection of
  *              professionally styled icons and logos for job roles, programming languages,
  *              and subjects. The site features a carousel for featured icons, a navigation
  *              bar, and an interactive layout for ease of access and contribution.
  * Version: 1.0
  -->
  ```  
  📌 **Update the Date** to match the latest modification.  

- **Meta Tags:**  
  ```html
  <!-- Specifies the publication date and time in ISO 8601 format. -->
  <meta name="date" content="2025-02-21T12:00:00Z" />

  <!-- Last Updated -->
  <meta name="last-modified" content="2025-02-21T12:30:45Z">
  ```  
  📌 **Update `last-modified` date whenever making changes.**  

---

## 📢 Issues & Discussions  
If you have any questions or run into issues, feel free to start a [discussion](https://github.com/madhurimarawat/Badger-Icons/discussions) or open an [issue](https://github.com/madhurimarawat/Badger-Icons/issues).  

---

## ✨ **Try Your Own Icon Styling!**  

We’ve included a sample GitHub logo styled using HTML and SVG! 🎨  
Want to try it with your **favorite icon**?  

🛠️ Visit the following example files to learn more:
- [`Github-Icon-Styled.html`](Github-Icon-Styled.html)  
- [`SVG Description and Links.html`](SVG%20Description%20and%20Links.html)  

💬 These files include **comments in the code** to help you understand how it works. 

Feel free to create your **own version** using any icon you love, and contribute it back to the project! 😄  

Happy contributing! 🎨🚀
