import numpy as np
import matplotlib.pyplot as plt


def plotting_2d_objects(object, name):
    plt.figure()
    plt.plot(object[:, 0], object[:, 1], color='purple')
    plt.axis('equal')
    plt.grid(True)
    plt.title(name)
    plt.show()


def plotting_tetrahedron(tetrahedron, name):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(len(tetrahedron)):
        for j in range(i + 1, len(tetrahedron)):
            x = [tetrahedron[i][0], tetrahedron[j][0]]
            y = [tetrahedron[i][1], tetrahedron[j][1]]
            z = [tetrahedron[i][2], tetrahedron[j][2]]
            ax.plot(x, y, z, color='purple')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(name)
    plt.show()


def rotate_2d_objects(object, angle):
    radians_angle = np.radians(angle)
    rotation_matrix = np.array([[np.cos(radians_angle), -np.sin(radians_angle)],
                                [np.sin(radians_angle), np.cos(radians_angle)]])
    rotated_object = np.dot(object, rotation_matrix)
    return rotated_object


def rotate_tetrahedron(object, angle, axis):
    axis = axis.lower()
    if axis == 'x':
        rotation_matrix = np.array([
            [1, 0, 0],
            [0, np.cos(angle), -np.sin(angle)],
            [0, np.sin(angle), np.cos(angle)]
        ])
    elif axis == 'y':
        rotation_matrix = np.array([
            [np.cos(angle), 0, np.sin(angle)],
            [0, 1, 0],
            [-np.sin(angle), 0, np.cos(angle)]
        ])
    elif axis == 'z':
        rotation_matrix = np.array([
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1]
        ])

    rotated_object = np.dot(object, rotation_matrix.T)
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


def reflecting_tetrahedron(object, axis):
    if axis == 'x':
        reflection_matrix = np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, -1]
        ])
    elif axis == 'y':
        reflection_matrix = np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, -1]
        ])
    elif axis == 'z':
        reflection_matrix = np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])

    reflected_object = np.dot(object, reflection_matrix.T)
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


def command_prompt():
    print("Choose the option: \n"
          "0) Help.\n"
          "1) Show objects without transformations.\n"
          "2) Rotation.\n"
          "3) Scaling.\n"
          "4) Reflecting.\n"
          "5) Shearing.\n"
          "6) Custom transformation.\n"
          "7) Exit.\n")


batman = np.array([[0, 0],
                   [1, 0.2],
                   [0.4, 1],
                   [0.5, 0.4],
                   [0, 0.8],
                   [-0.5, 0.4],
                   [-0.4, 1],
                   [-1, 0.2],
                   [0, 0]])
triangle = np.array([
    [0, 0],
    [1, 0],
    [0.5, np.sqrt(3)/2],
    [0, 0]])

tetrahedron = np.array([
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, -1],
    [1, -1, -1]
])
