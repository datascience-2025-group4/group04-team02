# group04-team02
See the project description here: https://github.com/maiwen-ch/2025_Data_Analysis_Topic_04_Antibody_Antigen_Interactions



# Topic 04: Antibody - Antigen interactions

# Group 02: Michaela Gabor, Lotta Gambert, Clara Zajac, Lóa Zink

# Supervisors: 
- Prof. Dominik Niopek (dominik.niopek@uni-heidelberg.de)
- Jan Mathony (jan.mathony@uni-heidelberg.de) 
- Benedict Wolf (benedict.wolf@uni-heidelberg.de)

# Tutor: 
- Enno Schäfer (enno.schaefer@uni-heidelberg.de)

## Research Question
- The aim of our project is to investigate whether the structural features of the CDR regions differ depending on the type of antigen. More specifically, we looking for characteristic patterns in the CDRs that distinguish between antibodies that target different classes of antigen.

## Structure of the repository
To run our code, first load the dataset specified below (ab_ag.tsv: a dataset derived from SAbDab) into a folder named `data`, the folder should be a direct subdirectory of group04-team02. 
The dataset contains information about heavy-light chain pairing in a PDB structure combined with the corresponding antigen.
To run our code, our repository must be loaded from top to bottom.

1. `data exploration` Frage wo und ob wir das hier mit einbegreifen @michi??

2. `data cleanup`
in this folder we have a total of five notebooks to filter and download the data used in our project, add columns to simplify analysis and create lists and DataFrames required later on in our project. 
Here the content of each notebook will be explained shortly but is explained in more detail in the notebooks themselves. 

- `01a_filter_summary_data.ipynb` @lóa, michi, lotta
In this notebook we will filter the data to our requirements. 
Data from `ab_ag.tsv` is imported into a DataFrame and filtered to only keep relevant columns (like `pdb`, `Hchain`, `antigen_chain`, etc.), non-scFv antibodies, 
structures with resolution ≤ 3.25 Ångström, drop any rows where critical columns are missing and remove entries of specific PDB IDs that don't exist on SAbDaB. 

To simplify our analysis we decided to reduce our dataset to ab_ag_komplexes where the antigen is a protein and for multiple entries for the same PDB value, keep only one. 

- `01b_exploratory`
This notebook is dedicated to the exploration of the dataset in order to make desicions regarding filtering.

- `02_download_chotia_PDB.ipynb`
In this notebook the prefiltered pdb files from notebooks 'requiered for this project will be downloaded from the internet

- `03a_cdr_h_seq_influenza.ipynb` @michi 
This Notenbook extracts CDR-H1, CDR-H2 and CDR-H3 sequences from Chotia-numbered PDB files for Antibodies against Influenza proteins

- `03b_cdr_h_seq_human.ipynb` @michi 
This Notenbook extracts CDR-H1, CDR-H2 and CDR-H3 sequences from Chotia-numbered PDB files for Antibodies against Human proteins

- `03c_cdr_h_seq_corona.ipynb` @michi 
This Notenbook extracts CDR-H1, CDR-H2 and CDR-H3 sequences from Chotia-numbered PDB files for Antibodies against SarsCov2 proteins

- `04_extend-existing-data.ipynb`@lotta

- `05_summary_all_data.ipynb`@lotta


3. `dataanalysis`
in this folder we did all our analysis on the data, we split the folder to three subfolders, according to the typ of analysis. 

in subfolder `01_length` we analysed differences in the lenghts of the CDR-regions of different antibodies

in subfolder `02_sequence` we analysed differences in the aminoacid composition and sequence of antibodies
- `01_aa_composytion.ipynb` @Michi
This Jupyter Notebook analyzes the amino acid distributions in the complementarity-determining regions (CDR-H1, CDR-H2, CDR-H3) of antibodies targeting different antigens. The goal is to identify potentially characteristic differences between these groups.


- `02_compare_all.ipynb` @Lotta

- `03_pairwise_alignment.ipynb` @Clara

- `04_nw_alignment.ipynb` @Clara

- `05_PCA.ipynb` @Michi

- `06_logistic_regression`@Michi



in subfolder `03_contacts` we analysed differences in atomic and resedue contacts in the CDR-regions of different antibodies. 

- `01_find_atomic_contacts.ipynb`


3. `generated``
this is where we save all our generated DataFrames and lists
.
.
.









## Convering the mandatory aspects of the project
Our project was supposed to contain the following elements. Here we,we lost which sub-topic covers which mandatory aspect:

- descriptive statistics about the datasets
- graphical representations
- dimension reduction analysis (PCA, clustering or k-means)
- statistical tests (t-test, proportion tests etc)
- linear regression analysis, either uni- or multivariate



## Additional files and folders



## Download the datasets worked on
- the ab_ag.tsv can be downloadet here https://heibox.uni-heidelberg.de/d/ad23ebb995a04b138ee9/








# Data Cleanup

## 01a_filter_summary_data.ipynb (Michi & Lotta)

Filtered summary data from ag_ab dataframe
--> to only download pdb files we actually need and want and not all of them

- Loads a file (`ab_ag.tsv`) with information about antibody-antigen structures
- Keep only certain columns, e.g. PDB ID, chain info, species, resolution etc.
- Removes all rows with missing values (NaNs)
- Filters for classical antibodies - i.e. no scFv (single-chain fragment variable)
- Keep only entries with high resolution (≤ 3.0 Å), i.e. well-resolved structures.
- Gets all unique PDB IDs from the filtered data.
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
 


## 04_compare_all.ipynb (Lotta)

# Comparison of the biophysical characteristics of CDR-H3, H2 and H3 between the individual species

# 1.
This code uses ANOVA to test for significant differences in the physicochemical properties of CDR regions between antibodies targeting SARS-CoV-2, Influenza, and human antibody types.

# 2.
Following a significant ANOVA result, the Tukey-HSD (Honest Significant Difference) test is applied to determine which specific groups differ significantly.

# 3.
This section visualizes the Tukey-HSD results as a confidence interval plot. Each group comparison is represented by a horizontal line, with significant differences highlighted in red. The vertical line at x = 0 indicates the threshold for no significant difference.

=> All analyses were conducted separately for the CDR regions H1, H2, and H3 to investigate differences in structural properties depending on the antibody source.

# Compare lengths












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


