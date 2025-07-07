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

## Download the datasets worked on
- the ab_ag.tsv can be downloadet here https://heibox.uni-heidelberg.de/d/ad23ebb995a04b138ee9/

## Packages that must be installed
- pandas
- scipy
- pingouin
- matplotlib
- seaborn


1. `data cleanup`
in this folder we have a total of five notebooks to filter and download the data used in our project, add columns to simplify analysis and create lists and DataFrames required later on in our project. 
Here the content of each notebook will be explained shortly but is explained in more detail in the notebooks themselves. 

- `01a_filter_summary_data.ipynb` @lóa, michi, lotta
In this notebook we will filter the data to our requirements. 
Data from `ab_ag.tsv` is imported into a DataFrame and filtered to only keep relevant columns (like `pdb`, `Hchain`, `antigen_chain`, etc.), non-scFv antibodies, 
structures with resolution ≤ 3.25 Ångström, drop any rows where critical columns are missing and remove entries of specific PDB IDs that don't exist on SAbDaB. 

To simplify our analysis we decided to reduce our dataset to ab_ag_komplexes where the antigen is a protein and for multiple entries for the same PDB value, keep only one. 

- `01b_exploratory` @lóa
This notebook is dedicated to the exploration of the dataset in order to make desicions regarding filtering.

- `02_download_chotia_PDB.ipynb` @lóa
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


2. `data exploration` Frage wo und ob wir das hier mit einbegreifen @michi??


3. `dataanalysis`
in this folder we did all our analysis on the data, we split the folder to three subfolders, according to the typ of analysis. 

- `01_length`
in this subfolder we analysed differences in the lenghts of the CDR-regions of different antibodies

   - `01_length_CDRseq.ipynb` @Clara
   The aim of this Jupyter Notebook is to analyse the lengths of the CDRs heavy chain regions, in order to characterize these sequences. Analyzing the variation in CDR lengths across different heavy chain types and comparing the results with the three different organsims (human, influenza, SARS-CoV-2) is relevant to understand these length distributions. 

- `02_sequence` 
in this subfolder we analysed differences in the aminoacid composition and sequence of antibodies

   - `01_aa_composytion.ipynb` @Michi
   This Jupyter Notebook analyzes the amino acid distributions in the complementarity-determining regions (CDR-H1, CDR-H2, CDR-H3) of antibodies targeting different antigens. The goal is to identify potentially characteristic differences between these groups.


   - `02_compare_all.ipynb` @Lotta
   In this notebook, antibodies directed against different antigens (SARS-CoV-2, influenza and human) are analyzed. It is investigated whether the properties of the CDR regions (charge, mass, polarity, hydrophobicity and length) differ between the groups. Statistical tests such as the Shapiro-Wilk test, Levene test, Welch-ANOVA and the Games-Howell method are used to test whether these differences are significant.

   - `03_pairwise_alignment.ipynb` @Clara
   The pairwise alignment analysis was performed to quantify the sequence similarity among CDR regions of antibodies derived from coronavirus, human, and influenza. The main aim was to compare CDR sequence diversity across different organisms and CDR types, enabling the identification of conserved or highly variable patterns.

   - `04_nw_alignment.ipynb` @Clara
   The Needleman–Wunsch algorithm was used to perform global sequence alignments that consider both matches,mismatches and gap penalties, providing a more biologically accurate measure of similarity compared to the global pairwise scoring method used before. Unlike this robust and more basic alignment, that only counts identical positions, Needleman–Wunsch evaluates the optimal alignment across the entire sequence length, accounting for insertions and deletions. This enables a more precise analysis of sequence conservation and divergence among CDR regions from different organisms.

   - `05_PCA.ipynb` @Michi, Lotta
   This notebook performs two Principal Component Analysis (PCA) based on the datasets all_data and all_data_normalized. The aim is to reduce the complex data to two principal components in order to visualize possible differences or groupings between antibodies against human proteins, influenza A and SARS-CoV-2


   - `06_logistic_regression`@Michi


-`03_contacts`
in this subfolder we analysed differences in atomic and resedue contacts in the CDR-regions of different antibodies. 

   - `01_find_atomic_contacts.ipynb` @lóa
   In this notebook we will create a DataFrame that contains atomic contacts for all the structures in our cleaned summary file.

   - `02_analyze_contacts.ipynb` @lóa
   This notebook alaysezes the contact frequencies of antibody residues within CDR regions across different species. We assess binding rates at each CDR and observe that some antibody–antigen structures form contacts outside the defined CDRs. CDR definitions are refined based on our binding analysis.


   - `03_analyze_CDRs.ipynb` @lóa



3. `generated`
3. `generated`
this is where we save all our generated DataFrames and lists

   - `cdrs` here are three csv files which list the PDB Ids
      - `seq` all generated tsv and txt files that were used for the sequence analysis
   
   - `contacts` all generated tsv and txt files that were used for the contact analysis

   - `data cleanup` contains tsv file with filtered ab_ag data set

   - `files` contains generated and saved Charts

   - `stat_tests` contains tsv file for Games-Howell-Test









r















