import datetime

def create_ics_file(start_year, end_year):
    # Define the file name
    file_name = f"{start_year}_to_{end_year}_Week_Dates.ics"
    
    # Open the file in write mode
    with open(file_name, 'w') as file:
        # Write the calendar header
        file.write("BEGIN:VCALENDAR\n")
        file.write("VERSION:2.0\n")
        file.write("PRODID:-//Your Organization//Your Calendar//EN\n")
        
        for year in range(start_year, end_year + 1):
            # Initialize the start date for the current year
            start_date = datetime.date(year, 1, 1)
            
            # Calculate the end date (first day of the next year)
            end_date = datetime.date(year + 1, 1, 1)
            
            # Loop over each day of the current year
            current_date = start_date
            while current_date < end_date:
                # Convert to ISO-8601 week date format
                iso_week_date = current_date.isocalendar()
                event_summary = f"{current_date.year}-W{iso_week_date[1]:02d}-{iso_week_date[2]}"
                
                # Write event to file
                file.write("BEGIN:VEVENT\n")
                file.write(f"SUMMARY:{event_summary}\n")
                file.write(f"DTSTART;VALUE=DATE:{current_date.strftime('%Y%m%d')}\n")
                file.write(f"DTEND;VALUE=DATE:{(current_date + datetime.timedelta(days=1)).strftime('%Y%m%d')}\n")
                file.write(f"DESCRIPTION:Dette er ukedatoen til datoen som denne hendelsen er oppført i kalenderen din. Du kan lese mer om dette på pdog.no/ukekalender\n")
                file.write(f"UID:{current_date.strftime('%Y%m%d')}-W{iso_week_date[1]:02d}-{iso_week_date[2]}@example.com\n")
                file.write("SEQUENCE:0\n")
                file.write("DTSTAMP:20230210T120000Z\n")
                file.write("END:VEVENT\n")
                
                # Move to the next day
                current_date += datetime.timedelta(days=1)
        
        # Write the calendar footer
        file.write("END:VCALENDAR\n")
    
    print(f"ICS file created: {file_name}")

# Example usage for a range of years, e.g., 2024 to 2026
create_ics_file(1994, 2094)
