# Pdf-generator

This script reads user data from a **CSV or JSON** file and generates **personalized PDF reports** for each user. It's perfect for automating report creation using structured data.

Features

- Supports both `.csv` and `.json` input files
- Creates clean, personalized reports for each user
- Saves all reports to a dedicated `reports/` folder

Flow:

1. Install Required Libraries
   pip install pandas fpdf
2. Prepare input file:- Create a .csv or .json file with the following columns
   name
   age
   email
   address
3. Run the script
   python pdf_generate.py
   #You will be prompted to enter the path to your CSV or JSON file:
   - Enter the full path of your csv or json file.
4. All generated PDF files will be saved in a folder called reports

























![Screenshot from 2025-05-30 00-01-09](https://github.com/user-attachments/assets/a85dd7d9-8279-41c9-bac5-4c9a5574ccef)
![Screenshot from 2025-05-30 00-00-48](https://github.com/user-attachments/assets/6c6d24c9-a371-41af-bf94-fa29b9cf3a82)
