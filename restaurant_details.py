import pandas as pd

# Load the restaurant data from the JSON file
with open("restaurant_data.json", encoding="utf-8") as file:
    restaurant_data = pd.read_json(file)

# Load the country code data from the Excel file
country_data = pd.read_excel("Country-Code.xlsx")

# Create a dictionary to map country codes to country names
country_code_lookup = dict(zip(country_data['Country Code'], country_data['Country']))
headers = ['Restaurant Id', 'Restaurant Name','Country','City','User Rating Votes','User Aggregate Rating','Cuisines','Event Id','Event Title','Event Start Date','Event End Date','Photo URL']
restaurant_details = pd.DataFrame(columns=headers)

# Loop through each entry in the JSON data
for pages in restaurant_data["restaurants"]:
    # Check if 'restaurant' key exists in the entry
    for entry in pages:
        if 'restaurant' in entry:
            restaurant_info = entry['restaurant']

            # Extract the country ID and match it to the country name from the country code dictionary
            country_id = restaurant_info['location']['country_id']
            country = country_code_lookup.get(country_id, None)

            # If country is found in country_code_dict, extract the required fields
            if country:
                restaurant_entry = {
                    'Restaurant Id': restaurant_info['id'],
                    'Restaurant Name': restaurant_info['name'],
                    'Country': country,
                    'City': restaurant_info['location']['city'],
                    'User Rating Votes': restaurant_info['user_rating']['votes'],
                    'User Aggregate Rating': float(restaurant_info['user_rating']['aggregate_rating']),
                    'Cuisines': restaurant_info['cuisines'],
                }

                # Check if events are available in the restaurant's data (using the 'zomato_events' key)
                if 'zomato_events' in restaurant_info:
                    for event in restaurant_info['zomato_events']:  # Loop through multiple events
                        # Extract event details
                        event_info = event['event']

                        # Check if photos exist and extract the first photo URL (if available)
                        photo_url = event_info['photos'][0]['photo']['url'] if event_info.get('photos') else 'NA'

                        # Copy restaurant data for each event
                        restaurant_entry.update({
                            'Event Id': event_info['event_id'],
                            'Event Title': event_info['title'],
                            'Event Start Date': event_info['start_date'],
                            'Event End Date': event_info['end_date'],
                            'Photo URL': photo_url,
                        })
                        
                        # Append the event entry to the restaurant details list
                restaurant_details = pd.concat([restaurant_details,pd.DataFrame(restaurant_entry,columns=restaurant_details.columns,index=[0]).fillna("NA")],ignore_index=True)
        else:
            print(f"Skipping entry without 'restaurant' key: {entry}")

# print(restaurant_details)  # Check if data exists in the list

restaurant_details.to_csv('restaurant_details.csv') 