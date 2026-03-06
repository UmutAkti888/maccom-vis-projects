# MV_LAB_5 — 3D Point Cloud Processing and ICP Registration

**Course:** B31MV Machine Vision · Heriot-Watt University · Spring 2025

---

## Topic

This lab covers the **3D reconstruction pipeline** using [Open3D](https://www.open3d.org/),
extended with **Iterative Closest Point (ICP) registration** — the algorithm used to align
overlapping point cloud scans in SLAM, Structure from Motion, and robotic mapping.

The test model is Open3D's built-in **Monkey (Suzanne)** mesh (`o3d.data.MonkeyModel`).

---

## Notebook Structure

### Part 1 — Mesh → Point Cloud Preprocessing
- Load the Monkey mesh and inspect its geometry
- Convert to a **50 k-point uniform cloud** via `sample_points_uniformly`
- Inject synthetic Gaussian noise + 500 hard outliers to simulate a real depth sensor
- **Statistical Outlier Removal (SOR)** — removes points whose mean neighbour distance
  exceeds `std_ratio × σ`
- **Voxel grid downsampling** — replaces all points in each spatial voxel with their
  centroid, enforcing uniform spatial coverage
- Sensitivity analysis: point count vs voxel size

### Part 2 — Normal Estimation and Poisson Reconstruction
- **Surface normal estimation** via PCA on local neighbourhoods (`KDTreeSearchParamHybrid`)
- `orient_normals_consistent_tangent_plane` — propagates consistent outward orientation
  through the neighbourhood graph
- **Poisson surface reconstruction** (`create_from_point_cloud_poisson`, depth = 9) —
  solves a global system to find the indicator function whose gradient matches the normals
- **Vertex density filtering** — removes low-density artefact vertices (10th percentile)
  that Poisson extrapolates into unsupported regions

### Part 3 — ICP Point Cloud Registration *(skeleton)*
- Two **partial overlapping scans** are simulated from the uniform cloud
- A known **25° rotation + translation** is applied to one scan to simulate misalignment
- The task is to recover the transformation using ICP:
  - `registration_icp` with `TransformationEstimationPointToPoint`
  - Evaluate via `fitness` score and `inlier_rmse`
  - Compare estimated vs ground-truth transformation (rotation error in degrees,
    translation error as L2 distance)
- Optional experiment: testing ICP with a larger (90°) initial misalignment to illustrate
  why global registration methods are needed as a prior step

---

## Why ICP for this Portfolio

ICP sits at the core of the dense reconstruction stage in **AI-enhanced SfM** pipelines:

```
Sparse SfM cloud  →  MVS densification  →  ICP registration  →  Poisson mesh
```

Aligning partial scans is the same problem whether the input comes from stereo cameras,
a depth sensor, or LiDAR — making it directly relevant to robotic perception and
3D mapping research.

---

## Dependencies

```
open3d
numpy
matplotlib
```

Install with:
```bash
pip install open3d numpy matplotlib
```
