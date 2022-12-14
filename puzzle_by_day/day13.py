# Lin Wouters
# 14-12-2022

import numpy as np

def compare_ints(left, right):
    # If left is lower, it is the right order
    if left < right:
        return 'right'
    elif left > right:
        return 'wrong'
    else:
        return 'unsure'

def compare_lengths(left, right):
    # If right has less items, it is the wrong order
    if len(left) < len(right):
        return 'right'
    elif len(left) > len(right):
        return 'wrong'
    else:
        return 'unsure'

def compare_pair(left, right):
    # If ints, left int should be lower
    if isinstance(left, int) and isinstance(right, int):
        return compare_ints(left, right)

    # If list, iterate over items and compare items
    if isinstance(left, list) and isinstance(right, list):
        # Otherwise compare items
        for i in range(min(len(left), len(right))):
            # Return right or wrong if a decision has been made
            comparison = compare_pair(left[i], right[i])
            if comparison != 'unsure':
                return comparison
        # Check if length determines order
        return compare_lengths(left, right)

    # If one value is int, convert to list and compare
    elif (isinstance(left, int) and isinstance(right, list)):
        return compare_pair([left], right)
    elif (isinstance(left, list) and isinstance(right, int)):
        return compare_pair(left, [right])


def find_right_orders(filepath):
    right_order_indx =[]
    with open(filepath) as f:
        file = f.read().split()
        for i in range(0, len(file), 2):
            # Evaluate pair
            left, right = eval(file[i]), eval(file[i+1])
            right_order = compare_pair(left, right)
            # Save index if order is right
            if right_order=='right':
                right_order_indx.append(i/2+1)

    return int(sum(right_order_indx))


def sort_right_order(filepath):
    # Use insertion sort
    orders = [[[2]], [[6]]]
    with open(filepath) as f:
        file = f.read().split()

        # Iterate over the packets
        for i in range(len(file)):
            packet = eval(file[i])
            # Iterate over the existing orders from left to right
            for j in range(len(orders)):
                # Insert packet when the order is right
                if compare_pair(packet, orders[j]) == 'right':
                    orders.insert(j, packet)
                    break

    return (orders.index([[2]])+1) * (orders.index([[6]])+1)


if __name__ == "__main__":
    filepath="data/day13.txt"
    # filepath="data/test_day13.txt"

    print(f"The sum of the indices with the right orders are: {find_right_orders(filepath)}")
    print(f"The decoder key for the distress signal is: {sort_right_order(filepath)}")