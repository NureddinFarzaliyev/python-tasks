import PyPDF2
import json
import re

def extract_questions_from_pdf(pdf_path, output_json_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        all_text = ""
        
        for page in pdf_reader.pages:
            all_text += page.extract_text()
    
    question_pattern = r"\d+\.\s.*?(?=\n\d+\.|\Z)"
    questions = re.findall(question_pattern, all_text, re.DOTALL)
    
    questions_data = []
    for question in questions:
        question_lines = question.split("\n")
        question_text = question_lines[0].strip()
        choices = [line.strip() for line in question_lines[1:] if line.strip()]
        questions_data.append({
            "question": question_text,
            "choices": choices
        })
    
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(questions_data, json_file, ensure_ascii=False, indent=4)

    print(f"Questions successfully extracted to {output_json_path}")

pdf_path = "./exam.pdf"  
output_json_path = "output_questions.json"
extract_questions_from_pdf(pdf_path, output_json_path)
