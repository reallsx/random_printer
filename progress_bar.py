import random
import time

def numbers_only(num, speed, rate):
    '''
    print progress in the same line but with only numbers.
    num: int, total number of items to go through
    speed: int, average number of files to go through per second
    rate: float, average time of refresh per second
    '''
    current = 0
    average_progress = speed/rate
    average_sleep = 1./rate

    while(current<num):
        print(f"\r[{current:>5d}/{num:>5d}]", end="")
        current += int(random.uniform(average_progress * 0.8, average_progress * 1.2))
        sleep_time = random.uniform(average_sleep * 0.8, average_sleep * 1.2)
        time.sleep(sleep_time)

    print(f"\r[{num:>5d}/{num:>5d}]")

def print_progress_bar(progress):
    bar_length = 40
    filled_length = int(round(bar_length * progress))
    bar = '#' * filled_length + '-' * (bar_length - filled_length)
    print(f'[{bar}] {progress * 100:.0f}%', end='')
    print('\r', end='')




