import cv2
import os
import numpy as np


def rotate_image_180(image):
    return cv2.rotate(image, cv2.ROTATE_180)


def rotate_image_90(image):
    return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)


def rotate_image_270(image):
    return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)


def rotate_yolo_label_180(label, image_width, image_height):
    x_center, y_center, width, height = map(float, label.strip().split()[1:])
    x_center = 1 - x_center
    y_center = 1 - y_center
    return f"{label.split()[0]} {x_center} {y_center} {width} {height}"


def rotate_yolo_label_90(label, image_width, image_height):
    x_center, y_center, width, height = map(float, label.strip().split()[1:])
    new_x_center = 1 - y_center
    new_y_center = x_center
    new_width = height
    new_height = width
    return f"{label.split()[0]} {new_x_center} {new_y_center} {new_width} {new_height}"


def rotate_yolo_label_270(label, image_width, image_height):
    x_center, y_center, width, height = map(float, label.strip().split()[1:])
    new_x_center = y_center
    new_y_center = 1 - x_center
    new_width = height
    new_height = width
    return f"{label.split()[0]} {new_x_center} {new_y_center} {new_width} {new_height}"


input_folder = "input"
output_folder = "output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    name, ext = os.path.splitext(filename)

    if ext.lower() == ".png":
        image_path = os.path.join(input_folder, filename)
        label_path = os.path.join(input_folder, f"{name}.txt")

        # Read image and rotate
        image = cv2.imread(image_path)
        rotated_image = rotate_image_270(image)

        # Read label and rotate
        with open(label_path, "r") as f:
            labels = f.readlines()

        rotated_labels = [rotate_yolo_label_270(label, image.shape[1], image.shape[0]) for label in labels]

        # Save rotated image and label
        cv2.imwrite(os.path.join(output_folder, f"{name}_270.png"), rotated_image)

        with open(os.path.join(output_folder, f"{name}_270.txt"), "w") as f:
            f.writelines("\n".join(rotated_labels))
