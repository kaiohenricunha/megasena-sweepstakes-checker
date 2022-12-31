import pandas as pd
import logging

class Bet:
    def __init__(self, betcode, ownership, numbers):
        self.betcode = betcode
        self.ownership = ownership
        self.numbers = numbers

    def __str__(self):
        return f'betcode: {self.betcode}, ownership: {self.ownership}, numbers: {self.numbers}'

# logging setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # or any level you want

# on-screen log output
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)  # or any other level
logger.addHandler(ch)

# collects bets info from csv file
def collect_bets_info():
    file_name = 'bets.csv'
    cols = ['betcode', 'ownership', 'numbers']

    try:
        bet_info = pd.read_csv(file_name, usecols=cols)
        betcode = bet_info['betcode'].tolist()
        ownership = bet_info['ownership'].tolist()
        numbers = [number.strip().split(' ') for number in bet_info['numbers'].tolist()]
    except FileNotFoundError:
        logger.error(f'file {file_name} not found')
        exit(1)
    
    return betcode, ownership, numbers


# initializes bet objects
def initialize_bets(betcode, ownership, numbers):
    bets = []
    for i in range(len(betcode)):
        bets.append(Bet(betcode[i], ownership[i], numbers[i]))

    return bets

# checks if any of the bets match at least 4 numbers
def check_bets(bets, numbers):
    winners = []

    for bet in bets:
        count = 0
        for number in bet.numbers:
            if number in numbers:
                count += 1
        switch = {
            6: 'sena',
            5: 'quina',
            4: 'quadra',
        }

        if count in switch:
            winners.append(f'betcode: {bet.betcode}, ownership: {bet.ownership}, won the {switch[count]}!')

    if len(winners) == 0:
        logger.info('not rich today...')
    else:
        for winner in winners:
            logger.info(winner)

def main():
    betcode, ownership, numbers = collect_bets_info()
    bets = initialize_bets(betcode, ownership, numbers)
    numbers = input('Enter the 6 numbers(eg. 1,2,3,4,5,6): ')
    numbers = numbers.strip().split(',')
    check_bets(bets, numbers)

if __name__ == '__main__':
    main()