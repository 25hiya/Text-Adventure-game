
import random


def hangman() -> bool:
    """
    Runs a game of HANGMAN.
    The player is looking for his/her cheat sheet in one of the books he/she had read last night.
    Unfortunately, he/she forgot which book she left her cheat sheet in.
    Play a game of HANGMAN to find out the book title.
    The player have 5 incorrect attempts to solve the HANGMAN.
    GOODLUCK!!
    """
    answer = 'LINEAR TIME, BRANCHING TIME AND PARTIAL ORDER IN LOGICS AND MODELS FOR CONCURRENCY'
    guesses = ['_', '_', '_', '_', '_', '_', ' ', '_', '_', '_', '_', ',', ' ',
               '_', '_', '_', '_', '_', '_', '_', '_', '_', ' ', '_', '_', '_', '_', ' ',
               '_', '_', '_', ' ', '_', '_', '_', '_', '_', '_', '_', ' ', '_', '_', '_', '_', '_', ' ',
               '_', '_', ' ', '_', '_', '_', '_', '_', '_', ' ', '_', '_', '_', ' ', '_', '_', '_', '_', '_', '_', ' ',
               '_', '_', '_', ' ', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
    print(''.join(guesses))
    number_of_guesses = 5
    while (number_of_guesses >= 0) and (answer != ''.join(guesses)):
        guess = input('Enter a letter ')
        if str.capitalize(guess) not in answer:
            number_of_guesses -= 1
            print('Letter not found in answer')
            print(f'Number of Guesses Left: {number_of_guesses}')

        elif str.capitalize(guess) == 'L':
            guesses[0] = 'L'
            guesses[38] = 'L'
            guesses[49] = 'L'
            guesses[64] = 'L'

        elif str.capitalize(guess) == 'I':
            guesses[1] = 'I'
            guesses[8] = 'I'
            guesses[19] = 'I'
            guesses[24] = 'I'
            guesses[36] = 'I'
            guesses[46] = 'I'
            guesses[52] = 'I'

        elif str.capitalize(guess) == 'N':
            guesses[2] = 'N'
            guesses[16] = 'N'
            guesses[20] = 'N'
            guesses[29] = 'N'
            guesses[47] = 'N'
            guesses[57] = 'N'
            guesses[73] = 'N'
            guesses[79] = 'N'

        elif str.capitalize(guess) == 'E':
            guesses[3] = 'E'
            guesses[10] = 'E'
            guesses[26] = 'E'
            guesses[43] = 'E'
            guesses[63] = 'E'
            guesses[78] = 'E'

        elif str.capitalize(guess) == 'A':
            guesses[4] = 'A'
            guesses[15] = 'A'
            guesses[28] = 'A'
            guesses[33] = 'A'
            guesses[37] = 'A'
            guesses[56] = 'A'

        elif str.capitalize(guess) == 'R':
            guesses[5] = 'R'
            guesses[14] = 'R'
            guesses[34] = 'R'
            guesses[41] = 'R'
            guesses[44] = 'R'
            guesses[69] = 'R'
            guesses[76] = 'R'
            guesses[77] = 'R'

        elif str.capitalize(guess) == 'T':
            guesses[7] = 'T'
            guesses[23] = 'T'
            guesses[35] = 'T'

        elif str.capitalize(guess) == 'M':
            guesses[9] = 'M'
            guesses[25] = 'M'
            guesses[60] = 'M'

        elif str.capitalize(guess) == 'B':
            guesses[13] = 'B'

        elif str.capitalize(guess) == 'C':
            guesses[17] = 'C'
            guesses[53] = 'C'
            guesses[71] = 'C'
            guesses[74] = 'C'
            guesses[80] = 'C'

        elif str.capitalize(guess) == 'H':
            guesses[18] = 'H'

        elif str.capitalize(guess) == 'G':
            guesses[21] = 'G'
            guesses[51] = 'G'

        elif str.capitalize(guess) == 'D':
            guesses[30] = 'D'
            guesses[42] = 'D'
            guesses[58] = 'D'
            guesses[62] = 'D'

        elif str.capitalize(guess) == 'P':
            guesses[32] = 'P'

        elif str.capitalize(guess) == 'O':
            guesses[40] = 'O'
            guesses[50] = 'O'
            guesses[61] = 'O'
            guesses[68] = 'O'
            guesses[72] = 'O'

        elif str.capitalize(guess) == 'S':
            guesses[54] = 'S'
            guesses[65] = 'S'

        elif str.capitalize(guess) == 'F':
            guesses[67] = 'F'

        elif str.capitalize(guess) == 'U':
            guesses[75] = 'U'

        elif str.capitalize(guess) == 'Y':
            guesses[81] = 'Y'

        print(''.join(guesses))

    if ''.join(guesses) != answer:
        print('FAILED')
        return False
    else:
        print('CONGRATS! YOU FOUND YOUR CHEAT SHEET!! YAY :')
        return True


class Deck:
    """
    A standard deck of playing cards consists of 52 Cards, divided into 4 suits.
    """
    stockpile: list[str]

    def __init__(self):
        """
        Initialize a new deck of cards
        """
        self.stockpile = []
        suits = ['Spade', 'Club', 'Diamond', 'Heart']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        for suit in suits:
            for value in values:
                self.stockpile.append(f'{value} of {suit}')

    def draw(self) -> str:
        """
        Return the card drawn from the shuffled stockpile
        """
        if len(self.stockpile) > 0:
            index = random.randint(0, len(self.stockpile) - 1)
            return self.stockpile.pop(index)


class Hand(Deck):
    """
    The Player's Hand.
    """
    hand: list[str]

    def __init__(self) -> None:
        """
        Initialize a new hand of cards
        """
        Deck.__init__(self)
        self.hand = []

    def get_value(self, card: str) -> int:
        """
        Return the value of each card.
        Rank of Values from lowest to highest : 2,3,4,5,6,7,8,9,10,J,Q,K,A
        """
        value = card.split()[0]
        true_value = 0
        if value in {'2', '3', '4', '5', '6', '7', '8', '9', '10'}:
            true_value += int(value)
        elif value in {'J': 11, 'Q': 12, 'K': 13, 'A': 14}:
            true_value += {'J': 11, 'Q': 12, 'K': 13, 'A': 14}[value]

        return true_value

    def compare(self, first_card: str, new_card: str) -> str:
        """
        Return which card has a greater value
        Rank of Suits from lowest to highest: Diamond, Club, Heart, Spade
        Rank of Values from lowest to highest : 2,3,4,5,6,7,8,9,10,J,Q,K,A
        Note: prioritizing numbers, not suits
        """
        suit1 = first_card.split()[2]
        suit2 = new_card.split()[2]
        value_first_card = self.get_value(first_card)
        value_new_card = self.get_value(new_card)
        while value_first_card == value_new_card:
            value_first_card *= {'Spade': 4, 'Heart': 3, 'Club': 2, 'Diamond': 1}[suit1]
            value_new_card *= {'Spade': 4, 'Heart': 3, 'Club': 2, 'Diamond': 1}[suit2]

        if value_first_card > value_new_card:
            return first_card
        elif value_first_card < value_new_card:
            return new_card

    def play(self) -> bool:
        """
        Playing a game of Higher or Lower. Where the player make a guess on
        whether their new card will have a higher or lower value than their first card.
        """
        first_card = self.draw()
        print(f'You drew a card, the {first_card}')

        guess = input('Do you think the next card drawn will be higher or lower than your current card? ').lower()

        while guess not in {'higher', 'lower'}:
            print('Please enter a valid answer (Higher/Lower) ')
            guess = input('Do you think the next card drawn will be higher or lower than your current card? ').lower()

        new_card = self.draw()
        print(f'Your new card is: {new_card}')

        if self.compare(first_card, new_card) == first_card:
            if guess == 'higher':
                print('You guessed wrong!')
                return False
            elif guess == 'lower':
                print('CORRECT! Congratulations! You were able to find out which is your lucky pen :)')
                return True

        elif self.compare(first_card, new_card) == new_card:
            if guess == 'lower':
                print('You guessed wrong!')
                return False
            elif guess == 'higher':
                print('CORRECT! Congratulations! You were able to find out which is your lucky pen :)')
                return True

def higher_lower() -> bool:
    hand1 = Hand()
    return hand1.play()












