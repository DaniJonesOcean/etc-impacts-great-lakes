# src/gmm_utils.py

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.mixture import GaussianMixture
from sklearn.metrics import adjusted_rand_score
from scipy.optimize import linear_sum_assignment


def run_gmm_subsamples(X, k, n_subsamples=30, sample_frac=0.8):
    label_matrix = []
    posterior_matrix = []
    subsample_indices = []

    for _ in range(n_subsamples):
        sample_idx = np.random.choice(len(X), size=int(sample_frac * len(X)), replace=False)
        X_sample = X[sample_idx]

        gmm = GaussianMixture(n_components=k, covariance_type='full', random_state=42, n_init=5)
        gmm.fit(X_sample)
        labels = gmm.predict(X_sample)
        probs = gmm.predict_proba(X_sample)

        label_matrix.append(labels)
        posterior_matrix.append(probs.max(axis=1))
        subsample_indices.append(sample_idx)

    return label_matrix, posterior_matrix, subsample_indices


def match_labels(labels1, labels2, n_clusters):
    cost_matrix = np.zeros((n_clusters, n_clusters))
    for i in range(n_clusters):
        for j in range(n_clusters):
            cost_matrix[i, j] = -np.sum((labels1 == i) & (labels2 == j))
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    label_map = {j: i for i, j in zip(row_ind, col_ind)}
    matched = np.array([label_map[label] for label in labels2])
    return matched


def compute_matched_ari_scores(label_matrix, subsample_indices, k):
    mapped_ari_scores = []
    n_runs = len(label_matrix)

    for i in range(n_runs):
        for j in range(i + 1, n_runs):
            idx_i = subsample_indices[i]
            idx_j = subsample_indices[j]
            shared_idx = list(set(idx_i) & set(idx_j))
            if not shared_idx:
                continue

            idx_i_map = [idx_i.tolist().index(x) for x in shared_idx]
            idx_j_map = [idx_j.tolist().index(x) for x in shared_idx]

            labels_i = label_matrix[i][idx_i_map]
            labels_j = label_matrix[j][idx_j_map]
            labels_j_matched = match_labels(labels_i, labels_j, k)

            ari = adjusted_rand_score(labels_i, labels_j_matched)
            mapped_ari_scores.append(ari)

    return mapped_ari_scores


def plot_histogram(data, title, xlabel):
    plt.figure(figsize=(8, 4))
    sns.histplot(data, bins=30, kde=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.tight_layout()
    plt.show()
