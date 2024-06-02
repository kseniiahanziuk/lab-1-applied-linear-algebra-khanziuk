import functions_2

print("Welcome to linear transformation program(for images)!")
functions_2.command_prompt_2()

while True:
    choice = input("Enter the number of operation you want to perform(0-7): ")
    if choice == '0':  # Helping function which prints commands:
        functions_2.command_prompt_2()
    elif choice == '1':  # Images without applied transformations:
        functions_2.plotting_image(functions_2.image_doggo, "Long-nose doggo without applied transformations.")
    elif choice == '2':  # Images with rotation applied:
        angle = int(input("Enter the angle of rotation(in degrees): "))
        functions_2.plotting_image(functions_2.rotating_image(functions_2.image_doggo, angle),
                                   f"Long-nose doggo rotated by {angle} degrees.")
    elif choice == '3':  # Images with scaling applied:
        c = float(input("Enter the coefficient you want the images to be scaled by: "))
        functions_2.plotting_image(functions_2.scaling_image(functions_2.image_doggo, c),
                                   f"Long-nose doggo scaled by {c}.")
    elif choice == '4':  # Images with reflection applied:
        axis = input("Enter the axis you want to reflect images by(x, y): ")
        while axis not in ['x', 'y']:
            axis = input("Oops! Invalid input. You must choose x, y: ")
        functions_2.plotting_image(functions_2.reflecting_image(functions_2.image_doggo, axis),
                                   f"Long-nose doggo reflected by {axis}.")
    elif choice == '5':  # Images with shearing applied:
        axis = input("Enter the axis you want to shear(x or y): ")
        while axis not in ['x', 'y']:
            axis = input("Oops! Invalid input. You must choose x or y: ")
        angle = int(input("Enter the angle you want to shear with(in degrees): "))
        functions_2.plotting_image(functions_2.shearing_image(functions_2.image_doggo, axis, angle),
                                   f"Long-nose doggo sheared by {axis} with angle of {angle} degrees.")
    elif choice == '6':  # Images with universal transformation applied:
        print("Not implemented yet:(")
    elif choice == '7':  # Exiting the program
        print("Exiting the program... Bye!")
        break
    else:
        print("Invalid input! Try again. Choose the command(0-7): ")
