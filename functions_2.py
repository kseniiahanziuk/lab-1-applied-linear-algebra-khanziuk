import cv2
import numpy as np
import matplotlib.pyplot as plt


def command_prompt_2():
    print("Choose the option: \n"
          "0) Help.\n"
          "1) Show images without transformations.\n"
          "2) Rotation.\n"
          "3) Scaling.\n"
          "4) Reflecting.\n"
          "5) Shearing.\n"
          "6) Custom transformation.\n"
          "7) Exit.\n")


def plotting_image(image, title):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()


def rotating_image(image, angle):
    height, width = image.shape[:2]
    centre = (width / 2, height / 2)
    rotation_matrix = cv2.getRotationMatrix2D(centre, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image


def scaling_image(image, c):
    scaled_image = cv2.resize(image, None, fx=c, fy=c)
    return scaled_image


def reflecting_image(image, axis):
    if axis == "x":
        reflected_image = cv2.flip(image, 0)
    elif axis == "y":
        reflected_image = cv2.flip(image, 1)
    return reflected_image


def shearing_image(image, axis, angle):
    radians_angle = np.radians(angle)
    if axis == "x":
        shearing_matrix = np.float32([[1, radians_angle, 0], [0, 1, 0]])
    elif axis == "y":
        shearing_matrix = np.float32([[1, 0, 0], [radians_angle, 1, 0]])
    height, width = image.shape[:2]
    sheared_image = cv2.warpAffine(image, shearing_matrix, (width, height))
    return sheared_image


image_doggo = cv2.imread('borzoi.jpeg')