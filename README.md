# group04-team02
See the project description here: https://github.com/maiwen-ch/2025_Data_Analysis_Topic_04_Antibody_Antigen_Interactions




# summary_all_data.ipynb

Merging CDR sequence data


- Loads three data sets with antibody information (each against:
human structures (human), influenza viruses (influenza), SARS-CoV-2 (sars_cov2)).

- Adds a new column indicating where the data comes from (e.g. "Source" = human).

- Joins all three tables into one large common table.

- Shows how many rows and columns the new table has and displays some column names.

- Saves the new table under the name all_data.tsv as a file (in the current folder).