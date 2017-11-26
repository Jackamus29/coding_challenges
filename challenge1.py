"""Solution to the 1st Challenge"""
game_count = 0
total_guess_count = 0
play_again_choice = 'y'
print ("In this game, you think of a number from 1 through n and I will try to"
       " guess what it is.\nAfter each guess, enter h if my guess is too high,"
       " l if too low, or c if correct.\n")
print "Please enter a number n:",
string = raw_input()
try:
    n = int(string)
    if n < 1:
        print "Your input: '%s', is not a positive integer." % string
        exit()
except ValueError:
    print "Your input: '%s', is not a positive integer." % string
    exit()

while play_again_choice == 'y':
    game_count += 1

    guess_low = 1
    guess_high = n
    guess_split = max((n / 2), guess_low)
    guess_count = 0
    response = ''
    while response != 'c':
        if response in ('', 'h', 'l'):
            guess_count += 1

        if response == 'l':
            guess_low = guess_split + 1
            guess_split = guess_high - ((guess_high - guess_split) / 2)
        elif response == 'h':
            guess_high = guess_split - 1
            guess_split = guess_low + ((guess_split - guess_low) / 2)

        if guess_high <= guess_low:
            print "Your number is %d." % guess_split
            response = 'c'
        else:
            print "%d?" % guess_split,
            response = raw_input()

    print "It took me %d guess(es)." % guess_count
    total_guess_count += guess_count
    print "I've averaged %g guess(es) per game for %d game(s)." % (
        (float(total_guess_count)/float(game_count)), game_count
    )

    print "Play again (y/n)?"
    play_again_choice = raw_input()

print "Bye!"
