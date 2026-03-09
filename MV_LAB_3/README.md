# MV_LAB_3 — Neural Networks & Unsupervised Learning

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange)](https://www.tensorflow.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-lightgrey)](https://scikit-learn.org/)

Part of the **B31MV Machine Vision** course at Heriot-Watt University.
This lab covers two complementary topics: supervised deep learning for action recognition, and classical unsupervised feature analysis with PCA and K-Means.

---

## Notebook: `MVLab3.ipynb`

The notebook is divided into two independent sections.

---

## Section 1 — Custom CNN on Stanford 40 Actions

### Dataset
- **Stanford 40 Actions** — a multi-class human action recognition dataset
- A 4-class subset was used for training efficiency: `applauding`, `cooking`, `drinking`, `reading`
- Images resized to **320 × 320**, split 80 / 20 train / validation
- Data augmentation applied during training (rescaling, random flips, shifts, shear, zoom)

### Model Architecture
A custom CNN was designed from scratch using the Keras Sequential API:

| Block | Layers | Filters | Dropout |
|-------|--------|---------|---------|
| Block 1 | Conv2D × 2 + BN + MaxPool | 32 | 0.25 |
| Block 2 | Conv2D × 2 + BN + MaxPool | 64 | 0.25 |
| Block 3 | Conv2D × 2 + BN + MaxPool | 128 | 0.25 |
| Block 4 | Conv2D × 2 + BN + MaxPool | 256 | 0.30 |
| Block 5 | Conv2D × 2 + BN + MaxPool | 512 | 0.30 |
| Head | Dense(128) → BN → Dense(64) → Softmax | — | 0.5 / 0.3 |

- **Optimizer:** Adam (lr = 0.0001)
- **Loss:** Categorical Cross-Entropy
- **Metrics:** Top-1 accuracy, Top-3 accuracy
- **Callbacks:** EarlyStopping, ReduceLROnPlateau, ModelCheckpoint

### Results

| Metric | Value |
|--------|-------|
| Validation Top-1 Accuracy | **23.94 %** |
| Validation Top-3 Accuracy | **73.71 %** |

Training converged in ~8 epochs before early stopping triggered. The gap between top-1 and top-3 accuracy suggests the model captures rough category similarity but struggles with fine-grained per-class discrimination — a common outcome on small subsets of action datasets with limited epochs.

### Outputs
- Model summary (layer-by-layer parameter count)
- Training history plots (accuracy and loss curves, train vs. validation)
- Confusion matrix (seaborn heatmap over all classes)
- Per-image prediction samples with true vs. predicted labels

---

## Section 2 — Unsupervised Learning: PCA + K-Means on Iris

### Dataset
- **Iris** dataset (sklearn built-in) — 150 samples, 4 features, 3 species

### Pipeline

1. **Standardisation** — `StandardScaler` to zero mean and unit variance
2. **PCA** — reduced to 2 principal components for 2D visualisation
3. **Elbow method** — inertia plotted for k = 1 … 10 to identify the optimal cluster count
4. **K-Means clustering** — k = 3 chosen from the elbow plot (matches the known 3 species)
5. **Cluster scatter plot** — PCA space coloured by predicted cluster label

### Outputs
- PCA 2D scatter (colour-coded by true species labels)
- Elbow curve (inertia vs. number of clusters)
- K-Means cluster scatter in PCA space

---

## Key Concepts

- Convolutional feature hierarchies (spatial filters at multiple scales)
- Batch normalisation for training stability
- Dropout regularisation to reduce overfitting
- Early stopping and learning rate scheduling
- Unsupervised dimensionality reduction with PCA
- Cluster validity assessment via the elbow method

---

## Dependencies

```
tensorflow / keras
opencv-python
scikit-learn
seaborn
pandas
matplotlib
tqdm
```
