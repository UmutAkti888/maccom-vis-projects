# LAB6 — Robust Estimation with RANSAC

**Language:** Python (Jupyter Notebook)
**File:** `MVLab6_3DReconstr.ipynb`

---

## Overview

Implementation of **RANSAC (Random Sample Consensus)** for robust 3D plane fitting in the presence of outliers. RANSAC is a fundamental algorithm in computer vision used wherever geometric model fitting must be resilient to noisy or incorrect data — including feature matching, homography estimation, fundamental matrix computation, and point cloud segmentation.

---

## Pipeline

```
Synthetic 3D point cloud (2500 inliers + 1200 outliers)
       │
       ▼ Random sampling of 3 points → candidate plane
       │
       ▼ Plane normal via cross product
       │
       ▼ Point-to-plane distance for all points
       │
       ▼ Inlier count at threshold
       │
       ▼ Repeat for max_iterations → keep best model
       │
       ▼ Final plane + inlier/outlier classification → 3D visualisation
```

---

## Concepts & Algorithms

### RANSAC (Random Sample Consensus)
A probabilistic, iterative algorithm for fitting geometric models to datasets with a high proportion of outliers:

1. **Random sampling:** Randomly select the minimum number of points to define the model (3 points for a plane)
2. **Model hypothesis:** Compute the candidate plane from the sampled points
3. **Consensus evaluation:** Count all points within a distance threshold `ε` of the plane — these are **inliers**
4. **Best model selection:** After `N` iterations, retain the hypothesis with the most inliers
5. **Optional refinement:** Refit the model using all inliers for improved precision

### Plane Estimation from 3 Points
- **Cross product** of two edge vectors gives the plane normal: `n = (p₂ - p₁) × (p₃ - p₁)`
- Plane equation: `ax + by + cz + d = 0`, where `[a,b,c] = n̂` (normalised) and `d = -n̂ · p₁`
- **Point-to-plane distance:** `dist = |ax + by + cz + d| / ||n||`

### Synthetic Data Generation
- **Inliers:** Points sampled near the ground-truth plane `0.2x - 0.3y + z - 5 = 0` with Gaussian noise (σ = 0.05)
- **Outliers:** Points at random heights, uniformly distributed in 3D space
- Dataset: 2500 inliers + 1200 outliers (≈32% outlier rate)

### Visualisation
- Inliers rendered in **blue**, outliers in **red**, fitted plane as a **green surface**
- Demonstrates the algorithm's ability to recover the correct model despite a high outlier fraction

---

## Key Takeaways

- RANSAC's robustness comes from its probabilistic sampling strategy — even with many outliers, the probability of sampling only inliers across multiple iterations is high enough to find the correct model.
- The number of iterations required scales with the outlier ratio and minimum sample size: `N = log(1 - p) / log(1 - (1 - ε)ˢ)` where p is desired confidence, ε is outlier ratio, and s is sample size.
- In SfM pipelines, RANSAC is applied during feature matching (to reject false correspondences) and during fundamental/essential matrix estimation — making it indispensable for any real-world geometric reconstruction system.
- The same principle extends to homography estimation, point cloud plane segmentation, and loop closure detection in SLAM.
