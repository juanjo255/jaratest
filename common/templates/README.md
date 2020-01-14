#  Project title (Ex: 2019astrpi)
[Brief explanation of project goes here]

# Producing databases
The file `studyparams.py` contains the list of animals used in this study as well as 
relevant file paths and statistical parameters for the database calculations

## `database_generation.py`
[Specify here which databases are generated and any special instructions for running this script]

## `database_generation_funcs.py`
Contains functions called during database generation.


# Database contents

The initial database is generated by `celldatabase.generate_cell_database_from_subjects()`. It contains columns according to the inforec files (`'subject'`, `'date'`, etc) and the spike sorting results (`'cluster'`, `'spikeShape'`, etc).


## Base stats:
These are additional columns calculated for all cells:

* *fancyStat*: mean firing rate after event x.
* *anotherStat*: max firing rate under y condition.

## Indices:
These are additional columns calculated for a selected set of cells:

* *fancyIndex*: A-B/A+B where A is the response and B is the baseline.


# Figures

All figures require access to the databases, the clustered ephys data, and the behavior data.

## Figure 1 (Write name of this figure here)
Created by `figure_myfirstfig.py`.

### Panel A
Cartoon of a neural circuit created in Inkscape.
### Panel B
Example cell showing strong response, using data generated by `generate_example_firstfig.py`.
