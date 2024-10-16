from ALL_IMPORT import  *

def allocate_daily_visitors(store, month, day_count):
    """Allocate visitors per day for the given store and month."""
    mean_daily_visitors = store['monthly_thresholds'][month] // day_count
    daily_visitor_allocation = [mean_daily_visitors + random.randint(-5, 5) for _ in range(day_count)]
    return daily_visitor_allocation