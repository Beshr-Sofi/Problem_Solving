"""Koko Eating Bananas — example script.

This module contains a solution for the common problem sometimes called
"Koko Eating Bananas": given a list of banana piles and an integer `h`
hours, find the minimum integer eating speed `k` (bananas per hour) such
that Koko can finish all piles within `h` hours.

Approach: binary search on the speed `k` in range [1, max(piles)]. For a
candidate speed `mid`, compute the total hours needed as the sum of
ceil(pile / mid) for every pile. If the total exceeds `h`, the speed is
too slow and we search higher; otherwise we try lower speeds.

Time complexity: O(n log m) where n = len(piles) and m = max(piles).
Space complexity: O(1).
"""


def minEatingSpeed(piles, h):
    """Return minimum integer eating speed `k` so total hours <= `h`.

    Parameters
    - piles (list[int]): list of positive integers, bananas in each pile
    - h (int): maximum allowed hours

    Returns
    - int: smallest integer `k` such that Koko can eat all bananas within
      `h` hours.

    The function performs a binary search over possible speeds. For each
    candidate `mid` it computes required hours using integer math:
    `(pile + mid - 1) // mid` is equivalent to `ceil(pile / mid)` but
    uses only integers.
    """

    # search range: at least 1 banana/hour, at most max(piles)
    l, r = 1, max(piles)

    while l <= r:
        mid = (l + r) // 2

        # compute total hours needed at speed `mid`
        total_hours = 0
        for pile in piles:
            # ceil division: how many hours to finish this pile at speed mid
            total_hours += (pile + mid - 1) // mid

        # if it takes more than h hours, `mid` is too small -> increase lower bound
        if total_hours > h:
            l = mid + 1
        else:
            # otherwise we can try a smaller speed
            r = mid - 1

    # after binary search `l` is the smallest valid speed
    return l


def main():
    # example usage and quick sanity check
    piles = [25, 10, 23, 4]
    H = 4
    print(minEatingSpeed(piles, H))


if __name__ == "__main__":
    main()
