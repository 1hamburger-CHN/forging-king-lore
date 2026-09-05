import json
import re

def extract_names():
    try:
        with open(r'e:\锻造之王宇宙\Scotalin（斯科塔林大陆） Full 2026-08-20-21-27.json', 'r', encoding='utf-8') as f:
            data = f.read()
        
        # This file might be a Wonderdraft file or Azgaar. Let's just find Chinese strings or 'name' attributes.
        # We can use regex to find all "name": "something" or "text": "something"
        names = re.findall(r'"name"\s*:\s*"([^"]+)"', data)
        texts = re.findall(r'"text"\s*:\s*"([^"]+)"', data)
        
        unique_names = set(names + texts)
        
        # Filter for things that look like Chinese names or interesting english names
        chinese_names = [n for n in unique_names if re.search(r'[\u4e00-\u9fff]', n)]
        print("Possible Place Names:", chinese_names)
        
    except Exception as e:
        print("Error:", e)

extract_names()

