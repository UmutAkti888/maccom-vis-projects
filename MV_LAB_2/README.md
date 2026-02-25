# LAB2 — Bag of Visual Words Image Classification

**Language:** Python (Jupyter Notebook)
**File:** `MVLab2.ipynb`
**Dataset:** Caltech-101 (4 categories: airplanes, motorbikes, faces, watches — 50 images each)

---

## Overview

A practical implementation of the **Bag of Visual Words (BoVW)** framework for multi-class image classification. BoVW is a classical computer vision technique that represents images as frequency histograms over a learned visual vocabulary of local features, enabling classification without deep learning. Multiple classifiers are evaluated against the same feature representation.

---

## Pipeline

```
Caltech-101 images
       │
       ▼ Grayscale + resize (150×150)
       │
       ▼ SIFT feature extraction (keypoints + 128-dim descriptors)
       │
       ▼ K-Means clustering → Visual vocabulary (visual words)
       │
       ▼ BoVW histogram encoding (per image)
       │
       ▼ Classification: SVM | Logistic Regression | Random Forest | KNN | MLP | CNN
```

---

## Concepts & Algorithms

### SIFT Feature Extraction
- **Scale-Invariant Feature Transform:** Detects interest points (corners, blobs) stable across scale and rotation changes
- Each keypoint produces a **128-dimensional descriptor** capturing local gradient orientation histograms
- Descriptors are robust to moderate illumination changes — key for real-world matching

### Visual Vocabulary (K-Means)
- All SIFT descriptors from the training set are pooled and clustered into **k visual words** using K-Means
- Each cluster centre is a **prototype descriptor** — a "visual word" representing a recurring local pattern (edge, corner type, texture element)
- The vocabulary size k is a key hyperparameter: larger k = finer vocabulary, but higher computational cost

### Bag of Visual Words Encoding
- Each image is encoded as a **normalised frequency histogram** over the k visual words
- Image representation is fixed-length regardless of the number of keypoints detected — enabling direct use with standard classifiers
- Analogous to the "bag of words" model in NLP

### Classifiers Evaluated
- **SVM** — effective with high-dimensional sparse feature vectors
- **Logistic Regression** — linear baseline
- **Random Forest** — ensemble of decision trees, robust to noise
- **K-Nearest Neighbours (KNN)** — instance-based, sensitive to feature scaling
- **MLP (Multi-Layer Perceptron)** — shallow neural network
- **CNN** — direct pixel-level learning for comparison

---

## Key Takeaways

- BoVW is a powerful mid-level representation that bridges raw pixel data and semantic classification — it remains relevant in resource-constrained or interpretability-focused systems.
- The choice of vocabulary size and SIFT parameters significantly impacts classification performance.
- BoVW loses spatial information (the histogram is orderless) — this limitation motivates spatial pyramid matching and, ultimately, convolutional feature learning.
