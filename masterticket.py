TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100


# Create Transaction function
# Calculate the price of the purchase
def purchase_price(number_of_tickets, ticket_price):
    return (number_of_tickets * ticket_price) + SERVICE_CHARGE

# Run this code continuously until we run out of tickets
while tickets_remaining :
    # Output how many tickets are remaining
    tickets_left = print("There are {} Tickets left to buy. So, Hurry while they last!".format(tickets_remaining))
    # Gather the user's name 
    users_name = input("Please enter your name:  ")
    try:
        # Welcome the user and ask how many tickets they would like to buy.
        # Expect a ValueError to happen
        greeting_and_gather_tickets_requested = int(input("Welcome {} there are {} tickets left for this event. How many would you like to purchase?  ".format(users_name, tickets_remaining)))
        if greeting_and_gather_tickets_requested > tickets_remaining :
            print("I'm sorry {}, You have requested more than the remaining amount of tickets.".format(users_name))
            how_many_remaining = print("There are only {} ticket(s) remaining.".format(tickets_remaining))
        else:
            # Inform the user the price of the tickets they want to purchase
            user_ticket_total_and_confirm_purchase = input("Your total will be ${}\n{}, Do you want to purchase these {} tickets? Y or N  ".format(purchase_price(greeting_and_gather_tickets_requested, TICKET_PRICE), users_name, greeting_and_gather_tickets_requested)).lower()
            # Subtract from the tickets remaining after the user purchase
            if user_ticket_total_and_confirm_purchase == "y" :
                # Subtract from the tickets remaining
                tickets_remaining -= greeting_and_gather_tickets_requested
                # TODO: Gather credit card information and process it.
                # Thank the user for the purchase
                print("Thank you {} for your purchase. Have a great day.".format(users_name))
            else:
                print("{}, Thank you for stopping by.".format(users_name))
    except ValueError:
        print("You must enter a digit.")
    
    
# Notify user if all the ticket have been sold
else:
    sold_out = print("We are sold out!")