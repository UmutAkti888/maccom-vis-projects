# HW2 — Classical vs. Deep Feature Extraction for Image Classification

**Language:** Python (Jupyter Notebook)
**File:** `UA_MVHW2.ipynb`
**Dataset:** CIFAR-10 (60,000 32×32 colour images, 10 classes)

---

## Overview

A systematic comparison of classical computer vision and deep learning approaches for image classification. The pipeline progresses from handcrafted feature extraction (SIFT + Bag of Visual Words + SVM) through a custom CNN to a pretrained ResNet-50, with data augmentation applied at each stage.

---

## Pipeline

```
CIFAR-10 → Grayscale → SIFT descriptors → K-Means (BoVW) → SVM classifier
                                                          → (after augmentation) SVM again
         → Grayscale → Custom CNN (10 epochs)
         → RGB       → ResNet-50 (ImageNet pretrained, fine-tuned, 10 epochs)
```

---

## Concepts & Algorithms

### Classical Approach — SIFT + BoVW + SVM
- **SIFT (Scale-Invariant Feature Transform):** Detects keypoints robust to scale, rotation, and illumination changes; computes 128-dim descriptors per keypoint
- **K-Means clustering (k=100):** Groups all training descriptors into a visual vocabulary of 100 "visual words"
- **Bag of Visual Words (BoVW):** Encodes each image as a frequency histogram over the visual vocabulary — analogous to word frequency in text classification
- **SVM (linear kernel):** Trained on BoVW histograms for 10-class classification

**Result:** 25.79% accuracy — limited by SIFT's inability to capture spatial relationships and the low resolution of CIFAR-10 images

### Deep Learning — Custom CNN
- Architecture: `Conv2D(32) → MaxPool → Conv2D(64) → MaxPool → Dense(128) → Dropout(0.5) → Softmax(10)`
- Optimizer: Adam | Loss: Sparse categorical cross-entropy | Epochs: 10

**Result:** 66.95% — convolutional layers learn spatial hierarchies directly, removing the need for handcrafted features

### Transfer Learning — ResNet-50
- Pretrained on ImageNet; top layers replaced with `GlobalAveragePooling → Dense(128) → Dropout → Softmax(10)`
- Fine-tuned on CIFAR-10 RGB images

**Result:** 77.10% — residual connections enable deeper feature extraction without gradient degradation

### Data Augmentation
- Applied: rotation (±20°), width/height shift (20%), shear, zoom (20%), horizontal flip
- Effect on SVM: marginal accuracy drop (25.79% → 24.98%) — augmentation hurts BoVW because SIFT keypoint distributions shift, introducing feature noise rather than diversity

---

## Results Summary

| Method | Accuracy |
|--------|----------|
| SIFT + BoVW + SVM | 25.79% |
| SIFT + BoVW + SVM (augmented) | 24.98% |
| Custom CNN | 66.95% |
| ResNet-50 (fine-tuned) | **77.10%** |

---

## Key Takeaways

- Classical feature descriptors like SIFT remain relevant for structured geometric tasks (matching, reconstruction) but underperform on unstructured classification at low resolution.
- Deep networks learn task-specific features end-to-end, outperforming handcrafted pipelines significantly.
- Data augmentation benefits deep models more than classical ones — a critical consideration when building hybrid learned-feature pipelines for SfM.
