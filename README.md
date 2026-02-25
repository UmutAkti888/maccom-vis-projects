# Machine & Computer Vision Portfolio

A collection of practical implementations covering the core pipeline of modern computer vision — from classical image processing and geometric reconstruction to deep feature learning. These projects were developed as part of the **B31MV Machine Vision** course at Heriot-Watt University (Spring 2025).

The topics covered align directly with the foundational components of **AI-enhanced Structure from Motion (SfM)** and robotic perception systems.

---

## Repository Structure

| Folder | Topic | Key Concepts |
|--------|-------|-------------|
| [`MacVis_HW1`](./MacVis_HW1) | Image Processing Fundamentals | Colour spaces, thresholding, affine transforms, filtering, edge detection |
| [`MacVis_HW2`](./MacVis_HW2) | Classical vs. Deep Feature Extraction | SIFT, Bag of Visual Words, SVM, CNN, ResNet-50, data augmentation |
| [`MacVis_HW3`](./MacVis_HW3) | Stereo 3D Reconstruction | Eight-point algorithm, epipolar geometry, essential matrix, triangulation, dense disparity |
| [`MV_LAB_2`](./MV_LAB_2) | BoVW Image Classification | SIFT, K-Means visual vocabulary, multi-classifier comparison |
| [`MV_LAB_4`](./MV_LAB_4) | Stereo Camera Calibration | Checkerboard calibration, camera matrix estimation, lens distortion correction |
| [`MV_LAB_6`](./MV_LAB_6) | Robust Estimation with RANSAC | RANSAC plane fitting, inlier/outlier separation, 3D point cloud |

---

## Core Vision Pipeline

These projects collectively cover the full geometric vision pipeline:

```
Image Formation          →  HW1 (colour spaces, filtering, transforms)
Feature Extraction        →  HW2, LAB2 (SIFT, BoVW, deep features)
Camera Calibration        →  LAB4 (intrinsics, distortion correction)
Geometric Reconstruction  →  HW3 (epipolar geometry, triangulation)
Robust Estimation         →  LAB6 (RANSAC for outlier rejection)
```

This pipeline forms the backbone of **Structure from Motion**, **stereo vision**, and **real-time robotic perception** — areas directly relevant to manipulation, navigation, and scene understanding in autonomous systems.

---

## Technologies

- **Python** — NumPy, OpenCV, scikit-learn, TensorFlow/Keras, SciPy, Matplotlib
- **MATLAB** — Image Processing Toolbox
- **Jupyter Notebooks** — interactive implementation with inline results

---

## Background

These implementations complement prior work in **visual servoing for underwater manipulation** and **LiDAR-based SLAM**, extending classical geometric vision towards learned feature representations for robotic applications.
