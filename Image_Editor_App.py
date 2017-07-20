import cv2
import numpy as np

def dummy(val):
    pass

identity_kernel = np.array([
    [0,0,0],
    [0,1,0],
    [0,0,0]
])

edge_detect_kernel = np.array([
    [1,2,1],
    [0,0,0],
    [-1,-2,-1]
])

sharpen_kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

blur_kernel = cv2.getGaussianKernel(3, 0)

box_kernel = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
], np.float32) / 9

kernels = [identity_kernel, edge_detect_kernel, sharpen_kernel, blur_kernel, box_kernel]

color_original = cv2.imread(#insert image filepath here)
color_modified = color_original.copy()
gray_original = cv2.cvtColor(color_original, cv2.COLOR_BGR2GRAY)
gray_modified = gray_original.copy()

cv2.namedWindow('Image Editor App')
cv2.createTrackbar('Contrast', 'Image Editor App', 1, 100,dummy) # dummy function for callback
cv2.createTrackbar('Brightness', 'Image Editor App', 50, 100, dummy) #50 is start value to allow for darkening
cv2.createTrackbar('Filter', 'Image Editor App', 0, len(kernels) - 1, dummy)
cv2.createTrackbar('Grayscale', 'Image Editor App', 0, 1, dummy)

count = 1

while True:
    grayscale = cv2.getTrackbarPos('Grayscale', 'Image Editor App')
    if grayscale == 0:
        cv2.imshow('Image Editor App', color_modified)
    else:
        cv2.imshow('Image Editor App', gray_modified)
    key = cv2.waitKey(1) & 0xFF # Wait for a keypress at every clock
    if key == ord('q'):
        break
    elif key == ord('s'):
        if grayscale == 0:
            cv2.imwrite('output%d.jpg' % count, color_modified)
            count += 1
        else:
            cv2.imwrite('output%d.jpg' % count, gray_modified)
            count += 1
    contrast = cv2.getTrackbarPos('Contrast', 'Image Editor App')
    brightness = cv2.getTrackbarPos('Brightness', 'Image Editor App')
    kernel = cv2.getTrackbarPos('Filter', 'Image Editor App')


    color_modified = cv2.filter2D(color_original, -1, kernels[kernel])
    gray_modified = cv2.filter2D(gray_original, -1, kernels[kernel])

    color_modified = cv2.addWeighted(color_modified, contrast, np.zeros(color_original.shape, dtype = color_original.dtype), 0, (brightness - 50))
    gray_modified = cv2.addWeighted(gray_modified, contrast, np.zeros(gray_original.shape, dtype = gray_original.dtype), 0, (brightness - 50))


cv2.destroyAllWindows()
