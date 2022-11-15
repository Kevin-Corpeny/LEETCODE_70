import numpy as np

def solve_steps(n: int) -> int:
    #return how many ways by taking 1 or 2 steps one could reach step n
    steps = np.zeros(n+1)

    steps[n] = 1 #at the final step
    steps[n-1] = 1 #one step before, only one option
    print(steps[n-1])
    i = n-2
    for _ in steps:
        steps[i] = steps[i+1] + steps[i+2]
        if i is 0:
            break
        i -= 1
    print(steps[0:2])
    return steps[0]
print(f'Permutations for 5 steps: {solve_steps(5)}')

print(f'Permutations for 3 steps: {solve_steps(3)}')
