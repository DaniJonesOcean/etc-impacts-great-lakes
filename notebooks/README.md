# Notebooks: ETC Impacts on the Great Lakes

This directory contains Jupyter notebooks used to generate the figures and processed data for the manuscript.

## Recommended execution order

1. `01_preprocess_data.ipynb`  
   Prepare and clean the storm datasets.

2. `02_build_gmm_model.ipynb`  
   Fit Gaussian mixture models and assign storm types (early-entry vs late-entry).  
   Outputs labeled dataset to `processed/`.

3. `03_analysis.ipynb`  
   Compute statistics and diagnostics (e.g. extremes, risk ratios).

4. `05_fig1_map.ipynb`  
   Generate Figure 1 (storm tracks and density overview).

5. `06_fig4_maps.ipynb`  
   Generate Figure 4 (genesis density maps by storm type and season).

## Supporting Information

Notebook 02 also generates supporting figures, including:
- Posterior probability distributions
- Clustering stability (ARI)
- t-SNE projection of storm classes

## Notes

- Figures are saved to the `figures/` directory as both PNG and PDF.
- Processed datasets are saved to the `processed/` directory.
- Some notebooks may be easier to run in Google Colab if Cartopy is not available locally.