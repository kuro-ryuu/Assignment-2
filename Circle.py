while True:
    try:
        radius = int(input("What's the circle's radius?: "))
        area = radius ** 2 * 3.14
        if radius <= 0:
            print(f"Invalid input. Value must be greater than 0 and must be a numerical value.")
        else:
            print(f"The Area or the circle is {area}")
            break
    except ValueError:
        print(f"Invalid input. Value must be greater than 0 and must be a numerical value.")
