ticket_count = 0
total_revenue = 0
free_tickets = 0

while True:
    name = input("Customer name (or q to quit): ")

    if name.lower() == "q":
        break

    age = int(input("Age: "))

    if age < 0 or age > 120:
        print("Invalid age.")
        continue

    day = input("Day (weekday/weekend): ").lower()

    if day != "weekday" and day != "weekend":
        print("Invalid day.")
        continue

    student = input("Student (yes/no): ").lower()

    if student != "yes" and student != "no":
        print("Please answer yes or no.")
        continue

    if day == "weekday":
        price = 200
    else:
        price = 250

    if age < 6:
        price = 0
        category = "Free"
    elif age >= 65:
        price = price * 0.5
        category = "Senior"
    elif age >= 6 and age <= 12:
        price = price * 0.6
        category = "Child"
    elif student == "yes" and age <= 25:
        price = price * 0.7
        category = "Student"
    else:
        category = "Standard"

    print(f"{name}: {price:.2f} TRY ({category})")

    ticket_count = ticket_count + 1
    total_revenue = total_revenue + price

    if price == 0:
        free_tickets = free_tickets + 1

if ticket_count == 0:
    print("No tickets sold.")
else:
    average_price = total_revenue / ticket_count
    print(
        f"Tickets sold: {ticket_count} "
        f"Total revenue: {total_revenue:.2f} TRY "
        f"Average price: {average_price:.2f} TRY "
        f"Free tickets: {free_tickets}"
    )
