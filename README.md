# ETC Impacts in the Great Lakes

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19559385-blue)](https://doi.org/10.5281/zenodo.19559385)
[![License: GPL v3](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Status](https://img.shields.io/badge/status-research%20code-blue.svg)

Unsupervised classification of extratropical cyclones reveals differences in precipitation and evaporation impacts across the Great Lakes.

This repository contains the data processing, clustering, and analysis pipeline used to identify classes of extratropical cyclones (ETCs) and quantify their impacts on the Great Lakes.

The analysis applies unsupervised learning (Gaussian Mixture Models) to storm characteristics and evaluates differences in precipitation and evaporation impacts across storm types.

---

## Repository structure

```text
.
├── data/            # Raw or lightly processed input data
├── processed/       # Derived datasets and model artifacts
├── figures/         # Generated figures (PNG and PDF)
├── notebooks/       # Analysis and figure-generation notebooks
├── src/             # Reusable pipeline and modeling utilities
└── environment.yml  # Conda environment specification
```

---

## Reproducing the analysis

### 1. Create the environment

```bash
conda env create -f environment.yml
conda activate etc-paper
```

### 2. Run notebooks (in order)

See `notebooks/README.md` for details. In brief:

1. `01_exploratory_analysis.ipynb`
2. `02_build_gmm_model.ipynb`
3. `03_impact_analysis.ipynb`
4. `04_generate_figures.ipynb`
5. `05_fig1_map.ipynb`
6. `06_fig4_maps.ipynb`

Outputs will be written to:
- `processed/` for data products and model artifacts
- `figures/` for publication and supporting-information figures

---

## Key outputs

### Clustered storm datasets
- `processed/cfsr_storms_labeled_k2.csv`
- `processed/era5_storms_labeled_k2.csv`

### Risk metrics
- `processed/rr_df_all_seasons.csv`
- `processed/rr_df_by_season.csv`

### Figures
Generated in `figures/` as both PNG and PDF files.

---

## Storm classification

Storms are grouped into two classes based on clustering of dynamical characteristics:

- **Early-entry storms**
- **Late-entry storms**

These classes exhibit systematically different spatial and seasonal impact patterns over the Great Lakes.

---

## Supporting Information

Additional diagnostics and robustness checks are generated in the notebooks, including:

- posterior probability distributions
- clustering stability (Adjusted Rand Index)
- t-SNE projections of storm classes

These figures are saved in the `figures/` directory.

---

## Notes

- Cartopy may download Natural Earth shapefiles on first use.
- Some notebooks may be easier to run in Google Colab if local Cartopy installation is difficult.
- Processed data products are included to facilitate reproducibility without re-running all steps.

---

## License

This repository is released under the terms of the license provided in `LICENSE`.

---

## Contact

Dani Jones  
Cooperative Institute for Great Lakes Research (CIGLR)  
University of Michigan

---

## Citation

If you use this repository, please cite:

Jones, D. et al. (2026). *ETC impacts in the Great Lakes*. Zenodo. https://doi.org/10.5281/zenodo.19559385