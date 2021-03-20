import sys, time

def typing(lst):
    lst += '\n'
    for character in lst:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)