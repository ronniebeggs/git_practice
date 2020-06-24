import random

money = 100

#you are in a casino with 100 dollars cash to bet.
#you can bet on a coin flip, card pull, cho han, or 3 variations of roulette.
#the results of the bets are calculated at the bottom and are displayed once the code is run.

#coin flip code: (heads = 2 and tails = 1)
def coin_flip(guess, bet):

    #if the bet is less than or equal to 0 dollars, the code won't run
    if bet <= 0:
        print("You should bet more than 0 dollars!")
        return 0

    guess_ = guess.title()
    print("Let's flip a coin! You guessed {}.".format(guess_))
    flip_result = random.randint(1, 2)

    #Assigns the flip result to a string and the guess to an integer value
    if flip_result == 1:
        print("Tails!")
    else:
        print("Heads!")
    dic = {'Heads': 2, 'Tails': 1}
    int_guess = dic.get(guess_)

    #return whether your guess was correct or not
    if int_guess == flip_result:
        print("You won {} dollars!".format(bet))
        return bet
    else:
        print("Sorry, you lost {} dollars! :(".format(bet))
        return -bet


#cho han code:
def cho_han(guess, bet):

    #if the bet is less than or equal to 0 dollars, the code won't run
    if bet <= 0:
        print("----------")
        print("You should bet more than 0 dollars!")
        return 0

    guess_ = guess.title()
    print("----------")
    print("Let's play Cho Han! You guessed {}.".format(guess_))

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum = dice1 + dice2
    print("The sum of the two dice is {}.".format(sum))

    #determines whether the sum is even or odd and compares it to the guess
    if sum % 2 == 0:
        sum_result = "Even"
    else:
        sum_result = "Odd"

    if guess_ == sum_result:
        print("You prediction was correct! You won {} dollars!".format(bet))
        return bet
    else:
        print("Your prediction was incorrect! -{} dollars".format(bet))
        return -bet


#card pull code:
def card_pull(bet):

    #if the bet is less than or equal to 0 dollars, the code won't run
    if bet <= 0:
        print("----------")
        print("You should bet more than 0 dollars!")
        return 0

    print("----------")
    print("Let's pull cards!")

    player1_value = random.randint(1, 13)
    player2_value = random.randint(1, 13)
    #print(player1_value, player2_value)

    #makes numbers 1, 11, 12, and 13 their respective face cards
    face_cards = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
    if player1_value > 10 or player1_value == 1:
        updated_p1_value = face_cards.get(player1_value)
    else:
        updated_p1_value = player1_value
    if player2_value > 10 or player2_value == 1:
        updated_p2_value = face_cards.get(player2_value)
    else:
        updated_p2_value = player2_value

    print("Your card: {}. \nYour opponents card: {}.".format(updated_p1_value, updated_p2_value))

    #determines the result of the card pull and returns the results
    if player1_value > player2_value:
        print("You have a higher numbered card! +{} dollars".format(bet))
        return bet
    elif player1_value < player2_value:
        print("Your opponent has a higher numbered card! You lost {} dollars!".format(bet))
        return -bet
    else:
        print("You both selected the same card number!")
        return 0


#roulette code:
def roulette(guess, bet):

    #if the bet is less than or equal to 0 dollars, the code won't run
    if bet <= 0:
        print("----------")
        print("You should bet more than 0 dollars!")
        return 0

    print("----------")
    print("Let's play roulette!")
    ball_number = random.randint(1, 38)
    print("The ball landed on the {}.".format(ball_number))

    #checks to see whether the guess is a string and formats it
    if type(guess) == str:
        guess_ = guess.title()

    #runs roulette for an integer guess
    if type(guess) == int:
        if guess == ball_number:
            bet_winnings = bet * 35
            print("WOW! You guessed the correct number! \nYou won {} dollars!!!".format(bet_winnings))
            return bet_winnings
        else:
            print("Sorry, Better luck next time! -{} dollars".format(bet))
            return -bet

    #runs roulette for an odd/even guess
    elif guess == 'Odd' or guess == 'Even':
        if ball_number % 2 == 0:
            ball_type = 'Even'
        else:
            ball_type = 'Odd'
        print("The ball is {}.".format(ball_type))

        #either even or odd\/
        if guess_ == ball_type:
            print("You guessed {}! You win {} dollars!".format(guess, bet))
            return bet
        else:
            print("Sorry, you guessed incorrectly. -{} dollars".format(bet))
            return -bet

    #runs roulette for a high/low guess
    else:
        if ball_number >= 19:
            print("The ball is High.")
        else:
            print("The ball is Low.")

        if (guess_ == 'High' and ball_number >= 19) or (guess_ == 'Low' and ball_number <= 18):
            print("Congratulations, You guessed correctly! You win {} dollars".format(bet))
            return bet
        else:
            print("Sorry, better luck next time! -{} dollars".format(bet))
            return -bet


#calls the functions below and tallys up the bet money
money += coin_flip('TAILS', 15)
money += cho_han('OdD', 25)
money += card_pull(30)
money += roulette('EveN', 40)

print("----------")
print("Your total amount is {} dollars.".format(money))
if money < 0:
    print("Looks like you're in some serious debt!")
else:
    pass
