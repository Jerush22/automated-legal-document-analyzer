
from flask import Flask, render_template, request
import ollama

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        document = request.form.get("document", "").strip()

        if document:
            prompt = f"""
You are a legal document analysis assistant.
Analyze this document and extract:
1. Document Type
2. Parties Involved
3. Purpose
4. Key Obligations
5. Payment Terms
6. Duration and Important Dates
7. Termination Conditions
8. Important Clauses
9. Simple Summary

Use only information in the document.
If information is missing, say Not Specified.
This is an educational summary, not legal advice.

Document:
{document}
"""
            try:
                response = ollama.chat(
                    model="llama3.2:1b",
                    messages=[{"role": "user", "content": prompt}]
                )
                result = response["message"]["content"]
            except Exception as e:
                result = f"AI Error: {e}"
        else:
            result = "Please enter a document."

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
