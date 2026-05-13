# Fasta_Tools

**Author**: Elise Gay (EPHE, MNHN)  
**Description**: A collection of Python functions to parse, process, and manipulate FASTA files.  

This module provides handy utilities to split, subset, deduplicate, and analyze FASTA sequences.

---

## Features

- Split FASTA files into chunks of `n` sequences  
- Convert FASTA to dictionary `{seq_id: sequence}`  
- Extract sequences by ID list  
- Rename FASTA IDs using an external mapping file  
- Remove duplicate sequences while keeping unique IDs  
- Compute percentage of ambiguous bases (`N/n`) in sequences  

---

## Installation

Clone this repository and import the module into your project:

```bash
git clone https://github.com/EliseGAY/Fasta_ToolsBox.git
cd Fasta_ToolsBox
pip install -e .
```

In your Python script:

```python
import fasta_tools
```

---

## Usage

### Split a FASTA file
```python
fasta_tools.split_fasta("example.fasta", 100)
```
➡ Splits `example.fasta` into multiple smaller files with 100 sequences each.  

### Convert FASTA into a dictionary
```python
d = fasta_tools.fasta_dict("example.fasta")
print(d["seq1"])
```
➡ Prints the sequence for ID `seq1`.  

### Extract sequences by ID
```python
ids = ["seq1", "seq2", "seq3"]
fasta_tools.Select_Seq("example.fasta", ids, "subset.fasta")
```
➡ Creates `subset.fasta` containing only the requested sequences.  

### Rename FASTA IDs
```python
fasta_tools.add_fasta_name("example.fasta", "new_ids.txt", "renamed.fasta")
```
➡ `new_ids.txt` should contain one new name per line.  

### Remove duplicate sequences
```python
fasta_tools.remove_dup("example.fasta", "deduplicated.fasta")
```

### Compute %N (ambiguous bases) per sequence
```python
fasta_tools.get_N_percent("example.fasta")
```
➡ Prints `sequence_ID percent_N` for each sequence.  

---

## Dependencies

- Python ≥ 3.6 (some functions also work on Python 2.7, but not recommended)  
- Standard library only (`sys`, `re`)  

---

## To Do / Known Issues

- ⚠️ `split_fasta` may write an extra sequence in the last file due to counter handling  
- Improve memory efficiency for very large FASTA files  

---
