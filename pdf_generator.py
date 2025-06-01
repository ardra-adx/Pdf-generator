import pandas as pd
from fpdf import FPDF
import os

def read_data(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.json':
        return pd.read_json(file_path)
    elif ext == '.csv':
        return pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file type. Use JSON or CSV.")

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Personalized Report", ln=True, align="C")
        self.ln(10)

    def add_user_data(self, user_data):
        self.set_font("Arial", size=12)
        fields = ['name', 'age', 'email', 'address']
        for field in fields:
            value = user_data.get(field, 'N/A') 
            self.cell(0, 10, f"{field}: {value}", ln=True)
        self.ln(10)

def generate_reports(data, output_folder='reports'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for index, row in data.iterrows():
        pdf = PDFReport()
        pdf.add_page()
        user_data = row.to_dict()
        pdf.add_user_data(user_data)

        filename = user_data.get('name', f'user_{index}')
        safe_filename = "".join(c for c in filename if c.isalnum() or c in (' ', '_')).rstrip()
        pdf.output(os.path.join(output_folder, f"{safe_filename}_report.pdf"))

    print(f"Reports generated in folder: {output_folder}")

if __name__ == "__main__":
    file_path = input("Enter path to JSON or CSV file with user data: ").strip()
    data = read_data(file_path)
    generate_reports(data)
