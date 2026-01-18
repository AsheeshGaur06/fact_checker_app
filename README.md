## Output

![Output](./Output/Ai%20Fact%20Checker.png)


# 🧠 AI Fact-Checking Web App

This project is an AI-powered Fact-Checking Web Application. It helps users verify facts and numbers inside a PDF file before publishing or sharing them.

The app checks whether the claims in the PDF are:

- ✅ **Verified** – correct  
- ⚠️ **Inaccurate** – wrong or outdated  
- ❌ **False** – no reliable evidence found  

---

## 🚀 Live Demo

**Deployed App Link:**  
👉 ![deployed link](https://your-app-name.streamlit.app)  


---

## 🎯 What This App Does

1. User uploads a PDF file  
2. The app extracts factual claims like numbers, dates, statistics, and technical specifications  
3. Each claim is checked using live web search  
4. AI verifies each claim and shows:  
   - Status (Verified / Inaccurate / False)  
   - Correct value (if available)  
   - Short explanation  
   - Source link  

This helps catch wrong data, outdated statistics, and false information before publishing.

---

## 🖥️ User Interface

- Simple drag-and-drop PDF upload  
- Clear list of extracted claims  
- Easy-to-read fact-check results  

**Screenshots in this repository show:**  
- PDF upload page  
- Fact-checking results page  

---

## 🛠️ Tech Stack Used

- **Frontend & UI:** Streamlit  
- **Backend:** Python  
- **AI Model:** OpenAI (via OpenRouter)  
- **LLM Framework:** LangChain  
- **Web Search:** Tavily API  
- **PDF Processing:** pdfplumber  
- **Deployment:** Streamlit Cloud  

---

## 📄 How the App Works (Simple Explanation)

1. User uploads a PDF  
2. App reads text from the PDF  
3. AI finds important claims like:  
   - GDP numbers  
   - Population data  
   - Dates  
   - Technical specifications  
4. Each claim is searched on the live web  
5. AI compares the claim with real data  
6. Result is shown with correct values, status, explanations, and sources  

**Claim Status Meaning:**  

| Status      | Meaning                                 |
|------------|-----------------------------------------|
| Verified    | Claim is correct                        |
| Inaccurate  | Claim is outdated or partially wrong    |
| False       | No trusted evidence found                |

---

## ⚙️ How to Run Locally

1. **Clone the Repository**  
```bash
git clone https://github.com/your-username/fact_checker_app.git
cd fact_checker_app
```

2. **Create Virtual Environment**
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate   # Mac/Linux
```

3. **Install Dependencies**

```bash

pip install -r requirements.txt

```


4. **Add Environment Variables**
```bash
Create a .env file with:

OPENROUTER_API_KEY=your_api_key_here
TAVILY_API_KEY=your_api_key_here

```


5. **Run the App**

```bash
streamlit run app.py

```