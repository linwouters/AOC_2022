# AOC 2022-12-07
# Lin Wouters

import regex as re
import operator
import math

# OPS = {
#     '+' : operator.add,
#     '-' : operator.sub,
#     '*' : operator.mul,
#     '/' : operator.truediv,  # use operator.div for Python 2
#     '%' : operator.mod,
#     '^' : operator.xor,
# }


# class monkey:
#     def __init__(self, monkey_id) -> None:
#         self.id = monkey_id
#         self.items = []
#         # new = operation[0] (operation[1]) operation[1]. e.g. new= old + 4
#         self.operation = []
#         # Divided by, if true throw to monkey x, if false throw to monkey y
#         self.test_steps = [None, None, None]
#         self.inspect_counts = 0

#     def inspect(self, item):
#         self.inspect_counts += 1
#         # Calculate worry level
#         opers = [item if op == 'old' else op for op in self.operation]
#         return OPS[opers[1]](int(opers[0]), int(opers[2]))

#     def test(self, item):
#         # Return the monkeyid to throw the item to
#         if item % self.test_steps[0] == 0:
#             return self.test_steps[1]
#         return self.test_steps[2]
        

# class all_monkeys:
#     def __init__(self, divide_worry) -> None:
#         self.monkey_dict = {}
#         self.divide_worry = divide_worry

#     def round(self):
#         # Each monkey gets a turn in a round
#         for monkey in self.monkey_dict:
#             self.turn(self.monkey_dict[monkey])

#     def turn(self, monkey):
#         # A monkey inspects and throws each item during its turn
#         for item in list(monkey.items):
#             new_value = monkey.inspect(item)  # Calculate worry after monkey gets bored
#             if self.divide_worry != 1:
#                 new_value = math.floor(new_value / self.divide_worry) # Calculate worry after monkey gets bored
#             to_monkey = monkey.test(new_value) # Test where item is thrown
#             # Throw item
#             if to_monkey != monkey.id:
#                 # Give item to monkey that catches
#                 self.monkey_dict[to_monkey].items.append(new_value)
#                 # Remove item from monkey that throws
#                 monkey.items.pop(0)
#             # print(monkey.id, item, new_value, to_monkey, monkey.inspect_counts)


# def monkey_business(filepath, rounds=20, divide_worry=1):
#     monkeys = all_monkeys(divide_worry)
#     #
#     with open(filepath) as f:
#         for line in f:

#             # Read attributes
#             if line.startswith('Monkey'):
#                 monkey_id = int(re.findall('Monkey (\d+)', line)[0])
#                 monkeys.monkey_dict[monkey_id] = monkey(monkey_id)

#             elif line.strip().startswith('Starting items:'):
#                 items = re.findall(r'(\d+)', line)
#                 monkeys.monkey_dict[monkey_id].items = [int(item) for item in items]

#             elif line.strip().startswith('Operation:'):
#                 monkeys.monkey_dict[monkey_id].operation = re.findall('Operation: new = (.*)', line)[0].split(' ')

#             elif line.strip().startswith('Test:'):
#                 monkeys.monkey_dict[monkey_id].test_steps[0] = int(re.findall('Test: divisible by (\d+)', line)[0])

#             elif line.strip().startswith('If true:'):
#                 monkeys.monkey_dict[monkey_id].test_steps[1] = int(re.findall('If true: throw to monkey (\d+)', line)[0])

#             elif line.strip().startswith('If false:'):
#                 monkeys.monkey_dict[monkey_id].test_steps[2] = int(re.findall('If false: throw to monkey (\d+)', line)[0])

OPS = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}


class monkey:
    def __init__(self, monkey_id) -> None:
        self.id = monkey_id
        self.items = []
        # new = operation[0] (operation[1]) operation[1]. e.g. new= old + 4
        self.operation = []
        # Divided by, if true throw to monkey x, if false throw to monkey y
        self.test_steps = [None, None, None]
        self.inspect_counts = 0

    def inspect(self, item):
        self.inspect_counts += 1
        # Calculate worry level
        opers = [item if op == 'old' else op for op in self.operation]
        return OPS[opers[1]](int(opers[0]), int(opers[2]))

    def test(self, item):
        # Return the monkeyid to throw the item to
        if item % self.test_steps[0] == 0:
            return self.test_steps[1]
        return self.test_steps[2]
        

class all_monkeys:
    def __init__(self, divide_worry) -> None:
        self.monkey_dict = {}
        self.divide_worry = divide_worry

    def round(self):
        # Each monkey gets a turn in a round
        for monkey in self.monkey_dict:
            self.turn(self.monkey_dict[monkey])

    def turn(self, monkey):
        # A monkey inspects and throws each item during its turn
        for item in list(monkey.items):
            new_value = monkey.inspect(item)  # Calculate worry after monkey gets bored
            if self.divide_worry != 1:
                new_value = math.floor(new_value / self.divide_worry) # Calculate worry after monkey gets bored
            to_monkey = monkey.test(new_value) # Test where item is thrown
            # Throw item
            if to_monkey != monkey.id:
                # Give item to monkey that catches
                self.monkey_dict[to_monkey].items.append(new_value)
                # Remove item from monkey that throws
                monkey.items.pop(0)
            # print(monkey.id, item, new_value, to_monkey, monkey.inspect_counts)


def monkey_business(filepath, rounds=20, divide_worry=1):
    monkeys = all_monkeys(divide_worry)
    #
    with open(filepath) as f:
        for line in f:

            # Read attributes
            if line.startswith('Monkey'):
                monkey_id = int(re.findall('Monkey (\d+)', line)[0])
                monkeys.monkey_dict[monkey_id] = monkey(monkey_id)

            elif line.strip().startswith('Starting items:'):
                items = re.findall(r'(\d+)', line)
                monkeys.monkey_dict[monkey_id].items = [int(item) for item in items]

            elif line.strip().startswith('Operation:'):
                monkeys.monkey_dict[monkey_id].operation = re.findall('Operation: new = (.*)', line)[0].split(' ')

            elif line.strip().startswith('Test:'):
                monkeys.monkey_dict[monkey_id].test_steps[0] = int(re.findall('Test: divisible by (\d+)', line)[0])

            elif line.strip().startswith('If true:'):
                monkeys.monkey_dict[monkey_id].test_steps[1] = int(re.findall('If true: throw to monkey (\d+)', line)[0])

            elif line.strip().startswith('If false:'):
                monkeys.monkey_dict[monkey_id].test_steps[2] = int(re.findall('If false: throw to monkey (\d+)', line)[0])


    # Perform rounds
    for i in range(rounds):
        # print('------------------------', i, '----------------------')
        monkeys.round()

    print([monkeys.monkey_dict[monkey_id].inspect_counts for monkey_id in monkeys.monkey_dict])
    max1, max2 = sorted([monkeys.monkey_dict[monkey_id].inspect_counts for monkey_id in monkeys.monkey_dict])[-2:]
    return max1 * max2

if __name__ == "__main__":
    filepath="../data/day11.txt"
    # filepath="../data/test_day11.txt"

    print(f"The level of monkey business after 20 rounds with dividing worry by 3: {monkey_business(filepath, rounds=20, divide_worry=3)}")
    print(f"The level of monkey business after 20 rounds with dividing worry by 1: {monkey_business(filepath, rounds=20, divide_worry=1)}")
