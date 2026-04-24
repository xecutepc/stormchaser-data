import json
import os

CHUNK_SIZE = 2000
BASE_OUT = r'C:\Users\e3483\Downloads\StormChaser\chunks'

def chunk_points(points, cx_key='x', cz_key='z'):
    chunks = {}
    for p in points:
        cx = int((p[cx_key] + 16000) / CHUNK_SIZE)
        cz = int((p[cz_key] + 16000) / CHUNK_SIZE)
        key = f"{cx}_{cz}"
        if key not in chunks:
            chunks[key] = []
        chunks[key].append(p)
    return chunks

def chunk_roads(roads):
    chunks = {}
    for road in roads:
        if not road['coords']:
            continue
        cx_avg = sum(c['x'] for c in road['coords']) / len(road['coords'])
        cz_avg = sum(c['z'] for c in road['coords']) / len(road['coords'])
        cx = int((cx_avg + 16000) / CHUNK_SIZE)
        cz = int((cz_avg + 16000) / CHUNK_SIZE)
        key = f"{cx}_{cz}"
        if key not in chunks:
            chunks[key] = []
        chunks[key].append(road)
    return chunks

def save_chunks(chunks, folder):
    out = os.path.join(BASE_OUT, folder)
    os.makedirs(out, exist_ok=True)
    for key, data in chunks.items():
        with open(os.path.join(out, f'chunk_{key}.json'), 'w') as f:
            json.dump(data, f)
    print(f"{folder}: {len(chunks)} chunks")

DOWNLOADS = r'C:\Users\e3483\Downloads'
SC = r'C:\Users\e3483\Downloads\StormChaser'

# Elevation
with open(os.path.join(DOWNLOADS, 'elevation.json')) as f:
    save_chunks(chunk_points(json.load(f)), 'elevation')

# Roads
with open(os.path.join(DOWNLOADS, 'roads.json')) as f:
    save_chunks(chunk_roads(json.load(f)), 'roads')

# Buildings
with open(os.path.join(DOWNLOADS, 'buildings.json')) as f:
    save_chunks(chunk_points(json.load(f)), 'buildings')

# Trees
with open(os.path.join(DOWNLOADS, 'trees.json')) as f:
    save_chunks(chunk_points(json.load(f)), 'trees')

# Lights
with open(os.path.join(DOWNLOADS, 'lights.json')) as f:
    save_chunks(chunk_points(json.load(f)), 'lights')

# Poles
with open(os.path.join(DOWNLOADS, 'poles.json')) as f:
    save_chunks(chunk_points(json.load(f)), 'poles')

# Signs
with open(os.path.join(DOWNLOADS, 'signs.json')) as f:
    save_chunks(chunk_points(json.load(f)), 'signs')

# Railways
with open(os.path.join(DOWNLOADS, 'railways.json')) as f:
    save_chunks(chunk_roads(json.load(f)), 'railways')

# Bridges
with open(os.path.join(DOWNLOADS, 'bridges.json')) as f:
    save_chunks(chunk_roads(json.load(f)), 'bridges')

# Parking
with open(os.path.join(DOWNLOADS, 'parking.json')) as f:
    save_chunks(chunk_points(json.load(f)), 'parking')

# Silos
with open(os.path.join(DOWNLOADS, 'silos.json')) as f:
    save_chunks(chunk_points(json.load(f)), 'silos')

# Water towers
with open(os.path.join(DOWNLOADS, 'water_towers.json')) as f:
    save_chunks(chunk_points(json.load(f)), 'water_towers')

# Fuel stations
with open(os.path.join(DOWNLOADS, 'fuel_stations.json')) as f:
    save_chunks(chunk_points(json.load(f)), 'fuel_stations')

print("All done!")