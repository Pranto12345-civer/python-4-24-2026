def km_to_miles():
    km = float(input("Enter distance in Kilometers: "))
    conversion_factor = 0.621371
    miles = km * conversion_factor
    print(f"{km} KM is equal to {miles:.2f} Miles")

km_to_miles()