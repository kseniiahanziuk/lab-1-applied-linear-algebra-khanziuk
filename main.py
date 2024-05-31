import functions

print("Welcome to linear transformation program!")
functions.command_prompt()

while True:
    choice = input("Enter the number of operation you want to perform(0-7): ")
    if choice == '0':  # Helping function which prints commands:
        functions.command_prompt()
    elif choice == '1':  # Objects without applied transformations:
        functions.plotting_2d_objects(functions.batman, "Batman without applied transformations")
        functions.plotting_2d_objects(functions.triangle, "Triangle without applied transformations")
        functions.plotting_tetrahedron(functions.tetrahedron,
                                       "Tetrahedron without applied transformations")
    elif choice == '2':  # Objects with rotation applied:
        angle = int(input("Enter the angle of rotation(in degrees): "))
        axis = (input("Enter the axis to rotate tetrahedron by(x, y, z): "))
        while axis not in ['x', 'y', 'z']:
            axis = input("Oops! Invalid input. You must choose x, y or z: ")
        functions.plotting_2d_objects(functions.rotate_2d_objects(functions.batman, angle),
                                      f"Batman rotated by {angle} degrees.")
        functions.plotting_2d_objects(functions.rotate_2d_objects(functions.triangle, angle),
                                      f"Triangle rotated by {angle} degrees.")
        functions.plotting_tetrahedron(functions.rotate_tetrahedron(functions.tetrahedron, angle, axis),
                                       f"Tetrahedron rotated by {angle} degrees by {axis} axis.")
    elif choice == '3':  # Objects with scaling applied:
        c = float(input("Enter the coefficient you want the objects to be scaled by: "))
        functions.plotting_2d_objects(functions.scaling_object(functions.batman, c), f"Batman scaled by {c}.")
        functions.plotting_2d_objects(functions.scaling_object(functions.triangle, c), f"Triangle scaled by {c}.")
        functions.plotting_tetrahedron(functions.scaling_object(functions.tetrahedron, c),
                                       f"Tetrahedron scaled by {c}.")
    elif choice == '4':  # Objects with reflection applied:
        axis = input("Enter the axis you want to reflect 2d objects by(x, y): ")
        while axis not in ['x', 'y']:
            axis = input("Oops! Invalid input. You must choose x, y: ")
        axis_3d = input("Enter the axis you want to reflect tetrahedron by(x, y, z): ")
        while axis_3d not in ['x', 'y', 'z']:
            axis_3d = input("Oops! Invalid input. You must choose x, y or z: ")
        functions.plotting_2d_objects(functions.reflecting_object(functions.batman, axis),
                                      f"Batman reflected by {axis}.")
        functions.plotting_2d_objects(functions.reflecting_object(functions.triangle, axis),
                                      f"Triangle reflected by {axis}.")
        functions.plotting_tetrahedron(functions.reflecting_tetrahedron(functions.tetrahedron, axis_3d),
                                       f"Tetrahedron reflected by {axis_3d}.")
        #   Reflecting tetrahedron does not change anything because it's a tetrahedron:)
    elif choice == '5':  # Objects with shearing applied:
        axis = input("Enter the axis you want to shear(x or y): ")
        while axis not in ['x', 'y']:
            axis = input("Oops! Invalid input. You must choose x or y: ")
        angle = int(input("Enter the angle you want to shear with(in degrees): "))
        functions.plotting_2d_objects(functions.shearing_axis(functions.batman, axis, angle),
                                      f"Batman sheared by {axis} with angle of {angle} degrees.")
        functions.plotting_2d_objects(functions.shearing_axis(functions.triangle, axis, angle),
                                      f"Triangle sheared by {axis} with angle of {angle} degrees.")
    elif choice == '6':  # Objects with universal transformation applied:
        matrix_elements = input(
            "Enter numbers for a, b, c and d in order 'a' 'b' 'c' 'd' respectfully for 2x2 matrix for 2d objects:\n"
            "a b\nc d\n")
        a, b, c, d = map(int, matrix_elements.split())
        functions.plotting_2d_objects(functions.universal_transformation(functions.batman, a, b, c, d),
                                      "Batman transformed by custom matrix.")
        functions.plotting_2d_objects(functions.universal_transformation(functions.triangle, a, b, c, d),
                                      "Triangle transformed by custom matrix.")

    elif choice == '7':  # Exiting the program
        print("Exiting the program... Bye!")
        break
    else:
        print("Invalid input! Try again. Choose the command(0-7): ")
