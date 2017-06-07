# UNFINISHED

def make_change(coins, n):

    coins.sort(reverse=True)
    coin_and_max = {}
    solutions = set([])

    for c in coins:
        if c < n:
            max_count = n/c
            coin_and_max[c] = max_count

            if n % c == 0:
                solution = []
                for i in range(max_count):  # here or later??
                    solution.append(c)
                solution = tuple(solution)
                solutions.add(solution)
        elif c == n:
            solutions.add([c])

    for coin, max in coin_and_max.iteritems():
        sum = 0
        solution = []

#        while sum < n:
 ########################3 ???
    return len(solutions)


# n,m = raw_input().strip().split(' ')
# n,m = [int(n),int(m)]
# coins = map(int,raw_input().strip().split(' '))
# print make_change(coins, n)
