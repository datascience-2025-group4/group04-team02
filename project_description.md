Topic 04: Antibody - Antigen interactions

============================================================

# Supervisor

----------


_Prof. Dominik Niopek_  ([dominik.niopek@uni-heidelberg.de](mailto:dominik.niopek@uni-heidelberg.de))

_Benedict Wolf_ ([benedict.wolf@uni-heidelberg.de](mailto:benedict.wolf@uni-heidelberg.de))

_Jan Mathony_  ([jan.mathony@uni-heidelberg.de](mailto:jan.mathony@uni-heidelberg.de))

Tutor:

_Enno Schaefer_ ([enno.schaefer@uni-heidelberg.de](mailto:enno.schaefer@uni-heidelberg.de))


# Introduction

------------

Antibodies play a crucial role in our immune system. They specifically recognize and bind antigens, thereby helping to differentiate between endogenous molecules and pathogens. While every antibody must be highly specific, their adaptive maturation mechanism theoretically allows the emergence of antibodies that bind to virtually any epitope. Despite being heavily investigated, the rules and constraints governing antibody-antigen (or more specifically paratope-epitope) interaction are still unclear. In this project, you will analyze a dataset experimentally resolved structures of antibody-antigen pairs. You will dive into the fundamentals and the computational analysis of protein-protein interactions to ultimately better understand antibody specificity.


# Objectives and work plan

------------------------

1. How diverse is the dataset? Do you think it covers the space of possible antibody/antigen sequences well?

1. Can you identify any Patterns (sequence, structure) in the interface between antibody and antigen? How variable are the antibodies? What kind of sequences do you observe? Is there a bias in the targeted regions of the Antigens?

1. What kind of important metrics can you identify that are neccessary to design good binders (antibodies)? How would you proceed when tasked with the development of a new antibody in silico that targets a selected antigen?


# Description of datasets

-----------------------


### Datatables
**ab_ag.tsv :**
Dataset derived from SAbDab. Contains information on a heavy-light chain pairing in a PDB structure combined with the corresponding antigen

**columns.tsv**
Column description for the `ab_ag.tsv` dataset



**uniprot_data.tsv :**
Mapping from PDB files to uniprot identifiers including additional information on the proteins.

### Download

https://heibox.uni-heidelberg.de/d/ad23ebb995a04b138ee9/


# Literature

----------



1. *James Dunbar, Konrad Krawczyk, Jinwoo Leem, Terry Baker, Angelika Fuchs, Guy Georges, Jiye Shi, Charlotte M. Deane, SAbDab: the structural antibody database, Nucleic Acids Research, Volume 42, Issue D1, 1 January 2014, Pages D1140–D1146, https://doi.org/10.1093/nar/gkt1043*

2. *M. Gao, J. Skolnick, Proceedings of the National Academy of Sciences. 121, e2410529121 (2024).*

3. *Chiu ML, Goulet DR, Teplyakov A, Gilliland GL. Antibody Structure and Function: The Basis for Engineering Therapeutics. Antibodies (Basel). 2019 Dec 3;8(4):55. doi: 10.3390/antib8040055. PMID: 31816964; PMCID: PMC6963682.*



# How to structure your project

-----------------------------

### Project proposal



You first task will we to define a **project proposal**, which should

include



-   summary of literature on this dataset

-   questions you want to address

-   approximate timetable



You will present this project proposal together with a literature review

on the subject 3 week after the beginning of the semester (10 minute

presentation + 5 minutes discussion).



### Project



You project **MUST** contain the following elements:

- **descriptive statistics** about the datasets

- **graphical representations**

- **dimension reduction** analysis (PCA, clustering or k-means)

- **statistical tests** (t-test, proportion tests etc)

- **linear regression** analysis, either uni- or multivariate



#### Data cleanup



You will be analyzing multiple data sets together. It is

essential that you explore each dataset and clean it. Cleaning can refer

to many things:



-   Removing/Imputing missing values

-   Removing low variance columns/rows

-   Removing batch effects

-   Removing outlier samples (only if it is due to technical issues !!)

-   Making sure that data is in the correct format, for example, numbers

    should be encoded as numeric and not as characters. Categorical

    variables should be factors etc.

-   Re-ordering rows/columns in meaningful and useful ways



#### Data exploration



Now that you have cleaned data, explore your data to understand its

structure. Perform basic exploratory data analysis.



-   Look at the distribution of the overall data, specific samples or

    features.

-   Visualize the data distribution

-   Visualize the inter-dependencies (e.g. correlations) among specific samples/features of

    interest

-   Check some of your hypothesis like - is something high/low between

    two conditions etc



#### Data reduction



You have a high dimension matrix, that is, you have way more features

 than observations.



-   Try out methods to reduce the dimensionality of this data.

-   Cluster your samples to identify similar and dis-similar groups

-   Check how well the groups separate based on the features of your

    interest



#### Data modelling



Use linear regression to evaluate the relation between variables and predicting one using others.