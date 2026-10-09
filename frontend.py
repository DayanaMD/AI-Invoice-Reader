import gradio as gr
import requests

FLASK_URL = "http://127.0.0.1:8000/upload"

def send_file_to_flask(file_path):
    if file_path is None:
        return{"error" : "Please attach a file!"}
    try:
        with open(file_path, "rb") as f:
            response = requests.post(FLASK_URL, files={"file" : f})
            return response.json()
    except Exception as e:
        return{"error" : f"Connection is lost:{str(e)}"}
    
demo = gr.Interface(
    fn = send_file_to_flask,
    inputs = gr.File(label = "Please attach a pdf invoice", file_types = [".pdf"], type = "filepath"),
    outputs = gr.JSON(label = "Please find the extracted data"),
    title = "Accounting AI assistant",
    description = "Simple interface for invoice data extraction with AI ",
    theme = gr.themes.Soft()
    )
if __name__ == "__main__":
        demo.launch(share=True)


