import json
import os

with open(r'C:\Users\e3483\Downloads\elevation.json') as f:
    points = json.load(f)

chunk_size = 2000
os.makedirs(r'C:\Users\e3483\Downloads\StormChaser\elevation_chunks', exist_ok=True)

chunks = {}
for p in points:
    cx = int((p['x'] + 16000) / chunk_size)
    cz = int((p['z'] + 16000) / chunk_size)
    key = f"{cx}_{cz}"
    if key not in chunks:
        chunks[key] = []
    chunks[key].append(p)

for key, data in chunks.items():
    with open(rf'C:\Users\e3483\Downloads\StormChaser\elevation_chunks\chunk_{key}.json', 'w') as f:
        json.dump(data, f)

print(f"Done! {len(chunks)} chunks created")