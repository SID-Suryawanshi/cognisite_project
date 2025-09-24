CogniSite 🧠✨
CogniSite is an intelligent website builder that uses AI and principles of cognitive science to generate neuro-optimized landing pages for non-tech entrepreneurs.

This project was built for the Vortexa 2.0: Neuro Nexus Hackathon at D.Y. Patil Institute of Technology, Pune.

The Problem
Building a website is easy, but building an effective website is hard. Entrepreneurs often struggle with complex design choices, leading to websites that are cluttered, confusing, and fail to convert visitors into customers. The core issue is high cognitive load—overwhelming users with too much information and unclear calls-to-action, which causes them to leave the site.

Our Solution: Neuro-Optimized Web Design
CogniSite isn't just another website builder. It's an AI assistant trained on the principles of neuro-marketing and cognitive science.

Instead of asking about colors and fonts, we ask about goals and feelings. The user simply provides:

Their business goal (e.g., "Sell a Product").

The desired visitor feeling (e.g., "Trust & Security").

Our AI engine then generates a complete, single-page website that is specifically designed to be brain-friendly, reduce cognitive load, and guide the user's attention towards the primary goal.

Key Features
🧠 AI-Powered Generation: Leverages the Google Gemini API to create custom HTML & CSS from a simple prompt.

🎯 Goal-Oriented Layouts: Generates specific page structures based on the user's primary objective (e.g., sales, signups).

🎨 Emotion-Driven Styling: Uses color psychology and tone to craft a user experience that aligns with the desired feeling.

🖥️ Live Preview: Instantly see the generated website rendered in a live preview panel.

📱 Fully Responsive UI: The control panel is fully responsive and works seamlessly on both desktop and mobile devices.

💾 Save & Copy: Easily copy the generated code or save it as a complete .html file.

🌙 Dark Mode: A professional dark mode for a better user experience.

Tech Stack
Frontend: Plain HTML5, CSS3, and JavaScript (No frameworks for maximum stability).

Backend: Python with FastAPI.

AI Engine: Google Gemini API (gemini-1.5-flash).

🚀 Getting Started
Follow these instructions to get the project running on your local machine.

Prerequisites
You must have a stable version of Python installed correctly.

Python 3.12: Install it from the official python.org website.

CRITICAL: During installation, you MUST check the box that says "Add python.exe to PATH".

Installation & Setup
Clone the repository:

git clone [https://github.com/SID-Suryawanshi/cognisite_project.git](https://github.com/SID-Suryawanshi/cognisite_project.git)
cd cognisite_project

Create a Virtual Environment: Use the stable Python 3.12 to create a new venv.

py -3.12 -m venv venv

Activate the Environment:

.\venv\Scripts\activate

Install Dependencies: Install all the required Python libraries.

pip install -r requirements.txt

Create a .env file: Create a new file named .env in the root of the project. Add your Google AI API key to this file:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"

Running the Application
Start the Backend Server: Make sure your venv is active, then run:

uvicorn main:app --reload

The server will be running at http://127.0.0.1:8000.

Open the Frontend: Navigate to the project folder in your File Explorer and double-click the index.html file to open it in your browser.

Team
Siddhant Suryawanshi - GitHub Profile
Nilesh Rajpure
Mohammadsufiyan Samir Bagwan
Mehwish Aadam Shaikh
