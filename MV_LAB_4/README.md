# LAB4 — Stereo Camera Calibration

**Language:** Python (Jupyter Notebook)
**File:** `stereocam_calibraiton.ipynb`

---

## Overview

Implementation of **stereo camera calibration** using a physical checkerboard pattern. Calibration recovers the intrinsic parameters of each camera (focal length, principal point, lens distortion) and enables accurate metric measurements from images. This is a prerequisite step for any stereo vision, 3D reconstruction, or robotic perception system.

---

## Pipeline

```
Checkerboard images (multiple poses)
       │
       ▼ Corner detection (cv2.findChessboardCorners)
       │
       ▼ Sub-pixel refinement (cv2.cornerSubPix)
       │
       ▼ Camera calibration (cv2.calibrateCamera)
       │
       ├── Camera matrix K (focal length + principal point)
       └── Distortion coefficients (radial + tangential)
              │
              ▼ Image undistortion (cv2.undistort)
              │
              ▼ Object size estimation from calibrated images
```

---

## Concepts & Algorithms

### Checkerboard Calibration Pattern
- A planar checkerboard with known physical dimensions (8×6 inner corners, 25mm square size) provides 3D world coordinates
- Multiple images at different poses and orientations provide diverse viewpoints, improving calibration robustness
- Inner corner positions in 3D: `objp = [0,0,0], [25,0,0], [50,0,0], ...` (in mm)

### Corner Detection & Refinement
- **`cv2.findChessboardCorners`:** Detects the grid of inner corner positions in pixel coordinates
- **`cv2.cornerSubPix`:** Refines corner locations to sub-pixel accuracy using iterative local gradient optimisation — critical for accurate calibration

### Camera Matrix Estimation (`cv2.calibrateCamera`)
Solves for the **3×3 intrinsic matrix K**:
```
K = | fx   0   cx |
    |  0  fy   cy |
    |  0   0    1 |
```
- `fx`, `fy`: focal lengths in pixels (horizontal and vertical)
- `cx`, `cy`: principal point (optical centre, typically near image centre)
- Also estimates **distortion coefficients** `[k₁, k₂, p₁, p₂, k₃]` (radial and tangential)

### Lens Distortion Correction
- Real lenses introduce radial distortion (barrel/pincushion) and tangential distortion (lens-sensor misalignment)
- **`cv2.getOptimalNewCameraMatrix`** + **`cv2.undistort`** applies the inverse distortion model to produce geometrically correct images
- Undistorted images are required for accurate epipolar geometry computation in stereo pipelines

### Object Size Estimation
- Using the calibrated camera matrix, real-world object dimensions can be estimated from pixel measurements
- `pixel_per_mm = pixel_width / (num_squares × square_size_mm)` establishes the scale factor
- Demonstrates direct metric reconstruction from a single calibrated camera

---

## Key Takeaways

- Camera calibration is a prerequisite for any metric 3D reconstruction — the intrinsic matrix K is required to compute the essential matrix from the fundamental matrix (`E = K₂ᵀ F K₁`).
- Sub-pixel corner refinement is essential; even small errors in feature localisation propagate into calibration accuracy.
- The distortion model must be applied before any feature matching or stereo processing to ensure that the pinhole camera model holds.
- In robotic systems, calibration is performed periodically or on-the-fly to account for mechanical drift and thermal effects.
