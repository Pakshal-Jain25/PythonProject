from ALL_IMPORT import *

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # Used when running as a bundled executable
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def SavePDF(log, month_name, year, store_name, employee_name, day):
    # Set up the folder structure
    logs_folder = f'LOG/{year}/{month_name}/{day}/{store_name}/{employee_name}'
    # logs_folder = f'DEMOLOG/{year}/{month_name}/{day}/{store_name}/{employee_name}'
    
    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)

    for i in range(len(log)) :
    # For each log entry, generate a PDF
    # for index, row in enumerate(log):  # Loop through each log entry
        visitor_name = log[i]["Visitor name"];
        file_name = f"{store_name}_{employee_name}_{day}_{month_name}_{visitor_name}.pdf"  # Create a unique filename
        
        pdf = FPDF()
        pdf.add_page()

        # Add fonts
        pdf.add_font('DejaVu', '', resource_path('DejaVu/DejaVuSans.ttf'), uni=True)
        pdf.add_font('DejaVu', 'B', resource_path('DejaVu/DejaVuSans-Bold.ttf'), uni=True)

        pdf.set_font('DejaVu', 'B', 12)

        pdf.set_text_color(137,249,221)
        pdf.cell(200, txt="Bürgertestcenter", ln=True, align='c')
        pdf.cell(200,5,txt="Augustusplatz", ln=True, align='c')

        # Title of the document (based on the template)
        pdf.set_font('DejaVu', 'B', 15)
        pdf.ln(5);
        pdf.set_text_color(0,0,0)
        pdf.cell(200, 5, txt="Bescheinigung über das Vorliegen eines Antigen-Tests", ln=True, align='l')
        pdf.cell(200, 5, txt="zum Nachweis des SARS-CoV-2 Virus", ln=True, align='l')
        pdf.set_font('DejaVu', '', 8)
        pdf.cell(200, 5, txt="Confirmation of a positive or negative antigen test to prove existence of the SARS-CoV-2 virus", ln=True)
        pdf.ln(5)

        # Visitor Information
        pdf.set_font('DejaVu', 'B', 15)
        pdf.cell(200, 5, txt="Getestete Person: ", ln=True)
        pdf.set_font('DejaVu', '', 8)
        pdf.cell(200, 5, txt="Person tested", ln=True)

        # Dynamically populate the fields using row data
        pdf.set_font('DejaVu', '', 15)
        pdf.cell(200, 5, log[i]["Visitor name"], ln=True)
        pdf.cell(200, 2, txt="."*100, ln=True)
        pdf.set_font('DejaVu', '', 8)
        pdf.cell(200, 5, 'Name, Vorname Last name,first name', ln=True)
        pdf.set_font('DejaVu', '', 15)
        pdf.cell(200, 5, log[i]["Visitor address"], ln=True)
        pdf.cell(200, 2, txt="."*100, ln=True)
        pdf.set_font('DejaVu', '', 8)
        pdf.multi_cell(200,5, 'Anschrift Hauptwohnung (Straße, Haus-Nr., PLZ, Ort, Land) Address of Primary place of recidence (street,unit no,post code,city,country)', ln=True)
        pdf.set_font('DejaVu', '', 15)
        pdf.cell(200, 5, log[i]["Current address"], ln=True)
        pdf.cell(200, 2, txt="."*100, ln=True)
        pdf.set_font('DejaVu', '', 8)
        pdf.multi_cell(200,5, 'ggf. Anschrift derzeitiger Aufenthaltsor  Address of current place of residence (if applicable)', ln=True)
        pdf.set_font('DejaVu', '', 15)        
        pdf.cell(200, 6, log[i]["Visitor date of birth"], ln=True)
        pdf.cell(200, 2, txt="."*100, ln=True)
        pdf.set_font('DejaVu', '', 8)
        pdf.cell(200, 5, 'Geburtsdatum*    Date of birth*', ln=True)
        pdf.set_font('DejaVu', '', 15)
        pdf.cell(200, 5, log[i]["Telephone number"], ln=True)
        pdf.cell(200, 2, txt="."*100, ln=True)
        pdf.set_font('DejaVu', '', 8)
        pdf.cell(200, 5 ,'Telefonnummer*  Telephone number*', ln=True)
        pdf.set_font('DejaVu', '', 15)
        pdf.cell(200, 5, log[i]["Email address"], ln=True)
        pdf.cell(200, 2, txt="."*100, ln=True)
        pdf.set_font('DejaVu', '', 8)
        pdf.cell(200, 5 ,'E-Mail-Adresse*   Email address*', ln=True)

        pdf.ln(5);
        pdf.set_font('DejaVu', '', 7)
        pdf.multi_cell(190, 3, txt="*Die Angabe ist freiwillig. Durch die Angabe von Telefonnummer oder E-Mail-Adresse können Sie im Fall der Kontaktnachverfolgung schneller kontaktiert werden.",ln=True)
        pdf.multi_cell(200, 3, txt="The information is optional.By providing phonenumber or email address,you can be contacted more quickly in case of follow up.")

        pdf.ln(5);
        # Test Information
        pdf.set_font('DejaVu', 'B', 15)
        # pdf.set_y(10);
        pdf.cell(200, 5, f'Coronavirus Antigen-Schnelltest: ', ln=False);
        # pdf.set_y(100);
        pdf.set_x(120);
        pdf.set_font('DejaVu', '', 10)
        pdf.set_text_color(255,0, 0);
        pdf.cell(200, 5, txt='BfArM Test-ID', ln=False);
        pdf.set_text_color(0,0, 0);
        pdf.set_x(147);
        pdf.cell(200,5, log[i]["Test ID"],ln=True);        
        pdf.set_font('DejaVu', '', 8)
        pdf.cell(200, 5,'Rapid Coronavirus antigen Test', ln=True)

        pdf.set_font('DejaVu', '', 15)
        pdf.cell(200, 5, 'Test: ', ln=False);
        pdf.set_x(80);
        pdf.cell(200, 1, log[i]["Test Name"], ln=True);
        pdf.set_x(80);
        pdf.cell(200, 5, txt="."*70, ln=True);

        pdf.set_font('DejaVu','',8);
        pdf.set_x(80);
        pdf.cell(200, 5,'Name des Tests  Test name', ln=True)
        
        pdf.ln(5);

        pdf.set_font('DejaVu','',15);
        pdf.cell(200, 5, 'Hersteller: ', ln=False);
        pdf.set_x(80);
        pdf.cell(200, 1, log[i]["Manufacturer"], ln=True);
        pdf.set_x(80);
        pdf.cell(200, 5, txt="."*70, ln=True);

        pdf.set_font('DejaVu','',8);
        pdf.cell(200,5,txt="Maufacturer");
        pdf.set_x(80);
        pdf.cell(200, 5,'Herstellername   Manufacturer name', ln=True)

        pdf.ln(5);

        pdf.set_font('DejaVu','',15);
        pdf.cell(200, 5, 'Testdatum/Uhrzeit: ', ln=False);
        pdf.set_x(80);
        pdf.cell(200, 1, f'{log[i]["Test Date"]}, {log[i]["Test Time"]}', ln=True);
        pdf.set_x(80);
        pdf.cell(200, 5, txt="."*70, ln=True);

        pdf.set_font('DejaVu','',8);
        pdf.cell(200,5,txt="Test date/time:",ln=True);

        pdf.ln(5);

        pdf.set_font('DejaVu','',15);
        pdf.cell(200, 5, 'Test durchgeführt durch: ', ln=False);
        pdf.set_x(80);
        pdf.cell(200, 1, log[i]["Conducted By"], ln=True);
        pdf.set_x(80);
        pdf.cell(200, 5, txt="."*70, ln=True);

        
        pdf.set_font('DejaVu','',8);
        pdf.cell(200,5,txt="Test Conducted by");
        pdf.set_x(80);
        pdf.cell(200, 5,'Name,Vorname   Last name,first name', ln=True)

        pdf.set_font('DejaVu','',15);
        pdf.set_x(80);
        pdf.multi_cell(130,5,log[i]["Test Location"], align='l',ln=True);
        pdf.set_x(80);
        pdf.cell(200, 1, txt="."*70, ln=True);

        pdf.set_font('DejaVu','',8);
        pdf.set_x(80);
        pdf.cell(200, 7,'testende Stelle, Ort   Testing facility,location', ln=True)

        # Test result checkboxes
        pdf.ln(5);
        pdf.set_font('DejaVu','',15);
        pdf.cell(200, 5, 'Testergebnis: ', ln=False)

        # Draw the checkboxes for "Negative" and "Positive"
        box_size = 5  # Size of the tick boxes
        pdf.set_x(80);
        pdf.set_font('DejaVu','',10);
        pdf.cell(20, 5, 'negativ', ln=False)
        negative_box_x = pdf.get_x()  # Store position for tick mark
        pdf.rect(negative_box_x - 3, pdf.get_y(), box_size, box_size)  # Draw negative box
        pdf.cell(30, 5, '', ln=False)  # Add some spacing between the boxes
        
        pdf.set_font('DejaVu','',10);
        pdf.cell(20, 5, 'positiv**', ln=False)
        positive_box_x = pdf.get_x()  # Store position for tick mark
        pdf.rect(positive_box_x - 3, pdf.get_y(), box_size, box_size)

        # Add symbols in appropriate box (X for cross, V for checkmark)
        pdf.set_font('DejaVu', 'B', 15)  # Set font for the checkmark/cross
        if log[i]["Test Result"].lower() == 'positive':
            pdf.set_xy(positive_box_x - 3.5, pdf.get_y())  # Move cursor inside the "Positive" box
            pdf.set_text_color(1,153,52);   #rgb(103,178,37) rgb(1,153,52)
            pdf.cell(5, 5, '√', ln=False)
        elif log[i]["Test Result"].lower() == 'negative':
            pdf.set_xy(negative_box_x - 3.5, pdf.get_y()) # Move cursor inside the "Negative" box
            pdf.set_text_color(255,0, 0);  
            pdf.cell(5, 5, '×', ln=False)
        
        pdf.set_text_color(0,0,0);
        pdf.ln(5);
        pdf.set_font('DejaVu','',8);
        pdf.cell(20,5,txt="Test result",ln=False);
        pdf.set_x(80);
        pdf.cell(20,5,txt="Negative",ln=False);
        pdf.set_x(130);
        pdf.cell(20,5,txt="Positive",ln=False);
        
        pdf.ln(10)
        pdf.set_font('DejaVu','',15);
        pdf.cell(200,3,log[i]["Test Date"],ln=True);
        pdf.cell(200, 4, txt="."*100, ln=True)
        pdf.set_font('DejaVu', '', 8)
        pdf.cell(200,4,text="Datum/Stempel testende Stelle/Unterschrift        Date/stamp of testing facility/signature");

        pdf.ln(10);
        pdf.set_font('DejaVu', '', 7)
        pdf.multi_cell(190, 3, txt="**Das Zeugnis zum Testergebnis wird bei einem positiven Testergebnis von der testenden Stelle an das örtliche Gesundheitsamt weitergeleitet.", ln=True)
        pdf.cell(200,3,txt="Positive test result are passed on to the local health authority by the testing facility.");
        
        # Save the PDF in the proper folder
        pdf.output(os.path.join(logs_folder, file_name))  # Save the PDF with unique filename