import google.generativeai as genai

genai.configure(api_key="AIzaSyDHqazJFH824cwgnsfab4nkax8w1J0A8A8")  # Use your own key

def analyze_with_llm(text):
    prompt = f"""
    Website Text: {text}

    1. What does this company do?
    2. Who are their target customers?
    3. Suggest one AI automation solution QF Innovate could pitch to them.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    return {
        "summary": response.text,
        "pitch": "Refer to the summary above"
    }
