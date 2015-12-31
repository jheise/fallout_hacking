#!/usr/bin/env python
import sys
import argparse

words = []
choices = []

running = True

def print_possible():
    global words
    for x in enumerate(words):
        print "{0}: {1}".format(x[0], x[1])

def process_choice(choice):
    global words, choices
    password = words[choice]

    print "input likeness ",
    likeness = int(sys.stdin.readline().strip())

    choices.append((password, likeness))

def check_passwords():
    global words, choices
    wordlist = words[:]

    for password, likeness in choices:
        next_list = []
        for word in wordlist:
            # ignore selected word
            if word == password:
                continue

            hit_count = 0
            for i in range(len(password)):
                if password[i] == word[i]:
                    hit_count +=1

            if hit_count == likeness:
                next_list.append(word)

        wordlist = next_list[:]

    return wordlist

def main(source_file):
    global running, words
    words = [ x.strip() for x in open(source_file).readlines()]
    while running:
        print_possible()
        print "q - quit"
        print "Select Option: ",
        choice  = sys.stdin.readline().strip()
        if choice == "q":
            running = False
        else:
            process_choice(int(choice))
            words = check_passwords()
            #for x in possible:
                #print x

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="hack terminals in fallout games")
    parser.add_argument("filename", help="filename to read")

    args = parser.parse_args()
    main(args.filename)
