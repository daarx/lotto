import random
import sys


def process_arguments(args):
    if len(args) < 2:
        print('Usage: (eurojackpot|lotto) [rows]')
        return

    if len(args) < 3:
        repetitions = 1
    else:
        repetitions = int(args[2])

    match args[1]:
        case 'eurojackpot':
            action = generate_eurojackpot_row
        case 'lotto':
            action = generate_lotto_row
        case _:
            print('Use either eurojackpot or lotto as arguments')
            return

    for _ in range(repetitions):
        action()


def generate_eurojackpot_row():
    available_normal_numbers, available_extra_numbers = [*range(1, 51, 1)], [*range(1, 13, 1)]
    normal_max, extra_max = 5, 2
    selected_numbers, selected_extra_numbers = [], []

    while len(selected_numbers) < normal_max:
        selected_numbers.append(available_normal_numbers.pop(random.randrange(len(available_normal_numbers))))

    while len(selected_extra_numbers) < extra_max:
        selected_extra_numbers.append(available_extra_numbers.pop(random.randrange(len(available_extra_numbers))))

    selected_numbers = sorted(selected_numbers)
    selected_extra_numbers = sorted(selected_extra_numbers)

    print(*map(add_space_before_single_digit, selected_numbers), sep=', ', end=' + ')
    print(*map(add_space_before_single_digit, selected_extra_numbers), sep=', ')


def generate_lotto_row():
    available_numbers = [*range(1, 41, 1)]
    normal_max = 7
    selected_numbers = []

    while len(selected_numbers) < normal_max:
        selected_numbers.append(available_numbers.pop(random.randrange(len(available_numbers))))

    selected_numbers = sorted(selected_numbers)

    print(*map(add_space_before_single_digit, selected_numbers), sep=', ')


def add_space_before_single_digit(number):
    if number < 10:
        return f' {number}'
    else:
        return f'{number}'


if __name__ == '__main__':
    process_arguments(sys.argv)
