import os
import json
from pypdf import PdfReader
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

def extract_text_from_pdf(file_stream):
    reader = PdfReader(file_stream)
    text = ""
    for page in reader.pages:
        text = text + (page.extract_text() or "")
    return text

def parse_invoice_ai(raw_text):
    HF_TOKEN = os.getenv("HF_TOKEN")
    client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct", token=HF_TOKEN)
    
    system_prompt = """
        You are an accountant and your task is to collect required information as below from the invoice.
        The desired format is json. Do not include any conversational text.
        If a value is missing, set it to null.
        {
          "vendor_name" : "string or null",
          "receiver_name": "string or null",
          "deal_description": "string or null",
          "invoice_number": "string or null",
          "invoice_date": "string or null",
          "tax_rate": "string or null",
          "tax_base": float or null,
          "vat_amount": float or null,
          "total_amount": float or null
        }
        """
    

    response = client.chat_completion(
        messages = [ 
            {"role" : "system", "content" : system_prompt},
            {"role" : "user", "content" : f"Invoice text:{raw_text}"}
        ],
        max_tokens = 300,
        temperature = 0.1
    )

    ai_text =  response.choices[0].message.content
    
    try:
        return json.loads(ai_text)
    except json.JSONDecodeError:
        return {"error": "AI response matches no valid JSON", "raw_response": ai_text}
