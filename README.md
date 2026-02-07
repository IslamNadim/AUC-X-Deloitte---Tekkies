# AUC-X-Deloitte---Tekkies
This is the official AUC X Deloitte Hackathon Repository of Tekkies team. 

# FlavorCraft AI  
### AI-Powered Menu Engineering & Pricing Intelligence Platform

---

## 1. Project Overview

FlavorCraft AI is an end-to-end **AI decision support system** that transforms raw restaurant sales data into **actionable pricing, promotion, and menu optimization recommendations**.

The platform combines:

- Machine Learning clustering  
- Business analytics  
- Large Language Model (LLM) reasoning  
- Interactive dashboard visualization  

to help restaurant managers move from **intuition-based decisions** to **data-driven strategy**.

---

## 2. Problem Statement

FlavorCraft restaurants collect extensive historical operational data:

- Orders and quantities  
- Item prices and costs  
- Customer purchasing behavior  

However, this data is **not effectively used** to support:

- Pricing optimization  
- Menu engineering  
- Profitability analysis  
- Strategic decision-making  

This leads to:

- Hidden loss-making items  
- Missed revenue opportunities  
- Inefficient promotions  

### 🎯 Goal

Build an **AI assistant** that converts historical restaurant data into:

- Clear business insights  
- Actionable recommendations  
- Natural-language strategic guidance  

---

## 3. Key Features

### 📊 Interactive Analytics Dashboard
Built using **Streamlit**, the dashboard provides:

- Revenue, profit, and margin KPIs  
- Sales volume visualization  
- Price sensitivity analysis  
- Real-time filtering of menu items  

---

### 🤖 Machine Learning Menu Engineering

Using **K-Means clustering**, menu items are automatically classified into:

- ⭐ Stars → High demand, high profit  
- 🐎 Plowhorses → High demand, low margin  
- 🧩 Puzzles → Low demand, high margin  
- 🐶 Dogs → Low demand, low profit  

This enables **data-driven menu optimization**.

---

### 🧠 AI Business Assistant (LLM-Powered)

A conversational AI assistant allows managers to ask:

- *Which items should we remove?*  
- *What should we promote?*  
- *How can we increase profit?*  

The assistant analyzes:
Database → ML Clusters → Business Context → LLM Reasoning

and returns **consulting-style recommendations in natural language**.

---

### 🔗 REST API Backend

Built with **Flask**, providing:

- Secure API key authentication  
- Menu analytics endpoints  
- ML clustering services  
- AI insight generation  

---

## 4. System Architecture

Streamlit Dashboard (UI)
↓
Flask REST API (Backend)
↓
PostgreSQL Database
↓
Machine Learning Clustering
↓
LLM Business Intelligence
↓
Actionable Recommendations

This modular architecture ensures:

- Scalability  
- Maintainability  
- Clear separation of concerns  

---

## 5. Technologies Used

### Backend
- Python  
- Flask  
- PostgreSQL  
- Pandas & NumPy  

### Machine Learning
- Scikit-learn (K-Means clustering)

### AI / LLM
- OpenAI GPT-4o-mini  

### Frontend
- Streamlit  

### Dev & Collaboration
- GitHub  
- Virtual Environments  

---

## 6. Installation

### Clone Repository

## Quick Start (Full Setup & Run)

Follow these steps to install and run the full FlavorCraft AI system locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/flavorcraft-ai.git
cd flavorcraft-ai
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Environment Variable (OpenAI Key)

```bash
export OPENAI_API_KEY="your_api_key_here"
```

---

### 5️⃣ Run Backend (Flask API)

```bash
python src/main.py
```

Backend will run on:

```
http://127.0.0.1:5001
```

---

### 6️⃣ Run Frontend Dashboard (Streamlit)

Open a **new terminal**, activate the environment again:

```bash
source .venv/bin/activate
streamlit run src/dashboard/Flavor.py
```

Then open in your browser:

```
http://localhost:8502
```

---

### 7️⃣ Use the AI Assistant

Scroll to **“Ask FlavorCraft AI”** in the dashboard and try:

```
Which items are dogs?
What should we promote?
How can we increase profit?
```

The assistant will analyze:

```
Database → ML Clustering → Business Context → LLM Reasoning
```

and return **data-driven strategic recommendations**.

---

### 8️⃣ Stop the System

Press:

```
CTRL + C
```

in each running terminal.

---

## Example End-to-End Flow

```
User Question → Streamlit UI → Flask API → PostgreSQL Data
→ ML Clustering → OpenAI LLM → Business Recommendation → UI Display
```

This demonstrates a **complete AI decision-support pipeline**.


10. Team Members & Responsibilities
🧠 Islam Nadim — AI & System Architecture Lead

Designed overall system architecture

Implemented ML clustering pipeline

Integrated LLM-based AI assistant

Led technical decision-making

⚙️ Hana Emad — Backend & Database Engineer

Built Flask REST API

Designed PostgreSQL schema & queries

Implemented secure API endpoints

Connected ML services to backend

📊 Ahmed Taia — Data Analytics & ML Support

Prepared data processing pipelines

Assisted in clustering logic & validation

Contributed to performance metrics & insights

🎨 Haya Hesham — UI/UX & Dashboard Design

Designed Streamlit dashboard layout

Implemented visual analytics & charts

Ensured usability and clarity of insights

📈 Haya Zaher — Business Analysis & Insights

Defined business problem & use cases

Interpreted ML results into strategy

Helped craft AI recommendation logic

📝 Zeina Karim — Documentation & Presentation Lead

Wrote project documentation & README

Prepared architecture explanations

Led final presentation & storytelling



