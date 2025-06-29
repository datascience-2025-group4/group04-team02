# group04-team02
See the project description here: https://github.com/maiwen-ch/2025_Data_Analysis_Topic_04_Antibody_Antigen_Interactions







# Data Cleanup

## 01a_filter_summary_data.ipynb

Filtered summary data from ag_ab dataframe
--> to only download pdb files we actually need and want and not all of them

- Loads a file** (`ab_ag.tsv`) with information about antibody-antigen structures

- Keep only certain columns, e.g. PDB ID, chain info, species, resolution etc.

- Removes all rows with missing values** (NaNs)

- Filters for classical antibodies** - i.e. no scFv (single-chain fragment variable)

- Keep only entries with high resolution** (≤ 3.0 Å), i.e. well-resolved structures.

- Gets all unique PDB IDs** from the filtered data.

- Saves these PDB IDs as a list in a new file `pdb_ids.csv`.

# create pdb lists with unique pdbs for influenza, human and sars cov2 Explanation

= Extract SARS-CoV-2/homo sapiens/and influenza A-specific PDB IDs from antibody data

 Three consecutive codes which create three dataframes with the PDB IDs for each species.

- Filters all rows containing the respective species in the antigen_species column

- Uses the previously cleaned DataFrame (df_filtered), in which: no scFv are contained, no NaNs occur, only structures with resolution ≤ 3.0 Å are contained.

- Retrieves all unique PDB IDs from specific subset

- Saves these PDB IDs in a new CSV file

- The generated file contains: one column: pdb containing the IDs

## 01b_exploratory-ipynb

- Tests run to see which methods were used to detect different structures

## 02_download_chotia_PDB.ipynb 

- Downloadfunktion: 

- first its checked if the chosen file already exists - if so Download is skipped




- Because we have three different PDB-Directories we make 

# 03_aa_composition.ipynb (Michi)
-->Analysis of Amino Acid Distribution in CDR Regions of Different Antibody Groups

## Analysis of Amino Acid Distribution
This Jupyter Notebook analyzes the **amino acid distributions in the complementarity-determining regions (CDR-H1, CDR-H2, CDR-H3)** of antibodies targeting different antigens (SARS-CoV-2, Influenza, and human-specific targets). The goal is to identify potentially characteristic differences between these groups.

### Approach

1. **Calculation of amino acid distributions:**
   - For each CDR region, the relative frequency of each amino acid was calculated.
   - This was done separately for each antigen source: `Corona`, `Influenza`, and `Human`.

2. **Visualization:**
   - Grouped bar plots display the amino acid distributions per region and antigen group.

3. **Statistical significance analysis:**
   - The **Mann–Whitney U test** was used to compare distributions between groups.
   - combined dataframe mit all the results from `Mann-Whitney U` test was made
   - p-values were adjusted using the **Benjamini–Hochberg correction**.
   - Results were visualized as a heatmap using `-log10(adjusted p-value)`.
   - In the heatmap, differences with **–log₁₀(adjusted p) > 1.3** are considered statistically significant, as this corresponds to an **adjusted p-value < 0.05**.


## Analysis of Amino Acid Property Groups
In addition to analyzing the distribution of individual amino acids, the residues were grouped into five chemically and functionally relevant categories:

- **Nonpolar (hydrophobic)**: A, V, L, I, M, P, G  
- **Polar (hydrophilic)**: S, T, N, Q, C  
- **Basic**: K, R, H  
- **Acidic**: D, E  
- **Aromatic**: F, W, Y

For each CDR region and antigen group (`Corona`, `Influenza`, `Human`), the **summed relative frequency** of each property group was calculated.

### Visualization:
- Grouped bar plots were used to compare the distribution of amino acid property classes across antibody groups.
 


## 04_compare_all.ipynb










## summary_all_data.ipynb

Merging CDR sequence data

- Loads three data sets with antibody information (each against:
human structures (human), influenza viruses (influenza), SARS-CoV-2 (sars_cov2)).

- Adds a new column indicating where the data comes from (e.g. "Source" = human).

- Joins all three tables into one large common table.

- Shows how many rows and columns the new table has and displays some column names.

- Saves the new table under the name all_data.tsv as a file (in the current folder)

---

## Calculate relative amino acid abundance

- This script calculates relative abundances of amino acids in the three CDR regions (CDR\_H1, CDR\_H2, CDR\_H3) for each antibody.

- Instead of just looking at the absolute number (e.g. how often “A” occurs), it is calculated


