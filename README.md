# AI Invoice Reader

AI-powered invoice processing application that extracts key invoice information from PDF files and stores the results in Excel.

## Features

- Upload PDF invoices through a simple Gradio interface
- Extract text from PDF documents
- Use Meta Llama 3 via Hugging Face Inference API
- Parse invoice information into structured JSON
- Automatically save extracted data to Excel
- REST API built with Flask

## Extracted Fields

The application extracts:

- Vendor Name
- Receiver Name
- Deal Description
- Invoice Number
- Invoice Date
- Tax Rate
- Tax Base
- VAT Amount
- Total Amount

## Project Structure

```text
.
├── app.py
├── frontend.py
├── services.py
├── requirements.txt
├── .env
└── invoices_archive.xlsx
```

## Technologies Used

- Python
- Flask
- Gradio
- Pandas
- PyPDF
- Hugging Face Inference API
- Meta Llama 3

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Invoice-Reader.git
cd AI-Invoice-Reader
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
HF_TOKEN=your_huggingface_token
```

## Run the Application

Start Flask API:

```bash
python app.py
```

In a second terminal start Gradio:

```bash
python frontend.py
```

Open the Gradio interface in your browser and upload a PDF invoice.

## Example Workflow

1. Upload PDF invoice
2. PDF text is extracted
3. Llama 3 analyzes the content
4. Structured JSON is generated
5. Data is stored in Excel
6. Results are displayed in the UI

## Example Output

```json
{
  "vendor_name": "ABC Ltd",
  "receiver_name": "XYZ Ltd",
  "invoice_number": "INV-2025-001",
  "invoice_date": "2025-05-20",
  "tax_rate": "20%",
  "tax_base": 1000.00,
  "vat_amount": 200.00,
  "total_amount": 1200.00
}
```

## Future Improvements


- Multi-language invoice processing
- Database integration
- Batch processing
- Invoice validation



