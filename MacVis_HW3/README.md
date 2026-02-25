# HW3 — Stereo 3D Reconstruction

**Language:** Python (Jupyter Notebook)
**File:** `UA_MVHW3.ipynb`
**Dataset:** Temple stereo image pair (`im1.png`, `im2.png`) with pre-computed correspondences and camera intrinsics

---

## Overview

A full implementation of the stereo 3D reconstruction pipeline, covering both **sparse reconstruction** (feature-based, from matched keypoints) and **dense reconstruction** (pixel-wise, via disparity and depth maps). This is the core geometric vision pipeline underpinning Structure from Motion (SfM) systems.

---

## Pipeline

```
Stereo image pair
       │
       ▼
Section 1 — Sparse Reconstruction
  ├── Eight-Point Algorithm  →  Fundamental Matrix (F)
  ├── Epipolar Correspondences  →  Matched point pairs along epipolar lines
  ├── Essential Matrix (E = K₂ᵀ F K₁)
  ├── E decomposition  →  4 candidate (R, t) solutions
  ├── Cheirality check  →  Select correct camera pose
  └── Triangulation  →  Sparse 3D point cloud + reprojection error

       │
       ▼
Section 2 — Dense Reconstruction
  ├── Stereo rectification  →  Align epipolar lines horizontally
  ├── Block matching (SSD)  →  Per-pixel disparity map
  └── Depth map  →  depth = (f × baseline) / disparity  →  Dense 3D point cloud
```

---

## Concepts & Algorithms

### Eight-Point Algorithm
Estimates the **Fundamental Matrix F** from N ≥ 8 point correspondences:
1. Normalise point coordinates by scale factor M (max image dimension)
2. Construct matrix A where each row encodes one correspondence: `[x₂x₁, x₂y₁, x₂, y₂x₁, y₂y₁, y₂, x₁, y₁, 1]`
3. Solve **Af = 0** via SVD — solution is the last row of Vᵀ
4. Enforce **rank-2 constraint** on F by zeroing the smallest singular value
5. Unnormalise F back to pixel coordinates

### Epipolar Geometry & Correspondences
- Each point p₁ in image 1 defines an **epipolar line** l = F·p₁ in image 2
- Correspondences are found by searching along epipolar lines using **SSD patch matching** within a bounded horizontal range
- The constraint `p₂ᵀ F p₁ = 0` is used to verify geometric consistency

### Essential Matrix & Camera Pose Recovery
- **E = K₂ᵀ · F · K₁** incorporates camera intrinsics (focal length, principal point) to encode pure rotation and translation
- E is decomposed via SVD using rotation matrix W to yield **4 candidate (R, t)** pairs
- Correct pose selected by **cheirality check**: triangulate a subset of points and choose the (R, t) for which the most 3D points have positive depth (z > 0) in both camera frames

### Triangulation
For each matched pair (p₁, p₂), a 4×4 linear system is formed from the projection equations:
```
A[0] = y₁·P₁[2] - P₁[1]
A[1] = x₁·P₁[2] - P₁[0]
A[2] = y₂·P₂[2] - P₂[1]
A[3] = x₂·P₂[2] - P₂[0]
```
Solved via SVD; the 3D point is the last row of Vᵀ, dehomogenised.

**Reprojection error** is computed to verify reconstruction quality.

### Dense Reconstruction
- **Rectification:** Images warped so epipolar lines become horizontal rows, reducing stereo matching to a 1D search (`cv2.stereoRectify`)
- **Disparity map:** For each pixel in the left image, SSD block matching finds the horizontal shift (disparity) to the best match in the right image
- **Depth map:** `depth = (f × baseline) / disparity`, where baseline = distance between camera centres

---

## Key Takeaways

- The fundamental matrix F captures the epipolar geometry between two views without requiring camera intrinsics — making it applicable even with uncalibrated cameras.
- The essential matrix E is the calibrated counterpart; decomposing it gives the relative camera pose, which is the central step in any SfM pipeline.
- Sparse reconstruction is fast and precise at feature-rich locations; dense reconstruction provides complete surface coverage at higher computational cost.
- The full pipeline (F → E → pose → triangulation → depth) is the basis of modern SfM systems such as COLMAP and ORB-SLAM.
