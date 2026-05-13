# Bioinformatics Sequence Analysis Pipeline

A Python-based bioinformatics pipeline for open reading frame identification, DNA sequence translation, mutation analysis, and activity score calculation.

---

## Overview

This project was adapted and expanded from sequence analysis functionality I developed during an MSc Bioinformatics collaborative software development project focused on directed evolution monitoring.

The pipeline demonstrates practical computational biology workflows including open reading frame (ORF) detection, DNA-to-protein translation, mutation classification, comparative sequence analysis, and activity score calculation using biological experimental data.

The project was designed to support analysis of recombinant DNA polymerase variants generated during directed evolution experiments and demonstrates practical applications of computational biology within biological sequence analysis workflows.

---

## Features

- DNA sequence validation and preprocessing
- Six-frame ORF detection
- Circular plasmid sequence handling
- DNA to mRNA transcription
- DNA to protein translation
- Synonymous and non-synonymous mutation classification
- Mutation summary generation
- Comparative sequence analysis
- Activity score calculation using DNA and protein yield data

---

## Technologies Used

- Python
- Computational biology workflows
- Biological sequence analysis
- Mutation analysis pipelines
- GitHub
- FASTA-style sequence handling

---

## Project Structure

```text
bioinformatics-sequence-analysis-pipeline/
│
├── src/
│   ├── orf_finder.py
│   ├── mutation_tracker.py
│   └── activity_score.py
│
├── examples/
│   └── test_mutations.py
│
├── data/
│
├── README.md
│
└── requirements.txt
```

---

## Example Workflow

1. Input wild-type and variant DNA coding sequences
2. Translate DNA sequences into protein sequences
3. Compare codons between wild-type and variant sequences
4. Classify mutations as synonymous or non-synonymous
5. Calculate activity score from DNA and protein yield data
6. Generate structured mutation and activity summaries

---

## Example Output

```python
WT protein: MAAAAAFFFFF
VAR protein: MAAAAAFFFFY

Synonymous count: 1
Non-synonymous count: 1
Mutation count: 2

Mutation records:
{'position': 2, 'wt_residue': 'A', 'mutant_residue': 'A',
 'mutation_type': 'synonymous',
 'generation': 1,
 'codon_change': 'GCT->GCC'}

{'position': 11, 'wt_residue': 'F', 'mutant_residue': 'Y',
 'mutation_type': 'nonsynonymous',
 'generation': 1,
 'codon_change': 'TTC->TAC'}

Activity score results:
{
    'dna_norm': 1.2,
    'protein_norm': 1.0,
    'activity_score_raw': 1.2,
    'activity_score_log2': 0.263
}
```

---

## Biological Context

Directed evolution experiments generate large numbers of DNA and protein variants that require computational analysis to identify mutations and evaluate functional changes.

This pipeline demonstrates how computational approaches can be applied to:

- identify recombinant coding regions
- translate DNA sequences into proteins
- compare sequence variants
- classify mutation types
- integrate experimental yield data into quantitative activity metrics

The project highlights practical applications of computational biology within genomics and protein engineering workflows.

---

## Future Improvements

- Add FASTA file input support
- Add command-line interface
- Export mutation summaries as CSV
- Add mutation visualisation
- Improve automated testing
- Integrate sequence alignment functionality
- Add support for larger biological datasets
