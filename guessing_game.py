# building a guessiing game
import random

print('Welcome to the guessing game')
print('There are 3 levels to the guessing game'
      '\nStage 1 Easy Level\nStage 2 Medium Level'
      '\nStage 3 Hard level\nPick One Option(stage : 1, 2 or 3)')


def easylevel():
    chances = 6
    number = 10
    mix = random.randint(1,number)
    print('Welcome to the Easy Level you have 6 guess chances.'
          '\nGuess the correct Number from 1-10'
          '\nIf you uses all 6 chances with out getting the right answer you loose'
          '\nIf you get the correct answer you move on to Medium level'
          '\nLET PLAY.')
    while True:
        guess = int(input('Enter Your Answer : '))
        if guess == mix:
            print('Congratulations, {} was the correct answer '.format(guess))
            print('Next level')
            mediumlevel()
        else:
            print('{} Was The Wrong Answer\nTry Again.'.format(guess))
            chances -= 1
            if chances == 1 or chances == 0:
                print('You have {} chance left'.format(chances))
            elif chances == 0:
                print('Chances exhausted Try again next time.\nGame OVer.')
                break
            else:
                print('You have {} chances left'.format(chances))



def mediumlevel():
    chances = 4
    number = 20
    mix = random.randint(1,number)
    print('Welcome to the Easy Level you have 4 guess chances.'
          '\nGuess the correct Number from 1-20'
          '\nIf you uses all 4 chances with out getting the right answer you loose'
          '\nIf you get the correct answer you move on to Hard level'
          '\nLET PLAY.')
    while True:
        guess = int(input('Enter Your Answer : '))
        if guess == mix:
            print('Congratulations, {} was the correct answer '.format(guess))
            print('Next level')
            hardlevel()
        else:
            print('{} Was The Wrong Answer\nTry Again.'.format(guess))
            chances -= 1
            if chances == 1 or chances == 0:
                print('You have {} chance left'.format(chances))
            elif chances == 0:
                print('Chances exhausted Try again next time.\nGame OVer.')
                break
            else:
                print('You have {} chances left'.format(chances))
def hardlevel():
    chances = 3
    number = 50
    mix = random.randint(1,number)
    print('Welcome to the Easy Level you have 3 guess chances.'
          '\nGuess the correct Number from 1-50'
          '\nIf you uses all 3 chances with out getting the right answer you loose'
          '\nIf you get the correct answer you Win.'
          '\nLET PLAY.')
    while True:
        guess = int(input('Enter Your Answer : '))
        if guess == mix:
            print('Congratulations, {} was the correct answer '.format(guess))
            print('YOU WIN...HURRAY\nGAME OVER.')
        else:
            print('{} Was The Wrong Answer\nTry Again.'.format(guess))
            chances -= 1
            if chances == 1 or chances == 0:
                print('You have {} chance left'.format(chances))
            elif chances == 0:
                print('Chances exhausted Try again next time.\nGame OVer.')
                break
            else:
                print('You have {} chances left'.format(chances))

selection = int(input('Enter Selection :  '))
if selection == 1:
    easylevel()
elif selection == 2:
    mediumlevel()
elif selection == 3:
    hardlevel()
else:
    print('Invalid Selection Try Again')
