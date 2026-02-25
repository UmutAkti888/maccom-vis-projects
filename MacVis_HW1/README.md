# HW1 — Image Processing Fundamentals

**Language:** MATLAB
**File:** `UAkti_MacVisionHW1_FINAL.m`

---

## Overview

Foundational image processing operations applied to real images, covering colour space transformations, geometric transforms, spatial filtering, and edge detection. This work establishes the low-level building blocks that underpin all higher-level computer vision pipelines.

---

## Concepts & Algorithms

### Part A — Colour & Intensity Processing
- **Colour space conversion:** RGB → Grayscale (`rgb2gray`), RGB → HSV (`rgb2hsv`)
- **Thresholding / Binarization:** Applied at multiple intensity levels (128, 180, 256) to examine the effect of threshold choice on binary segmentation
- **Intensity quantisation:** Bit-depth reduction across power-of-2 levels (255 → 4) to observe information loss

### Part B — Geometric Transformations
- **Translation:** Constructed via affine transformation matrix using `affine2d` + `imwarp`
- **Rotation:** Applied at 45° and 60° using `imrotate`, comparing the effect of rotation angle on content preservation

### Part C — Spatial Filtering & Edge Detection
- **Mean filter (5×5):** Uniform blur via `fspecial('average')` + `imfilter`
- **Gaussian blur (σ=2):** Weighted smoothing via `imgaussfilt`, preserving edges better than mean filtering
- **Canny edge detection:** Applied with two threshold pairs ([0.1, 0.3] and [0.2, 0.4]) to compare sensitivity — lower thresholds detect finer edges, higher thresholds retain only strong boundaries

### Part D — Histogram Equalisation
- **`histeq`:** Redistributes pixel intensities to maximise contrast, particularly effective for images with uneven illumination

---

## Key Takeaways

- Affine transforms (translation, rotation) are linear operations representable as matrix multiplications — the foundation of homography and camera pose estimation.
- Gaussian filtering is a separable convolution; understanding this is critical for scale-space theory used in SIFT and similar detectors.
- Canny edge detection combines Gaussian smoothing with gradient thresholding and non-maximum suppression — a core component in feature extraction pipelines.
