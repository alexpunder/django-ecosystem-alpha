"""
Напишите программу, которая выводит n первых элементов
последовательности 122333444455555…
(число повторяется столько раз, чему оно равно).
"""


def solution(string: str):
    cleaned_data = ''.join([
        i for i in string if i.isdigit()
    ])

    if not cleaned_data or (n := int(cleaned_data)) == 0:
        return None

    result = []
    for i in range(1, n + 1):
        result.append(str(i) * i)

    return ''.join(result)


if __name__ == '__main__':
    some_string = input()
    print(solution(some_string))
