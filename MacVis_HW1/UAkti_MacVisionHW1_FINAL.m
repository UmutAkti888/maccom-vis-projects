%% Assignment 1 - Image Processing
% ******** Umut Akti ********
% Part A: Image Loading and Basic Processing 
% Using "gigachad.jpg" for all processing methods. Because why not?

% Load Image (At the Beginning)
img = imread('gigachad.jpg'); % Loading the original image
figure;
imshow (img);

%% Q1: Image Loading and Conversion
figure;
subplot(1,3,1), imshow(img), title('Q1 - Gigachad - Original Image');
gray_img = rgb2gray(img);
subplot(1,3,2), imshow(gray_img), title('Grayscale');
hsv_img = rgb2hsv(img);
subplot(1,3,3), imshow(hsv_img), title('HSV');

% Binarization with 3 thresholds (128, 256, and an adjusted one)
thresholds = [128, 256, 180]; % 256 and 180 were added for comparison. 
figure;
for i = 1:length(thresholds)
    threshold = thresholds(i);
    binary_img = gray_img > threshold;
    subplot(1,3,i), imshow(binary_img), title(['Gigachad - Binary ', num2str(threshold)]);
end
% Why these values?  
% - 128: Middle of intensity range (classic choice).  
% - 256: Max value (should be almost all black).  
% - 180: A mid-high threshold to observe effects.
% Thanks to ChatGPT for this crazy for loop trick applied for naming the
% plots.

%% Q2: Geometric Transformations
% Translation (tx = 50, ty = 30)
tx = 50; ty = 30;
T = [1 0 0; 0 1 0; tx ty 1]; %Transfrom matrix defined.
tform = affine2d(T); % affine2d(T) creates an affine transformation object
% based on matrix T, which defines linear geometric transformations such as
% scaling, rotation, translation, and shearing.
translated_img = imwarp(img, tform, 'OutputView', imref2d(size(img)));

% Rotation (45 and 60 degrees)
rotated_img45 = imrotate(img, 45);
rotated_img60 = imrotate(img, 60);

% Display Transformations Comparatively
figure;
subplot(1,3,1), imshow(img), title('Q2 - Gigachad - Original');
subplot(1,3,2), imshow(translated_img), title('Translated');
subplot(1,3,3), imshow(rotated_img45), title('Rotated 45°');

figure;
subplot(1,2,1), imshow(rotated_img45), title('Q2 - Gigachad - Rotated 45°');
subplot(1,2,2), imshow(rotated_img60), title('Gigachad - Rotated 60°');
% Why 45° and 60°?
% - 45°: Common rotation for analysis.
% - 60°: Chosen to compare an additional significant rotation.

%% Q3: Smoothing Filters and Edge Detection
% Mean Filter (Smoothing) vs Gaussian Filter
kernel = fspecial('average', [5 5]);  
mean_filtered_img = imfilter(img, kernel);
gaussian_filtered_img = imgaussfilt(img, 2);

% Display both filters together
figure;
subplot(1,3,1), imshow(img), title('Q3 - Gigachad - Original');
subplot(1,3,2), imshow(mean_filtered_img), title('Mean Filter');
subplot(1,3,3), imshow(gaussian_filtered_img), title('Gaussian Blur');
% Why kernel size 5x5?
% - Small enough to smooth, large enough to notice effects.

% Canny Edge Detection - Comparing Two Different Sigma Values
edges1 = edge(gray_img, 'Canny', [0.1 0.3], 'both'); % Default Canny
edges2 = edge(gray_img, 'Canny', [0.2 0.4], 'both'); % Higher thresholds

figure;
subplot(1,2,1), imshow(edges1), title('Q3 - Canny Edges (Low Thresholds)');
subplot(1,2,2), imshow(edges2), title('Canny Edges (High Thresholds)');
% Why compare two different threshold values?
% - Lower values ([0.1 0.3]) detect finer edges.
% - Higher values ([0.2 0.4]) remove weaker edges and retain only strong ones.

%% Part B: Image Analysis Using Peppers.png
% Load and Display Peppers Image
peppers_img = imread('peppers.png');
gray_peppers = rgb2gray(peppers_img);

% Show Original and Grayscale Side by Side
figure;
subplot(1,2,1), imshow(peppers_img), title('Q4 - Peppers - Original Image');
subplot(1,2,2), imshow(gray_peppers), title('Peppers - Grayscale');

% Reduce Intensity Range Comparatively
N_values = [255, 128, 64, 32, 16, 8, 4]; % Added 4 for extreme comparison
figure;
for i = 1:length(N_values)
    N = N_values(i);
    reduced_img = uint8(double(gray_peppers) / 255 * N);
    subplot(2,4,i), imshow(reduced_img), title(['Q4 - Intensity ', num2str(N)]);
end
% Why these values?
% - Power of 2 values ensure structured bit-depth reduction.
% - 4 added to show extreme information loss.

% Apply Histogram Equalization
equalized_img = histeq(gray_peppers);
figure, imshow(equalized_img), title('Q4 - Peppers - Histogram Equalized');
% Why histogram equalization?
% - Enhances contrast by redistributing pixel intensity values.
% - Makes dark areas brighter and bright areas darker for better visibility.
% - Useful for images with uneven lighting or low contrast.
% - Robust and reliable method for improving image clarity.
