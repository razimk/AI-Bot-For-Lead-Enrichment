# 🤖 AI Automation Bot for Lead Enrichment

This project is an AI-powered automation tool that enriches company leads by analyzing their website and generating strategic insights using Google’s Gemini LLM. It helps businesses like **QF Innovate** understand potential clients better by automating research and generating personalized AI-based solution pitches.

---

## 🚀 Features

- ✅ Upload a list of companies via CSV
- 🌐 Scrape company homepage content
- 🧠 Use Gemini LLM to:
  - Summarize what the company does
  - Identify their target customer
  - Suggest a relevant AI automation solution
- 📤 Download enriched results as CSV

---

## 📁 Folder Structure

aibot/
├── main.py # Main script for backend enrichment
├── app.py # Optional Streamlit web app
├── sample_input.csv # Sample input file
├── data/ # Output directory (auto-created)
└── helpers/
├── enrich.py # Logic to fill company metadata
├── scraper.py # Web scraper for homepage content
└── ai_analysis.py # Handles Gemini LLM interaction


---

## 📄 Sample Input Format

**sample_input.csv**
```csv
company_name
OpenAI
DeepMind
Zoho
Freshworks

Example Output Fields

| company\_name | website                                          | industry | summary\_from\_llm   | automation\_pitch\_from\_llm |
| ------------- | ------------------------------------------------ | -------- | -------------------- | ---------------------------- |
| OpenAI        | [https://www.openai.com](https://www.openai.com) | Software | "OpenAI develops..." | "QF Innovate could..."       |
