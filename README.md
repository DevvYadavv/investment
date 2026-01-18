# 📊 Investment AI Assistant

An **educational GenAI application** that helps users:

* Learn investing concepts (Investment Coach / Teacher Persona)
* Understand daily market movements (Market Commentary / News Persona)

⚠️ **Important:** This application is strictly for **educational purposes only**. It does **NOT** provide financial advice, stock tips, or investment recommendations.

---

## ✨ Features

### 1️⃣ Investment Coach Mode (Teacher Persona)

* Explains investing concepts such as:

  * SIP (Systematic Investment Plan)
  * Stocks, ETFs, diversification, risk
* Uses beginner-friendly explanations and analogies
* **Strictly refuses**:

  * Buy/sell/hold advice
  * Stock recommendations
  * Intraday or guaranteed-return requests
* Redirects users to *how investors evaluate investments* instead of giving tips

---

### 2️⃣ Market Commentary Mode (News Persona)

* Explains:

  * Why markets are up or down
  * Macro and sector-level movements
* Uses **neutral, news-style summaries**
* No predictions or recommendations
* Market context is grounded using recent (mock) news data

---

## 🛡️ Safety & Guardrails

The app includes explicit safety controls:

* Advice-detection logic to identify prohibited requests
* Polite refusals with redirection to educational content
* Mandatory disclaimer shown with responses

This directly satisfies the **Safety & Compliance** requirements of the assignment.

---

## 🧠 Technology Stack

* **Frontend / UI:** Streamlit
* **LLM:** Groq (LLaMA 3.3 70B)
* **Backend Logic:** Python


---

## 📁 Project Structure

```
├── investment.py # Main Streamlit application
├── README.md     # Project documentation
```

---

## 🚀 Setup Instructions

### 2️⃣ Install dependencies

```bash
pip install streamlit groq
```

### 3️⃣ Set environment variable

**Linux / macOS**

```bash
export GROQ_API_KEY="your_groq_api_key"
```

**Windows (PowerShell)**

```powershell
setx GROQ_API_KEY "your_groq_api_key"
```

### 4️⃣ Run the application

```bash
streamlit run app.py
```

---

## 🎯 Evaluation Criteria Mapping

| Requirement         | How it is satisfied              |
| ------------------- | -------------------------------- |
| Safety & Guardrails | Advice refusal + disclaimers     |
| Conversation Flow   | Separate Teacher & News personas |
| Code Quality        | Modular, readable Python code    |
| Prototype           | Streamlit-based web chat UI      |

---

## 📌 Notes for Reviewers

* This app intentionally avoids personalized investment advice
* RAG is limited to news grounding to prevent advice leakage
* Architecture is LLM-ready and can be extended with:

  * Real-time news APIs
  * Vector databases
  * Advanced guardrails (LangChain / LangGraph)

---

## 👤 Author

**Dev Yadav**

---

## 📄 Disclaimer

This project is created **only for educational and demonstration purposes**. It should not be used to make real investment decisions.
