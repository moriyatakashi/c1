import requests
from bs4 import BeautifulSoup
import json
url = 'http://localhost:8000/a.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
select_tag = soup.find('select')
option_list = []
if select_tag:
    options = select_tag.find_all('option')
    for opt in options:
        option_list.append({
            'value': opt.get('value'),
            'text': opt.text.strip()
        })
with open('a.json', 'w', encoding='utf-8') as f:
    json.dump(option_list, f, ensure_ascii=False, indent=2)
print("a.json に保存しました。")
