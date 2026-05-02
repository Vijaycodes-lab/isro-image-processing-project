import cv2
import numpy as np

img = cv2.imread('image.jpg')

if img is None:
    print("Error: Image not loaded")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ✅ ADD HERE
    blur = cv2.GaussianBlur(img, (5,5), 0)

    edges = cv2.Canny(img, 100, 200)

    # Show all images
    cv2.imshow('Original Image', img)
    cv2.imshow('Grayscale Image', gray)
    cv2.imshow('Blur Image', blur)
    cv2.imshow('Edges', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()