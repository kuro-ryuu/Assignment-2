while True:
    try:
        length = int(input("What's the rectangle's length?: "))
        width = int(input("What's the rectangle's width?: "))
        if width <= 0 or length <= 0:
            print(f"Error. Length & width must both be bigger than 0 and is a numerical value.")
        else:
            print(f"The Area or the rectangle is {length * width}\n"
                  f"The perimeter of the rectangle is {(length + width) * 2}")
            break
    except ValueError:
        print(f"Error. Please enter a valid numerical value for both length and width.")
