#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    print(
        "Количество одиннаковых элементов: ", len(tuple(filter(lambda x: x == A[0], A))),
        "\nИзмененный список", tuple(filter(lambda x: x != A[0], A))
    )
