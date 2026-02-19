user_id = int(input("User ID: "))
name = input("Name: ")
username = input("Username: ")
password = input("Password: ")
mobile = input("Mobile Number: ")
email = input("Email ID: ")
address = input("Address: ")

role = "User"
cart_details = []
purchase_history = []
total_orders = 0
billing_amount = 0
purchase_datetime = None
account_status = "Active"

choice = input("Add item to cart? (yes/no): ")

if choice == "yes":
    item = input("Enter item: ")
    cart_details.append(item)

buy = input("Proceed to purchase? (yes/no): ")

if buy == "yes" and cart_details:
    amount = float(input("Billing Amount: "))
    purchase_datetime = input("Date & Time: ")
    billing_amount += amount
    total_orders += 1
    purchase_history.append(cart_details)
    cart_details = []
    print("Purchase Successful")
elif buy == "yes":
    print("Cart is empty")
else:
    print("Purchase cancelled")

status = input("Deactivate account? (yes/no): ")

if status == "yes":
    account_status = "Inactive"
else:
    account_status = "Active"

print("\nUser Details:")
print(user_id, name, username, mobile, email, role, address)
print("Total Orders:", total_orders)
print("Billing Amount:", billing_amount)
print("Account Status:", account_status)















