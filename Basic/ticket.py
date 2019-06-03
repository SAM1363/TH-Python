Ticket_price = 100
Servise_charge = 2

tickets_remaining = 14


def calc_price(x):
    return (x * Ticket_price) + Servise_charge

while tickets_remaining > 1:
    print('there are {} tickets remaining now'.format(tickets_remaining))
    User_name = raw_input('What is your name? ')
    total_tickets = input('Hi {}! How many tickets do you want to buy? '.format(User_name))
    try:
        total_tickets = int(total_tickets)
        if total_tickets > tickets_remaining:
            raise ValueError('sorry, there is no more than {} tickets'.format(tickets_remaining))
    except ValueError as err:
        print('that is nat a valid value {} please run it again'.format(err))
    else:
        # total_price = total_tickets * Ticket_price
        total_price = calc_price(total_tickets)
        print('total is {}'.format(total_price))
        proc = raw_input('Do you wanna proceed? Y/N ')
        if proc == 'Y':
            print('sold')
            tickets_remaining -= total_tickets
        else:
            print('thank you {}!'.format(User_name))

print('Sorry the tickets is sold')