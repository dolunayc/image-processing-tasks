# image-processing-tasks

# Image Processing Tasks

This repository contains various image processing tasks implemented in Python. The scripts in this repository cover fundamental techniques such as filtering, edge detection, thresholding, and segmentation. Each script is self-contained and demonstrates a specific image processing technique.

## 📂 Folder Structure
```
py.codes/
├── adaptive_thresholding.py
├── canny_edge.py
├── connected_labeling.py
├── contours_detection.py
├── contrast_streching.py
├── edge_linking.py
├── global_thresholding.py
├── histogram_equalization.py
├── image_loading.py
├── image_segmentation.py
├── intensity_level_reduction.py
├── interpolation.py
├── linear_spatial_filter.py
├── local_thresholding.py
├── lowpass_gaussian.py
├── marrhildreth_Edge.py
├── median_filter.py
├── morphological_filtering.py
├── negative_image.py
├── nonlinear_filters.py
├── nonlinear_spatial_filter.py
├── quantization.py
├── spatial_resolution.py
├── thresholding.py
├── variable_thresholding.py
├── weighted_smoothing.py
```

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/dolunayc/image-processing-tasks.git
cd image-processing-tasks/py.codes
```

### 2️⃣ Install Dependencies
Make sure you have OpenCV and NumPy installed:
```sh
pip install opencv-python numpy
```

### 3️⃣ Run a Sample Script
To test one of the scripts, run:
```sh
python canny_edge.py
```

## 📜 Description of Scripts
- **Filtering Techniques**:
  - `lowpass_gaussian.py` - Applies Gaussian Low-Pass Filtering.
  - `median_filter.py` - Uses Median Filtering to reduce noise.
  - `weighted_smoothing.py` - Implements Weighted Smoothing Filters.
  
- **Edge Detection**:
  - `canny_edge.py` - Performs Canny Edge Detection.
  - `marrhildreth_Edge.py` - Uses Marr-Hildreth Edge Detection.
  - `edge_linking.py` - Implements edge linking algorithms.

- **Thresholding & Segmentation**:
  - `thresholding.py` - Basic thresholding technique.
  - `adaptive_thresholding.py` - Adaptive thresholding for different lighting conditions.
  - `global_thresholding.py` - Applies global thresholding.
  - `local_thresholding.py` - Implements local thresholding.
  - `variable_thresholding.py` - Variable thresholding for different image regions.
  - `image_segmentation.py` - Various segmentation techniques.

- **Image Transformations**:
  - `contrast_streching.py` - Enhances contrast.
  - `histogram_equalization.py` - Improves image contrast using histogram equalization.
  - `spatial_resolution.py` - Changes image spatial resolution.
  - `quantization.py` - Reduces color levels.
  - `interpolation.py` - Resizes images using interpolation methods.

- **Morphological Operations**:
  - `morphological_filtering.py` - Applies dilation and erosion for noise removal.
  - `connected_labeling.py` - Labels connected components in a binary image.

## 📝 Notes
- Each script is designed to be **standalone**, meaning you can run them independently.
- Ensure that you have the necessary image files if required by the scripts.

