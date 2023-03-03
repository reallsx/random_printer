import random
import time

# Define a list of possible program names and actions
programs = ['firefox', 'chrome', 'notepad', 'explorer', 'cmd', 'powershell']
actions = ['running', 'loading', 'updating', 'scanning', 'installing']

# Define a function to print a progress bar
def print_progress_bar(progress):
    bar_length = 40
    filled_length = int(round(bar_length * progress))
    bar = '#' * filled_length + '-' * (bar_length - filled_length)
    print(f'[{bar}] {progress * 100:.0f}%', end='')
    print('\r', end='')

# Loop forever
while True:
    # Choose a random program and action
    program = random.choice(programs)
    action = random.choice(actions)

    # Print out the line
    print(f'{program} {action}...')
    
    # Simulate progress with a progress bar
    for i in range(1, 11):
        time.sleep(random.uniform(0.1, 0.5))
        print_progress_bar(i/10)

    print('\r')

    # Wait for a random amount of time between 0.5 and 2 seconds
    time.sleep(random.uniform(0.5, 2.0))
