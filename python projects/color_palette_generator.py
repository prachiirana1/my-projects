import random

def generate_palette():
    print("Welcome to the Color Palette Generator!")
    colors = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple', 'Pink', 'Brown', 'Black', 'White']
    print("Choose an option:")
    print("1. Generate a random color palette")
    print("2. Create a custom color palette")

    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        palette = random.sample(colors, 3)
        print("Generated Color Palette:", ", ".join(palette))
    elif choice == '2':
        print("Available Colors:", ", ".join(colors))
        custom_palette = input("Enter three colors separated by commas: ").split(',')
        print("Your Custom Color Palette:", ", ".join([color.strip() for color in custom_palette]))
    else:
        print("Invalid choice. Please restart.")


generate_palette()
