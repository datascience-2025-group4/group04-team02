import os
from Bio.PDB import PDBParser
from Bio.SeqUtils import seq1

# Path to your Chothia-numbered PDB files
PDB_DIR = "../data/pdb_cnf"

# Parser setup
parser = PDBParser(QUIET=True)

def extract_cdr_h3(pdb_path):
    structure = parser.get_structure("antibody", pdb_path)
    cdr_h3 = []

    for model in structure:
        for chain in model:
            if chain.id == "H":  # Heavy chain
                for residue in chain:
                    hetfield, resseq, _ = residue.get_id()
                    if hetfield == " " and 95 <= resseq <= 102:  # Chothia H3 range
                        if "CA" in residue:
                            try:
                                aa = seq1(residue.resname)
                                cdr_h3.append(aa)
                            except KeyError:
                                pass  # Skip unknown residue
    return "".join(cdr_h3)

# Loop through all files and extract CDR-H3
cdr_h3_dict = {}

for filename in os.listdir(PDB_DIR):
    if filename.endswith(".pdb"):
        filepath = os.path.join(PDB_DIR, filename)
        try:
            h3_seq = extract_cdr_h3(filepath)
            pdb_id = filename.split(".")[0].lower()
            cdr_h3_dict[pdb_id] = h3_seq
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Print or save result
for pdb_id, seq in cdr_h3_dict.items():
    print(f"{pdb_id}: {seq}")
