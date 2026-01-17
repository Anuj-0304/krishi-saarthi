🌱 Krishi Saarthi – Farmer Support Web Platform

Krishi Saarthi is a Streamlit-based web application designed to support Indian farmers by providing verified government scheme information, weather insights, 
crop disease awareness, and agricultural advisory tools in one unified platform.

The application focuses on simplicity, trust, and accessibility, ensuring that farmers can easily understand and use the information without technical complexity.

🎯 Objective
Small and marginal farmers often face multiple challenges, such as:
* Lack of awareness about government welfare schemes
* Fragmented and unreliable agricultural information
* Difficulty accessing timely advisory and decision-support tools

Krishi Saarthi addresses these challenges by acting as a digital “Saarthi” (guide) that centralizes reliable, verified, and farmer-friendly agricultural resources.

🚀 Key Features :

🌾 Government Schemes Dashboard

* Displays major central government agricultural schemes
* Each scheme is shown as an image-based visual card
* Clear explanation of benefits, eligibility, and purpose
* One-click access to official government websites

🧠 Session-Based Navigation
* Uses Streamlit session_state for page control
* Smooth navigation between:
    * Home page (scheme listing)
    * Scheme detail page
* Avoids unnecessary page reloads

🖱 Interactive Scheme Exploration
* Each scheme includes a “View” button
* Clicking opens a detailed information card
* Includes a Back button for easy navigation

🧾 Structured Scheme Detail View
* Clean card-based layout for scheme details
* Bullet-point format for easy reading
* Focused presentation to avoid information overload

🔗 Verified Official Sources
* Direct redirection to official government portals
* Ensures authenticity and prevents misinformation

🖼 Image-Based UI with Hover Effects
* Each scheme includes a representative image
* Hover zoom effects improve visual engagement
* Images rendered using Base64 encoding for reliability

🌦 Weather Prediction Integration
* External weather prediction application linked
* Helps farmers plan:
    * Sowing
    * Irrigation
    * Harvesting

🌱 Crop Disease Detection (AI Saarthi)
* Integration with an AI-based crop disease detection app
* Assists farmers in identifying crop health issues at early stages
* Helps reduce crop loss and improve yield quality

📊 Crop Care & Maintenance Advisory
* Dedicated advisory section
* Provides easy access to crop management guidance
* Supports better decision-making during crop cycles

💧 Water Requirement Calculator (Planned Feature)
* Calculates estimated water requirement for crops
* Based on:
    * Crop type
    * Area of cultivation
    * Growth stage

* Helps farmers:
    * Optimize irrigation
    * Reduce water wastage
    * Improve water-use efficiency
(This feature can be implemented using simple input forms and calculation logic in Streamlit.)

💰 Crop Cost & Profit Calculator (Planned Feature)
* Estimates total cultivation cost and expected profit
* Inputs may include:
    * Seed cost
    * Fertilizer cost
    * Labor cost
    * Irrigation cost
    * Expected yield
    * Market price
* Helps farmers:
    * Understand profitability before sowing
    * Plan investments wisely
    * Reduce financial risk
(This feature is ideal for implementation using Streamlit input widgets and basic arithmetic calculations.)

🎨 Farmer-Friendly Design
* Earthy color palette and high-contrast text
* Large fonts for better readability
* Simple layout designed for non-technical users
* Desktop-friendly responsive interface

🧠 How the App Works
1. User opens the application
2. Homepage displays government schemes as visual cards
3. Clicking a scheme opens a detailed information page
4. User can:
    * Read benefits and eligibility
    * Return to the scheme list
    * Visit the official government website
5. Additional sections allow navigation to:
    * Weather Prediction App
    * Crop Disease Detection App
    * Crop Care Advisory App
6. Future tools like Water Requirement Calculator and Crop Cost & Profit Calculator will provide decision support
7. All external services open in new browser tabs

🛠️ Tech Stack
Layer |	Technology
Frontend | Streamlit
Backend	| Python
UI Styling | HTML + CSS (via Streamlit Markdown)
Image Handling |	PIL
Data Handling |	Pandas, NumPy

📂 Project Structure
Krishi-Saarthi/
│
├── Saarthi_app.py        # Main Streamlit application
├── website_logo.jpg     # Website header logo
├── img1.jpg             # Scheme image
├── img2.jpg
├── img3.jpg
├── img4.jpg
├── img5.jpg
├── img6.jpg
├── img7.jpg
├── img8.jpg
├── img9.jpg
├── img10.jpg
└── README.md

🌾 Krishi Saarthi

A digital guide for farmers — simple, reliable, and practical.
