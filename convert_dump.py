import json

with open('DZ1/dump.json', 'r', encoding='windows-1251') as f:
    data = json.load(f)

with open('DZ1/dump_utf8.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)