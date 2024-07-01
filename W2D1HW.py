
restaurant_menu = {"Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}}
Bev= {"Beverages":{'Rootbeer':2.99, 'Iced Tea': 2.99}}
restaurant_menu.update(Bev)
restaurant_menu.update


del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)



#Service Data Handling


def addTask():
  task = input("Please enter a task: ")
 
  print(f"Task '{task}' added to the list.")





s_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}




def open_ticket(customer, issue):
    ticket_id = f'Ticket{len(s_tickets) + 1:03d}'
    s_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
    print(f"New ticket opened: {ticket_id}")


def update_ticket_status(ticket_id, status):
    if ticket_id in s_tickets:
        s_tickets[ticket_id]['Status'] = status
        print(f"Ticket {ticket_id} status updated to {status}")
    else:
        print(f"Ticket {ticket_id} not found")

def display_tickets(filter_status=None):
    for ticket_id, details in s_tickets.items():
        if filter_status is None or details['Status'] == filter_status:
            print(f"ID: {ticket_id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")


open_ticket("Sam", "connection issue")
open_ticket("Keoini", "Error message 0021E")


update_ticket_status("Ticket001", "closed")


print("All Tickets:")
display_tickets()


print("\nOpen Tickets:")
display_tickets(filter_status="open")


open_ticket("Skylar", "Forgot password")
print("\nUpdated Tickets:")
display_tickets()


update_ticket_status("Ticket002", "closed")
print("\nTickets after status update:")
display_tickets()