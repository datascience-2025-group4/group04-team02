import pandas as pd  # Pandas wird als "pd" importiert
df = pd.read_csv('../Data/ab_ag.tsv', sep='\t')  # "df" ist der Name des DataFrames
print(df.head())  # Zeigt die ersten 5 Zeilen des Datensatzes an
#um es anzeigen zu lassen im terminal python3 Lotta.ab_ag.py eingeben 


