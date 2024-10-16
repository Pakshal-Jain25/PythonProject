from ALL_IMPORT import *

def TestId(length=8):
    """Generate a random alphanumeric test ID."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_daily_logs(store, visitors, month, day, employees):
    """Generate logs for a particular store on a given day."""
    
    total_visitors_available = len(visitors['Visitor name'])
    visitors_needed = store['daily_visitors'][day - 1]

    visitors_to_sample = min(visitors_needed, total_visitors_available)

    if visitors_to_sample <= 0:
        return []  # Return an empty list if no visitors are needed or available

    visitors_of_the_day = random.sample(list(visitors.iterrows()), k=visitors_to_sample)  # Use iterrows() to access visitor details

    visit_logs = []

    days_in_month = calendar.monthrange(2024, month)[1]

    if day > days_in_month:
        raise ValueError(f"Day {day} is out of range for month {month}. Max is {days_in_month}.")

    opening_hour, closing_hour = store['hours']
    visit_time = datetime(2024, month, day, opening_hour, random.randint(0, 59))  # Starting time
    
    for _, visitor in visitors_of_the_day:
        # Increment visit time by 10 minutes for each visitor
        visit_time += timedelta(minutes=1)
        
        employee = random.choice(employees)  # Employee who signed
        
        # Generate random test ID
        test_id = TestId();
        test_name = "COVID-19 Antigen Rapid Test";
        manufacturer_name = "Hangzhou Clongene Biotech Co., Ltd.";
        
        # Include the required visitor details and assign the employee and visit time
        log_entry = {
            "Visitor name": visitor['Visitor name'],
            "Visitor address": visitor['Visitor address'],
            "Visitor date of birth": visitor['Visitor date of birth'],
            "Current address": "  ",
            "Telephone number": "  ",
            "Email address": visitor['Email address'],
            "Test Result": visitor['issue'],
            "Test Location": store['location'],
            "Test Date": visit_time.strftime("%Y.%m.%d"), #Visiting Date
            "Test Time": visit_time.strftime("%H:%M"),  # Visiting time
            "Test ID": test_id,  # Random Test ID
            "Test Name": test_name,  # Test Name
            "Manufacturer": manufacturer_name,  # Manufacturer Name
            "Conducted By": employee  # Employee
        }
        
        visit_logs.append(log_entry)

    return visit_logs
