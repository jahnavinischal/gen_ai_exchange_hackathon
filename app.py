from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# ---------------------------
# Load API Key
# ---------------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ API key not found. Please set GEMINI_API_KEY in your .env file.")
else:
    genai.configure(api_key=api_key)

# ---------------------------
# Initialize text model
# ---------------------------
text_model = genai.GenerativeModel("gemini-1.5-flash")

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="AI Marketplace Assistant", page_icon="🛍️")
st.title("🛍️ AI Marketplace Assistant for Artisans")
st.write("Empowering artisans to showcase their craft with AI-powered storytelling & marketing.")

# User input
product_input = st.text_area(
    "✍️ Enter your product details:", 
    placeholder="Example: Handmade jute bag, eco-friendly, crafted by women artisans."
)

# Generate buttons
col1, col2, col3 = st.columns(3)
generate_story = col1.button("📖 Generate Story")
generate_caption = col2.button("📢 Generate Social Post")
generate_poster = col3.button("🎨 Generate Pitch")

# ---------------------------
# Feature 1: Product Story
# ---------------------------
if generate_story and product_input:
    prompt = f"Write a compelling product story and description for an online marketplace. Product: {product_input}"
    response = text_model.generate_content(prompt)
    st.subheader("📖 Product Story & Description")
    st.text_area("Copy this story:", value=response.text, height=150)

# ---------------------------
# Feature 2: Social Media Captions
# ---------------------------
if generate_caption and product_input:
    prompt = f"Create a short Instagram/Facebook caption with emojis and 5 trending hashtags for: {product_input}"
    response = text_model.generate_content(prompt)
    st.subheader("📢 Social Media Caption & Hashtags")
    st.text_area("Copy this caption:", value=response.text, height=100)

# ---------------------------
# Feature 3: Marketing Pitch
# ---------------------------
if generate_poster and product_input:
    st.subheader("💌 Marketing Pitch / Product Email")

    # Prompt to generate a marketing pitch
    prompt = f"Write a short, engaging marketing pitch or email to promote this product: {product_input}. Keep it persuasive and suitable for online shoppers."

    # Generate pitch using Gemini
    response = text_model.generate_content(prompt)
    marketing_pitch = response.text

    # Display the pitch
    st.write(marketing_pitch)