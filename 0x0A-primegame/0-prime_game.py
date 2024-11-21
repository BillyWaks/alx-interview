#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of integers where each integer n denotes
        a set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.

    Raises:
        None.
    """
    if not nums or x <= 0 or x != len(nums):
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    ben, maria = 0, 0

    for n in nums:
        prime_count = sum(primes[:n + 1])
        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def sieve_of_eratosthenes(n):
    """
    Generates a list indicating prime numbers up to n using the
    Sieve of Eratosthenes.

    Args:
        n (int): The upper limit of numbers to check for primality.

    Returns:
        list of int: A list where a[i] = 1 if i is prime, else 0.
    """
    primes = [1] * (n + 1)
    primes[0], primes[1] = 0, 0  # 0 and 1 are not primes

    for i in range(2, int(n**0.5) + 1):
        if primes[i] == 1:
            for multiple in range(i * i, n + 1, i):
                primes[multiple] = 0

    return primes
