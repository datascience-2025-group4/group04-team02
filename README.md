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
In this notebook, CDR sequence files are systematically expanded. First, the sequences are checked for validity and the frequency of the individual amino acids is determined. Then average properties such as hydrophobicity, mass, charge and polarity are calculated and added for each CDR region. Finally, the length of each CDR sequence is determined and integrated into the original files as new information.

- `05_summary_all_data.ipynb`@lotta
In this notebook, three data sets from three different sources (human, influenza, SARS-CoV-2) are merged and supplemented by an sorce column. The relative frequency of the 20 amino acids is then calculated for each CDR region. The results are saved in all_data.tsv and in all_data_normalozed.tsv and displayed for control purposes.


3. `dataanalysis`
in this folder we did all our analysis on the data, we split the folder to three subfolders, according to the typ of analysis. 

in subfolder `01_length` we analysed differences in the lenghts of the CDR-regions of different antibodies

- `01_length_CDRseq.ipynb` @Clara
The aim of this Jupyter Notebook is to analyse the lengths of the CDRs heavy chain regions, in order to characterize these sequences. Analyzing the variation in CDR lengths across different heavy chain types and comparing the results with the three different organsims (human, influenza, SARS-CoV-2) is relevant to understand these length distributions. 

in subfolder `02_sequence` we analysed differences in the aminoacid composition and sequence of antibodies

- `01_aa_composytion.ipynb` @Michi
This Jupyter Notebook analyzes the amino acid distributions in the complementarity-determining regions (CDR-H1, CDR-H2, CDR-H3) of antibodies targeting different antigens. The goal is to identify potentially characteristic differences between these groups.


- `02_compare_all.ipynb` @Lotta
In this notebook, antibodies directed against different antigens (SARS-CoV-2, influenza and human) are analyzed. It is investigated whether the properties of the CDR regions (charge, mass, polarity, hydrophobicity and length) differ between the groups. Statistical tests such as the Shapiro-Wilk test, Levene test, Welch-ANOVA and the Games-Howell method are used to test whether these differences are significant.

- `03_pairwise_alignment.ipynb` @Clara
The pairwise alignment analysis was performed to quantify the sequence similarity among CDR regions of antibodies derived from coronavirus, human, and influenza. The main aim was to compare CDR sequence diversity across different organisms and CDR types, enabling the identification of conserved or highly variable patterns.

- `04_nw_alignment.ipynb` @Clara
The Needleman–Wunsch algorithm was used to perform global sequence alignments that consider both matches/mismatches and gap penalties, providing a more biologically accurate measure of similarity compared to simpler scoring methods. Unlike basic alignment approaches that only count identical positions, Needleman–Wunsch evaluates the optimal alignment across the entire sequence length, accounting for insertions and deletions. This enables a more precise assessment of sequence conservation and divergence among CDR regions from different organisms.

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


