"""
hw1_companion.py — Python equivalent of UAkti_MacVisionHW1_FINAL.m
===================================================================
Replicates all HW1 image processing operations using Python libraries.
Built-in skimage test images replace the original files so the script
runs without any external assets.

MATLAB → Python library map
───────────────────────────
imread / imshow              →  skimage.io / matplotlib
rgb2gray                     →  skimage.color.rgb2gray
rgb2hsv                      →  skimage.color.rgb2hsv
affine2d + imwarp            →  skimage.transform.AffineTransform + warp
imrotate                     →  skimage.transform.rotate
fspecial('average') + imfilter →  scipy.ndimage.uniform_filter
imgaussfilt                  →  skimage.filters.gaussian
edge(…, 'Canny')             →  skimage.feature.canny
histeq                       →  skimage.exposure.equalize_hist
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import data, color, filters, feature, exposure, transform
from scipy.ndimage import uniform_filter

# ─────────────────────────────────────────────────────────────────────────────
# PART A — Image Loading and Basic Processing
# MATLAB used 'gigachad.jpg'; skimage's astronaut image is used here instead.
# ─────────────────────────────────────────────────────────────────────────────

img  = data.astronaut()          # uint8 RGB, 512×512
gray = color.rgb2gray(img)       # float64, range [0, 1]

# ── Q1: Colour Space Conversion ──────────────────────────────────────────────
# MATLAB: rgb2gray(img), rgb2hsv(img)
hsv = color.rgb2hsv(img)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
axes[0].imshow(img);               axes[0].set_title('Original (RGB)');  axes[0].axis('off')
axes[1].imshow(gray, cmap='gray'); axes[1].set_title('Grayscale');        axes[1].axis('off')
axes[2].imshow(hsv);               axes[2].set_title('HSV');              axes[2].axis('off')
plt.suptitle('Q1 — Colour Space Conversion', fontsize=13)
plt.tight_layout()
plt.show()

# ── Q1: Binarisation — three threshold values ────────────────────────────────
# MATLAB: binary_img = gray_img > threshold  (threshold in 0–255 range)
# Python: gray is in [0, 1], so divide threshold by 255.
thresholds = [128, 180, 220]   # same rationale as MATLAB: mid, mid-high, high

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
for ax, t in zip(axes, thresholds):
    binary = gray > (t / 255.0)
    ax.imshow(binary, cmap='gray')
    ax.set_title(f'Threshold = {t}')
    ax.axis('off')
plt.suptitle('Q1 — Binarisation (three thresholds)', fontsize=13)
plt.tight_layout()
plt.show()

# ── Q2: Geometric Transformations ────────────────────────────────────────────
# Translation
# MATLAB: T = [1 0 0; 0 1 0; tx ty 1]; tform = affine2d(T); imwarp(img, tform)
tx, ty = 50, 30
# skimage.transform.warp uses inverse mapping, so translation is negated.
tform_translate = transform.AffineTransform(translation=(-tx, -ty))
img_translated  = transform.warp(img, tform_translate, preserve_range=True).astype(np.uint8)

# Rotation
# MATLAB: imrotate(img, 45), imrotate(img, 60)
img_rot45 = transform.rotate(img, 45, preserve_range=True).astype(np.uint8)
img_rot60 = transform.rotate(img, 60, preserve_range=True).astype(np.uint8)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
axes[0].imshow(img);            axes[0].set_title('Original');          axes[0].axis('off')
axes[1].imshow(img_translated); axes[1].set_title('Translated (50,30)');axes[1].axis('off')
axes[2].imshow(img_rot45);      axes[2].set_title('Rotated 45°');       axes[2].axis('off')
plt.suptitle('Q2 — Geometric Transformations', fontsize=13)
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].imshow(img_rot45); axes[0].set_title('Rotated 45°'); axes[0].axis('off')
axes[1].imshow(img_rot60); axes[1].set_title('Rotated 60°'); axes[1].axis('off')
plt.suptitle('Q2 — Rotation Comparison', fontsize=13)
plt.tight_layout()
plt.show()

# ── Q3: Smoothing Filters ─────────────────────────────────────────────────────
# Mean filter
# MATLAB: kernel = fspecial('average', [5 5]); imfilter(img, kernel)
img_mean = uniform_filter(img.astype(float), size=[5, 5, 1]).astype(np.uint8)

# Gaussian filter
# MATLAB: imgaussfilt(img, 2)
img_gauss = (filters.gaussian(img, sigma=2, channel_axis=-1) * 255).astype(np.uint8)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
axes[0].imshow(img);       axes[0].set_title('Original');           axes[0].axis('off')
axes[1].imshow(img_mean);  axes[1].set_title('Mean Filter (5×5)');  axes[1].axis('off')
axes[2].imshow(img_gauss); axes[2].set_title('Gaussian (σ=2)');     axes[2].axis('off')
plt.suptitle('Q3 — Smoothing Filters', fontsize=13)
plt.tight_layout()
plt.show()

# ── Q3: Canny Edge Detection ─────────────────────────────────────────────────
# MATLAB: edge(gray_img, 'Canny', [0.1 0.3]), edge(gray_img, 'Canny', [0.2 0.4])
edges_low  = feature.canny(gray, sigma=1, low_threshold=0.05, high_threshold=0.15)
edges_high = feature.canny(gray, sigma=1, low_threshold=0.10, high_threshold=0.25)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].imshow(edges_low,  cmap='gray'); axes[0].set_title('Canny — low thresholds');  axes[0].axis('off')
axes[1].imshow(edges_high, cmap='gray'); axes[1].set_title('Canny — high thresholds'); axes[1].axis('off')
plt.suptitle('Q3 — Canny Edge Detection', fontsize=13)
plt.tight_layout()
plt.show()

# ─────────────────────────────────────────────────────────────────────────────
# PART B — Image Analysis
# MATLAB used 'peppers.png'; skimage's coffee image is used here.
# ─────────────────────────────────────────────────────────────────────────────

peppers = data.coffee()              # uint8 RGB — similar colourful test image
gray_p  = color.rgb2gray(peppers)    # float64 [0, 1]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].imshow(peppers);             axes[0].set_title('Original'); axes[0].axis('off')
axes[1].imshow(gray_p, cmap='gray'); axes[1].set_title('Grayscale'); axes[1].axis('off')
plt.suptitle('Q4 — Part B Image', fontsize=13)
plt.tight_layout()
plt.show()

# ── Q4: Intensity Range Reduction ────────────────────────────────────────────
# MATLAB: uint8(double(gray_peppers) / 255 * N)
N_values = [255, 128, 64, 32, 16, 8, 4]

fig, axes = plt.subplots(2, 4, figsize=(16, 7))
for ax, N in zip(axes.flat, N_values):
    reduced = (gray_p * N).astype(np.uint8)
    ax.imshow(reduced, cmap='gray', vmin=0, vmax=N)
    ax.set_title(f'N = {N}')
    ax.axis('off')
axes.flat[-1].axis('off')   # hide unused subplot
plt.suptitle('Q4 — Intensity Range Reduction', fontsize=13)
plt.tight_layout()
plt.show()

# ── Q4: Histogram Equalisation ───────────────────────────────────────────────
# MATLAB: histeq(gray_peppers)
eq = exposure.equalize_hist(gray_p)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].imshow(gray_p, cmap='gray'); axes[0].set_title('Before equalisation'); axes[0].axis('off')
axes[1].imshow(eq,     cmap='gray'); axes[1].set_title('After equalisation');  axes[1].axis('off')
plt.suptitle('Q4 — Histogram Equalisation', fontsize=13)
plt.tight_layout()
plt.show()

# Histogram comparison — shows the redistribution effect
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].hist(gray_p.ravel(), bins=256, color='steelblue', alpha=0.85)
axes[0].set_title('Histogram — Original'); axes[0].set_xlabel('Intensity')
axes[1].hist(eq.ravel(),     bins=256, color='seagreen',  alpha=0.85)
axes[1].set_title('Histogram — Equalised'); axes[1].set_xlabel('Intensity')
plt.suptitle('Q4 — Histogram Comparison', fontsize=13)
plt.tight_layout()
plt.show()

print("All operations completed.")
