import os
import google.generativeai as genai
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# --- Configuration ---
# Create a .env file in the same directory and add your API key:
# GOOGLE_API_KEY="YOUR_API_KEY_HERE"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = FastAPI()

# --- Pydantic Models for Data Validation ---
# This defines what data we expect from the user's form
class WebsiteRequest(BaseModel):
    business_name: str
    product_name: str
    goal: str # e.g., "Sell a Product"
    feeling: str # e.g., "Trust & Security"

# --- API Endpoint ---
@app.post("/generate-website/")
async def generate_website(request: WebsiteRequest):
    """
    Receives user input and uses an AI to generate a website.
    """
    print("Received Request:", request.dict())

    # This is the "Master Prompt" we discussed
    prompt = f"""
    You are CogniSite, an expert AI web developer specializing in cognitive science and neuro-marketing. 
    Your task is to generate a single, complete HTML file with inline CSS for a landing page.

    Based on the following user input:
    - Business Name: "{request.business_name}"
    - Product: "{request.product_name}"
    - Goal: "{request.goal}"
    - Desired Feeling: "{request.feeling}"

    Follow these cognitive rules STRICTLY:

    1. If the Goal is 'Sell a Product': Structure the page to minimize cognitive load. Use a clear Z-pattern layout. Include ONLY these sections: a compelling headline, a section with 3 key benefits (not features), a large product image, and ONE SINGLE, high-contrast Call-to-Action button. This applies Hick's Law.
    2. If the Goal is 'Capture Email Signups': The page must be extremely simple. A powerful headline, a short sentence explaining the benefit of signing up, an email input field, and a button. Nothing else.
    3. Regarding the Desired Feeling:
        - If 'Trust & Security', use a blue/green color palette. The text should use words like "Guaranteed," "Secure," "Trusted," "Official."
        - If 'Excitement & Urgency', use a red/orange/yellow color palette for buttons. Use words like "Limited Time," "Instantly," "Unlock," and add a countdown timer element.

    Generate ONLY the HTML code and nothing else.
    """

    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        
        # We might need to clean up the response to remove backticks or "html" label
        clean_html = response.text.replace("```html", "").replace("```", "").strip()
        
        return {"html_content": clean_html}

    except Exception as e:
        print("An error occurred:", e)
        return {"error": "Failed to generate website from AI model."}