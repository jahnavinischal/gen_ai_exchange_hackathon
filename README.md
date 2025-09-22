# 🛍️ AI Marketplace Assistant for Artisans  

An AI-powered platform that empowers local artisans to showcase and market their handmade products more effectively. Built with **Streamlit** and **Google Gemini LLM**, the assistant generates **product stories**, **social media captions** and **business pitches** to help artisans reach wider digital audiences without needing professional marketing expertise.  

The app is deployed at this site:
[Link to webapp](https://genaiexchangehackathon-bjxazhemrsgreqwwkrbok8.streamlit.app/)
Below is a screenshot of the interface.
<img width="1888" height="963" alt="image" src="https://github.com/user-attachments/assets/95f39485-c406-47bd-8651-f3b4eaa0c8f6" />

---

## 🚀 Features  
- 📖 **Product Story Generator** – Converts product details into compelling marketplace-ready descriptions.  
- 📢 **Social Media Post Generator** – Creates engaging captions with emojis and trending hashtags.  
- 🎤 **Pitch Generator** – Helps artisans craft short pitches for business growth and collaborations.  

---

## 🏗️ Tech Stack  
- **Frontend/UI**: Streamlit  
- **Backend**: Python  
- **LLM API**: Google Gemini   
- **Libraries**: `streamlit`, `google-generativeai`, `python-dotenv`, `Pillow`  

---

## 📂 Project Structure  

```bash
gen_ai_exchange_hackathon/
│── app.py              # Main Streamlit app
│── requirements.txt    # Dependencies
│── .env                # API key (local only, not in repo)
│── README.md           # Documentation
```

---

## 🔑 Setup & Installation  

1. **Clone the repo**  
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

2. **(Optional) Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

Add API key
Create a .env file in the project root:
```bash
GEMINI_API_KEY=your_api_key_here
```

4. **Run the App**
```bash
streamlit run app.py
```



## 📊 Future Scope

- AI-Poster generation using image APIs 

- Pricing recommendations

- Multilingual support

- Artisan profile management with login
