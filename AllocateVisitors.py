from ALL_IMPORT import  *

def allocate_daily_visitors(store, month, day_count):
    """Allocate visitors per day for the given store and month."""
    mean_daily_visitors = store['monthly_thresholds'][month] // day_count
    daily_visitor_allocation = [];

    for i in range(1,day_count + 1) :
        
        daily_visitor_allocation.append(mean_daily_visitors);
    
    # print(daily_visitor_allocation);
    
    return daily_visitor_allocation