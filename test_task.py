"""
Напишите программу, которая выводит n первых элементов
последовательности 122333444455555…
(число повторяется столько раз, чему оно равно).
"""


def solution(num: str):
    if not num or (n := int(num)) == 0:
        return None

    nums = []
    for i in range(1, n + 1):
        nums.append(str(i) * i)

    return ''.join(nums)


if __name__ == '__main__':
    num = input().replace(' ', '')
    print(__doc__)
    print(solution(num))
