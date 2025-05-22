import pandas as pd

# Lade die beiden Datensätze (Passe ggf. Pfade an)
dfc1 = pd.read_csv("ab_ag copy.tsv", sep="\t")
dfc2 = pd.read_csv("uniprot_data copy.tsv", sep="\t")

print(dfc1.columns)
print(dfc2.columns)


