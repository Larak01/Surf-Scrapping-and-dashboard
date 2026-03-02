import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import re

def scrap_to_csv(url, output_path):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    scripts = soup.find_all('script')
    json_text = ""
    for s in scripts:
        if s.string and 'var data =' in s.string:
            json_text = re.search(r'var data = (\[.*?\]);', s.string, re.DOTALL).group(1)
            break
            
    raw_data = json.loads(json_text)
    all_rows = []
    
    for day_info in raw_data:
        date_text = day_info['dateKey'].replace('<br>', ' ')
        for hour_data in day_info['values']:
            all_rows.append({
                "day": date_text,
                "hour": hour_data['dateHour'].split(' ')[1][:5],
                "waves_size": hour_data['houlePrimaire'],
                "wind_speed": f"\n{hour_data['wind']}\n\n",
                "wind_direction": f"Orientation vent {hour_data['windDirection']}"
            })
            
    df = pd.DataFrame(all_rows)
    df.to_csv(output_path, index=True, index_label='')
    print(f"Extraction terminée. Fichier sauvegardé : {output_path}")

