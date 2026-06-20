trains = {
    101: {"name": "Express", "seats": 5},
    102: {"name": "Super Fast", "seats": 3}
}

while True:
    print("\n--- Railway Reservation System ---")
    print("1. View Trains")
    print("2. Book Ticket")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for train_no, details in trains.items():
            print(f"{train_no} - {details['name']} - Seats: {details['seats']}")

    elif choice == "2":
        train_no = int(input("Enter Train Number: "))

        if train_no in trains:
            if trains[train_no]["seats"] > 0:
                name = input("Enter Passenger Name: ")
                trains[train_no]["seats"] -= 1

                print("\nTicket Booked Successfully!")
                print("Passenger:", name)
                print("Train:", trains[train_no]["name"])
                print("Remaining Seats:", trains[train_no]["seats"])
            else:
                print("No Seats Available!")
        else:
            print("Invalid Train Number!")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
