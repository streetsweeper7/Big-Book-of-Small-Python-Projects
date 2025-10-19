"""Birthday Paradox Simulation, by John Banda
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem"""

import random
from datetime import datetime, timedelta

birthdays = []

def init_birthdays():
    global birthdays
    birthdays = [0] * 366 

# This function generates an n number of random birthdays
# and returns the number of matching birthdays
def guess_n_birthdays(n:int):
    global birthdays
    i       = 0
    matches = []

    while (i < n):
        day = random.randint(0, 365)
        birthdays[day] += 1
        if birthdays[day] == 2:
            matches.append(day)
        i += 1

    return matches
    

def decode_birthday(day:int, year:int=2020):
    date = datetime(year, 1, 1) + timedelta(days=day)
    return date

def main():
     # Display the intro:
    print('''Birthday Paradox, by John Banda
 
    The Birthday Paradox shows us that in a group of N people, the odds
    that two of them have matching birthdays is surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated random
    simulations) to explore this concept.
    
    (It's not actually a paradox, it's just a surprising result.)
    ''')

    # init birthdays first
    init_birthdays()

    # Generate 23 birthdays
    matches = guess_n_birthdays(23)

    # Print the birthdays
    for day, day_count in enumerate(birthdays):
       if day_count > 0: 
            date = decode_birthday(day)
            print(f"{date.strftime('%b %d')} ")
   
    total_matches = 0 
    # Now let's run
    for i in range(1, 100001):
        init_birthdays()
        matches = guess_n_birthdays(23)
        if len(matches) >= 1:
            total_matches += 1 

        if (i % 10000 == 0):
            print(f'{i} simulations run ...')          

    print(f'Out of 100,000 simulations of 23 people, there was a matching birthday in that group {total_matches} times. This means that 23 people have a {total_matches / 1000:.2f}% chance of having a matching birthday in their group. That\'s probably more than you would think!')


if __name__ == "__main__":
    main()
