print("Enter your daily expenses. Type '0' to stop.")
expenses = []

while True:
    item = float(input("Enter amount: "))
    if item == 0:
        break
    expenses.append(item)

print(f"Total Expenses: ${sum(expenses)}")
print(f"Number of items: {len(expenses)}")