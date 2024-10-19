import sys
import time


def animated_print(text, delay=0.1):
    """
    THis function will add animation effect to printed output
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
