from ALL_IMPORT import *
from AllocateVisitors import *
from GenerateDailyLogs import *
from SavePDF import *

def process_store(store_info):
    store_name, store, visitors, month, month_names = store_info
    days_in_month = calendar.monthrange(2024, month)[1]
    store['daily_visitors'] = allocate_daily_visitors(store, month - 1, days_in_month)

    try : 
        for day in range(1, days_in_month + 1):
            if datetime(2024, month, day).weekday() in (5, 6):  # Skip weekends
                continue
            
            logs = generate_daily_logs(store, visitors, month, day, store['employees'])
            
            employee_logs = {}
            for log in logs:
                    if isinstance(log, dict) and "Conducted By" in log:
                        employee_name = log["Conducted By"]  # Access employee name
        
                        # Ensure employee_name is a string
                        if isinstance(employee_name, str):
                            if employee_name not in employee_logs:
                                employee_logs[employee_name] = []
                            employee_logs[employee_name].append(log)
                        else:
                            print(f"Error: Expected a string for employee_name but got: {employee_name}")
            # print(employee_logs);
            for employee_name, employee_log in employee_logs.items():
                SavePDF(employee_log, month_names[month], 2024, store_name, employee_name, day)
    except (EXCEPTION) :
        print("An Execption while storing data into the excel file");

def GenerateData(FilePath):
    # Load visitor data from Excel file
    start = time.time();
    store_tasks = [];
    month = 0;

    visitors = pd.read_excel(FilePath)
    store_locations = ['Store_1', 'Store_2', 'Store_3', 'Store_4', 'Store_5']

    # Store data - opening hours, employees, monthly thresholds
    store_info = {
        'Bürgertestcenter Augustusplatz': {
            'hours': (9, 17), 
            'employees': ['David Guetta', 'Dua lipa', 'Alex Paul', 'Drew Taggert'],
            'location':'Bürgertestcenter Augustusplatz, Leipzig',
            'monthly_thresholds': [445] * 20
        },
        'AKZYTE Corona rapid test center': {
            'hours': (9, 17), 
            'employees': ['Tony Stark', 'Vin Diesel', 'Chris Evans', 'Tom Holland'],
            'location':'AKZYTE Corona rapid test center,Tröndlinring 9,Leipzig',
            'monthly_thresholds': [445] * 20
        },
        'Pharmacy Holzhausen': {
            'hours': (9, 17), 
            'employees': ['Scarlet Johansson', 'Jordan Brewster', 'Markuffalo', 'Robert Downey Jr.'],
            'location':'Pharmacy Holzhausen,Stötteritzer Landstraße 28, Leipzig',
            'monthly_thresholds': [445] * 20
        },
        'Biodynamic practices Südvorstadt': {
            'hours': (9, 17), 
            'employees': ['Chris Hemsworth', 'Jeremy Renner', 'Brie Larson', 'Paul Rudd'],
            'location':'Biodynamic practices Südvorstadt,Kurt-Eisner-Straße 15,Leipzig',
            'monthly_thresholds': [445] * 20
        },
        'Citizens Test Center Eutritzsch': {
            'hours': (9, 17), 
            'employees': ['Elizabeth Olsen', 'Don Cheadle','Chadwick Boseman', 'Joe Russo'],
            'location':'Citizens Test Center Eutritzsch,Theresienstraße 16,Leipzig',
            'monthly_thresholds': [445] * 20
        },
    }

    month_names = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 
                   7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

    # Prepare data for multiprocessing
    try :
        for i in range(1, 21) :
            month = month + 1;

            if(month > 12) :
                month = 1;
            
            for store_name, store in store_info.items() :
                store_tasks.append((store_name, store, visitors, month, month_names))  

        # Create a pool of worker processes
        with Pool() as pool:
            pool.map(process_store, store_tasks)
    except (EXCEPTION):
        print("An Exception Occured While Performing Multi Processing Tasks");

    end = time.time();
    Time = (end - start) / 60;
    

    formatted_time = f"{Time:.2f}";
    message = f"Logs File Generated Successfully in {formatted_time} Minutes!!!"
    
    messagebox.showinfo("Message", message);
