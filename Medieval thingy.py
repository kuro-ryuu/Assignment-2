while True:
    try:
        print("Please enter a valid answer.")
        talents = float(input(f"Please enter your talents: "))
        pounds = float(input(f"Please enter your pounds: "))
        lots = float(input(f"Please enter your lots: "))
        grams = ((talents*20+pounds)*32+lots)*13.3
        kilograms = float(grams // 1000)
        extra = grams % 1000
        print(f"Enter talents:\n"
              f"{talents}\n"
              "\n"
              f"Enter pounds:\n"
              f"{pounds}\n"
              "\n"
              f"Enter lots:\n"
              f"{lots}\n"
              "\n"
              f"The weight in modern units:\n"
              f"{kilograms:.0f} kilograms and {extra:.2f} grams.\n")
    except ValueError:
        print("Invalid respond, please try again.")
