#!/usr/bin/python3

  def isWinner(x, nums):
    """
    Determines the winner of each game and returns the player
    with the most wins.

    :param x: Number of rounds (integer)
    :param nums: List of integers representing n for each round
    :return: Name of the player with the most wins or None if it's a tie
    """
    if not nums or x < 1:
        return None

    # Precompute prime numbers up to the maximum number in nums
    max_num = max(nums)
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_num + 1, i):
                is_prime[multiple] = False

    # Precompute the cumulative count of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
  if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
