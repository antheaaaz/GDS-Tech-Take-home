import pandas as pd

# Load the restaurant data from the JSON file
with open("restaurant_data.json", encoding="utf-8") as file:
    restaurant_data = pd.read_json(file)

headers = ['Event Id', 'Restaurant Id', 'Restaurant Name','Photo URL','Event Title','Event Start Date','Event End Date']
restaurant_events = pd.DataFrame(columns=headers)

# Loop through each entry in the JSON data
for pages in restaurant_data["restaurants"]:
    # Check if 'restaurant' key exists in the entry
    for entry in pages:
        if 'restaurant' in entry:
            restaurant_info = entry['restaurant']
            if 'zomato_events' in restaurant_info:
                for event in restaurant_info['zomato_events']:  # Loop through multiple events
                    # Extract event details
                    event_info = event['event']

                    # Check if photos exist and extract the first photo URL (if available)
                    photo_url = event_info['photos'][0]['photo']['url'] if event_info.get('photos') else 'NA'

                    # Copy restaurant data for each event
                    restaurant_entry = {
                        'Event Id': event_info['event_id'],
                        'Restaurant Id': restaurant_info['id'],
                        'Restaurant Name': restaurant_info['name'],
                        'Event Title': event_info['title'],
                        'Event Start Date': event_info['start_date'],
                        'Event End Date': event_info['end_date'],
                        'Photo URL': photo_url,
                    }
                        
                        # Append the event entry to the restaurant details list
                    restaurant_events = pd.concat([restaurant_events,pd.DataFrame(restaurant_entry,columns=restaurant_events.columns,index=[0]).fillna("NA")],ignore_index=True)
        else:
            print(f"Skipping entry without 'event' key: {entry}")


restaurant_events.to_csv('restaurant_events.csv')

