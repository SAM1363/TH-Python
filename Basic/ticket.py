Ticket_price = 100

tickets_remaining = 14

# output how many tickets remaining using the tr vurable

print('there are {} tickets remaining now'.format(tickets_remaining))

# gather the user's name and assign it to new vurable

User_name = raw_input('What is your name? ')

# ask how many tickets the user want

total_tickets = raw_input('Hi {}! How many tickets do you want to buy? '.format(User_name))
total_tickets = int(total_tickets)

total_price = total_tickets * Ticket_price

print('total is {}'.format(total_price))
