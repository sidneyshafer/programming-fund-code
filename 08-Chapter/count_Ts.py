# This program counts the number of times
# the letter T (upper or lower)
# appears in a string

def main():

    count = 0

    my_string = input('Enter a sentence: ')

    for ch in my_string:
        if ch == 'T' or ch == 't':
            count += 1

    print('The letter T appears', count, 'times.')

main()
