import pandas as pd

# Load the restaurant data from the JSON file
with open("restaurant_data.json", encoding="utf-8") as file:
    restaurant_data = pd.read_json(file)

headers = ['User Aggregate Rating','User Rating Text']
rating_details = pd.DataFrame(columns=headers)

# Loop through each entry in the JSON data
for pages in restaurant_data["restaurants"]:
    # Check if 'restaurant' key exists in the entry
    for entry in pages:
        if 'restaurant' in entry:
            restaurant_info = entry['restaurant']
            rating_entry = {
                'User Aggregate Rating': float(restaurant_info['user_rating']['aggregate_rating']),
                'User Rating Text': restaurant_info['user_rating']['rating_text']
            }
            if rating_entry['User Rating Text'] in ['Poor','Average','Good','Very Good','Excellent']:
                rating_details = pd.concat([rating_details,pd.DataFrame(rating_entry,columns=rating_details.columns,index=[0]).fillna("NA")],ignore_index=True)

rating_thresholds = rating_details.groupby('User Rating Text')['User Aggregate Rating'].agg(['min', 'max'])
rating_thresholds = rating_thresholds.sort_values(by=['min','max']).reset_index()

rating_thresholds.to_csv('rating_thresholds.csv')