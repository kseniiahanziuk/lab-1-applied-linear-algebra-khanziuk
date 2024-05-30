import numpy as np
import matplotlib.pyplot as plt


def plotting_objects(object, name):
    plt.figure()
    plt.plot(object[:, 0], object[:, 1])
    plt.axis('equal')
    plt.grid(True)
    plt.title(name)
    plt.show()


def rotate_objects(object, angle):
    radians_angle = np.radians(angle)
    rotation_matrix = np.array([[np.cos(radians_angle), -np.sin(radians_angle)], [np.sin(radians_angle), np.cos(radians_angle)]])
    rotated_object = np.dot(object, rotation_matrix)
    return rotated_object


def scaling_object(object, c):
    scaled_object = object * c
    return scaled_object


def reflecting_object(object, axis):
    if axis == 'x':
        reflection_matrix = np.array([[1, 0], [0, -1]])
    elif axis == 'y':
        reflection_matrix = np.array([[-1, 0], [0, 1]])
    reflected_object = np.dot(object, reflection_matrix)
    return reflected_object


def shearing_axis(object, axis, angle):
    radians_angle = np.radians(-angle)
    if axis == "x":
        shearing_matrix = np.array([[1, 0], [np.tan(radians_angle), 1]])
        shearing_object = np.dot(object, shearing_matrix)
    elif axis == "y":
        shearing_matrix = np.array([[1, np.tan(radians_angle)], [0, 1]])
        shearing_object = np.dot(object, shearing_matrix)
    return shearing_object


def universal_transformation(object, a, b, c, d):
    custom_matrix = np.array([[a, b], [c, d]])
    transformed_object = np.dot(object, custom_matrix)
    return transformed_object


batman = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])
triangle = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2], [0, 0]])
