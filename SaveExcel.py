import openpyxl
import os

def SaveExcel(log, month_name, year, store_name, employee_name, day):
    # Set up the folder structure
    logs_folder = f'LOG/{year}/{month_name}/{day}/{store_name}/{employee_name}'
    
    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)
    
    file_name = f"{store_name}_{employee_name}_{day}_{month_name}.xlsx"
    file_path = os.path.join(logs_folder, file_name)
    
    # Create a new Excel workbook and sheet
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Test Results"
    
    # Header row
    headers = ["Visitor Name", "Visitor Address", "Current Address", "Date of Birth", 
               "Telephone Number", "Email Address", "Test ID", "Test Name", "Manufacturer", 
               "Test Date", "Test Time", "Conducted By", "Test Location", "Test Result"]
    sheet.append(headers)
    
    # Populate rows with data from the log
    for entry in log:
        row = [
            entry["Visitor name"], 
            entry["Visitor address"], 
            entry["Current address"], 
            entry["Visitor date of birth"], 
            entry["Telephone number"], 
            entry["Email address"], 
            entry["Test ID"], 
            entry["Test Name"], 
            entry["Manufacturer"], 
            entry["Test Date"], 
            entry["Test Time"], 
            entry["Conducted By"], 
            entry["Test Location"], 
            entry["Test Result"]
        ]
        sheet.append(row)
    
    # Save the Excel file
    wb.save(file_path)
    print(f"Excel file saved at {file_path}")
