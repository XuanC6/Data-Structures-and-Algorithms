# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    ratio = []
    for i in range(len(weights)):
        ratio.append(values[i]/weights[i])
    
    for i in range(n):
        if capacity==0:
            return value
        c = max(ratio)
        j = ratio.index(c)
        weight = min(capacity,weights[j])
        value = value + c*weight
        capacity -= weight
        weights.pop(j)
        values.pop(j)
        ratio.pop(j)
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
