import time
def print_simbol(n, symbol='*', delay=1):
    # Print increasing sequence of asterisks
    for i in range(n + 1):
        print(symbol * i)
        time.sleep(delay)

    # Print decreasing sequence of asterisks
    for j in range(n, 0, -1):
        print(symbol * j)
        time.sleep(delay)
def printer(n):
    print_simbol(n)
printer(5)







