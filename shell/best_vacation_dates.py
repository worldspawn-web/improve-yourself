import datetime

def get_holidays(calendar_type):
    
    if calendar_type == "russian":
        return {
            "New Year": datetime.date(2025, 1, 1),
            "Orthodox Christmas": datetime.date(2025, 1, 7),
            "Defender of the Fatherland Day": datetime.date(2025, 2, 23),
            "International Women's Day": datetime.date(2025, 3, 8),
            "Labour Day": datetime.date(2025, 5, 1),
            "Victory Day": datetime.date(2025, 5, 9),
            "Russia Day": datetime.date(2025, 6, 12),
            "Unity Day": datetime.date(2025, 11, 4),
        }
    elif calendar_type == "american":
        return {
            "New Year": datetime.date(2025, 1, 1),
            "Martin Luther King Jr. Day": datetime.date(2025, 1, 20),
            "Presidents' Day": datetime.date(2025, 2, 17),
            "Memorial Day": datetime.date(2025, 5, 26),
            "Independence Day": datetime.date(2025, 7, 4),
            "Labor Day": datetime.date(2025, 9, 1),
            "Thanksgiving": datetime.date(2025, 11, 27),
            "Christmas": datetime.date(2025, 12, 25),
        }
    elif calendar_type == "european":
        return {
            "New Year": datetime.date(2025, 1, 1),
            "Easter Monday": datetime.date(2025, 4, 21),  # Примерная дата
            "Labour Day": datetime.date(2025, 5, 1),
            "Christmas": datetime.date(2025, 12, 25),
            "Boxing Day": datetime.date(2025, 12, 26),
        }
    else:
        raise ValueError("Unknown calendar type")
    
def generate_dates(year):
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    delta = datetime.timedelta(days=1)
    dates = []
    current_date = start_date
    
    while current_date <= end_date:
        dates.append(current_date)
        current_date += delta
    return dates

def find_best_vacations(dates, holidays, min_gap=30):
    best_weeks = []
    best_two_weeks = []
    
    for i in range(len(dates)):
        # Checking a week
        week = dates[i:i+7]
        holiday_count = sum(1 for day in week if day in holidays)
        best_weeks.append((week[0], holiday_count))
        
        # Checking 2-weeks
        two_weeks = dates[i:i+14]
        holiday_count = sum(1 for day in two_weeks if day in holidays)
        best_two_weeks.append((two_weeks[0], holiday_count))
        
    # Sorting by the amount of holidays
    best_weeks.sort(key=lambda x: x[1], reverse=True)
    best_two_weeks.sort(key=lambda x: x[1], reverse=True)
    
    # Filtering by seasons & min gap
    seasons = {
        "winter": (datetime.date(2025, 1, 1), datetime.date(2025, 3, 20)),
        "spring": (datetime.date(2025, 3, 21), datetime.date(2025, 6, 20)),
        "summer": (datetime.date(2025, 6, 21), datetime.date(2025, 9, 22)),
        "autumn": (datetime.date(2025, 9, 23), datetime.date(2025, 12, 31)),
    }
    
    selected_vacations = []
    last_vacation_end = None
    
    for period, options in [("week", best_weeks), ("two_weeks", best_two_weeks)]:
        for start_date, holiday_count in options:
            if period == "week":
                end_date = start_date + datetime.timedelta(days=7)
            else:
                end_date = start_date + datetime.timedelta(days=14)
                
            # Checking a season
            season_found = False
            for season, (season_start, season_end) in seasons.items():
                if season_start <= start_date <= season_end:
                    season_found = True
                    break
                
            if not season_found:
                continue
            
            # Checking gap
            if last_vacation_end and (start_date - last_vacation_end).days < min_gap:
                continue
            
            # Adding a vacation
            selected_vacations.append((start_date, end_date, holiday_count))
            last_vacation_end = end_date
            break # only 1 vacation per season
        
    return selected_vacations

def main():
    print("Choose your calendar type (Russian, American, European)...")
    calendar_type = input().strip().lower()
    
    holidays = get_holidays(calendar_type)
    dates = generate_dates(2025)
    
    selected_vacations = find_best_vacations(dates, holidays)
    
    print("\nBest dates:")
    for start_date, end_date, holiday_count in selected_vacations:
        print(f"Vacation from {start_date} until {end_date}.\nHolidays near: {holiday_count}\n\n")
        
if __name__ == "__main__":
    main()