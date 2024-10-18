from ALL_IMPORT import *
from AllocateVisitors import *
from GenerateDailyLogs import *
from SavePDF import *
from SaveExcel import *

# Function to convert hours from string to tuple of integers
def convert_hours(hours_str):
    # Check for the ':' character to identify the format
    if ':' in hours_str:
        start_hour_str, end_hour_str = hours_str.split(' - ') if ' - ' in hours_str else (hours_str, hours_str)
        
        # Convert to 24-hour format integers
        start_hour = int(start_hour_str.split(':')[0])
        end_hour = int(end_hour_str.split(':')[0])
    else:
        start_hour, end_hour = map(int, hours_str.split(' - '))
    
    return (start_hour, end_hour)

def process_store(store_info):
    store_name, store, visitors, month, month_names = store_info
    days_in_month = calendar.monthrange(2024, month)[1]
    store['daily_visitors'] = allocate_daily_visitors(store, month - 1, days_in_month)

    try:
        visited_today = set()  # Set to track visitors who have already visited a store on that day
        
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

            # Allocate visitors for the day, ensuring they haven't visited another store
            for employee_name, employee_log in employee_logs.items():
                for log in employee_log:
                    visitor_id = log.get("Visitor ID")  # Assume you have a "Visitor ID" field to uniquely identify visitors

                    if visitor_id and visitor_id not in visited_today:
                        # Save log and mark this visitor as visited
                        SaveExcel([log], month_names[month], 2024, store_name, employee_name, day)
                        visited_today.add(visitor_id)  # Mark this visitor as visited today
                    else:
                        print(f"Visitor {visitor_id} has already visited a store on {month_names[month]} {day}, 2024.")
                        
    except Exception as e:
        print(f"An exception occurred while processing store {store_name}: {e}")

def GenerateData(FilePath):
    # Load visitor data from Excel file
    start = time.time();
    store_tasks = [];
    month = 0;
    store_info = {};

    file_path = 'Data_Generation/visitor_data_1000.xlsx';
    sheet_name = 'Store Info';

    df = pd.read_excel(file_path,sheet_name=sheet_name);

    visitors = pd.read_excel(FilePath)
    store_locations = ['Store_1', 'Store_2', 'Store_3', 'Store_4', 'Store_5']

    # Populate store_info from the DataFrame
    for index, row in df.iterrows():
        store_name = row['Store Name']

        # Handle hours format
        hours_str = row['Hours']
        hours = convert_hours(hours_str)  # Convert hours string to tuple

        location = row['Location']
        employees = row['Employees'].split(', ')  # Split employees string into a list
        monthly_thresholds = [445] * 20  # Assuming the monthly thresholds are the same as before

        # Add the store info to the dictionary
        store_info[store_name] = {
            'hours': hours,
            'employees': employees,
            'location': location,
            'monthly_thresholds': monthly_thresholds
        }


    month_names = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 
                   7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

    # Prepare data for multiprocessing
    try :
        for i in range(1, 21) :
            month = month + 1;

            if(month > 12) :
                month = 1;
            
            for store_name, store in store_info.items():
                store_tasks.append((store_name, store, visitors, month, month_names))
        
        # Create a pool of worker processes
        with Pool() as pool:
            pool.map(process_store, store_tasks);

    except (EXCEPTION):
        print("An Exception Occured While Performing Multi Processing Tasks");

    end = time.time();
    Time = (end - start) / 60;
    

    formatted_time = f"{Time:.2f}";
    message = f"Logs File Generated Successfully in {formatted_time} Minutes!!!"
    
    messagebox.showinfo("Message", message);
