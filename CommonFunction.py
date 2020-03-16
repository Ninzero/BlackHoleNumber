from functools import reduce


def list2int(a: list) -> int:
    return reduce(lambda x, y: x*10+y, a)


def int2list(a: int) -> list:
    a = list(str(a))
    return map(lambda x: int(x), a)


def format_black_holes(black_hole_numbers: list) -> tuple:
    black_hole_number_groups = []
    while len(black_hole_numbers) > 0:
        current_group = []
        current_number = black_hole_numbers[0]
        while current_number in black_hole_numbers:
            current_group.append(current_number)
            black_hole_numbers.remove(current_number)
            minimum = list2int(sorted(int2list(current_number)))
            maximum = list2int(sorted(int2list(current_number), reverse=True))
            current_number = maximum - minimum
        black_hole_number_groups.append(tuple(current_group))
    return tuple(black_hole_number_groups)
