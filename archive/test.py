import os
import requests
import pandas as pd

# ----------- Konfiguration -----------
PDB_URL = "https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/sabdab/pdb/{}/?scheme=chothia"
PDB_DIR = os.path.join(os.path.dirname(__file__), "pdb_cf")
CSV_FILENAME = "pdb_ids_sars_cov2.csv"  # kann auch pdb_ids_sars_cov2.csv sein

# ----------- Vorbereitung -----------
os.makedirs(PDB_DIR, exist_ok=True)  # Verzeichnis erstellen, falls es nicht existiert

csv_path = os.path.join(os.path.dirname(__file__), CSV_FILENAME)
df = pd.read_csv(csv_path, header=None)

# Nur gültige 4-stellige PDB-IDs behalten
unique_pdb_ids = df[0].dropna().astype(str).str.strip()
unique_pdb_ids = unique_pdb_ids[unique_pdb_ids.str.match(r"^[A-Za-z0-9]{4}$")].tolist()

# ----------- Download-Funktion -----------
def download_pdb(pdb_id):
    url = PDB_URL.format(pdb_id)
    filename = os.path.join(PDB_DIR, f"{pdb_id}.pdb")

    if os.path.exists(filename):
        print(f"{pdb_id} already exists.")
        return filename

    response = requests.get(url)
    if response.status_code == 200 and len(response.content) > 100:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"{pdb_id} downloaded successfully.")
        return filename
    else:
        print(f"{pdb_id} could not be downloaded.")
        return None

# ----------- Hauptlauf -----------
print(f"Starte Download von {len(unique_pdb_ids)} PDB-Dateien...\n")

for i, pdb_id in enumerate(unique_pdb_ids, 1):
    print(f"[{i}/{len(unique_pdb_ids)}] {pdb_id}:", end=" ")
    download_pdb(pdb_id)

print("\nFertig.")
