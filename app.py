from flask import Flask, request, jsonify
import pandas as pd
from services import extract_text_from_pdf, parse_invoice_ai
import os

app = Flask(__name__)

EXCEL_FILE_PATH = os.path.abspath("invoices_archive.xlsx")

def save_to_excel(data, file_path):
    """
    Тази функция взема JSON данните от AI, превръща ги в ред
    и ги дописва най-отдолу в Excel файла.
    """
    if not isinstance(data, dict):
        return
    
    new_row = pd.DataFrame([data])

    if os.path.exists(file_path):
        try:
            old_df = pd.read_excel(file_path)
            updated_df = pd.concat([old_df, new_row], ignore_index=True)
            updated_df.to_excel(file_path, index=False)
        except Exception:
            new_row.to_excel(file_path.replace(".xlsx", "_new.xlsx"), index=False)

    else:
        new_row.to_excel(file_path, index=False)

@app.route("/upload", methods = ["POST"])
def process_invoice():
    if "file" not in request.files:
        return jsonify({"error": "Please attach a file!"}), 400
    
    file = request.files["file"]

    raw_text = extract_text_from_pdf(file.stream)

    ai_response = parse_invoice_ai(raw_text)

    if isinstance(ai_response, dict) and "error" not in ai_response:
        save_to_excel(ai_response, EXCEL_FILE_PATH)
        ai_response["excel_export_status"] = "Successfully saved!"
        ai_response["excel_file_location"] = EXCEL_FILE_PATH


    return jsonify(ai_response), 200

if __name__ == "__main__":
    app.run(port=8000, debug=True)


  