r"""
Problem:
    In a town, there are n people labeled from 1 to n. There is a rumor that one
    of these people is secretly the town judge.

    If the town judge exists, then:
    1. The town judge trusts nobody (out-degree = 0).
    2. Everybody (except the town judge) trusts the town judge (in-degree = n - 1).
    3. There is exactly one person that satisfies properties 1 and 2.

    Given the integer n and an array trust where trust[i] = [a_i, b_i] indicates
    that person a_i trusts person b_i, return the label of the town judge if the
    judge exists and can be identified, or return -1 otherwise.

Graph / Degree Concept:
    We can model the trust relationships as a Directed Graph:
    - Nodes: People labeled 1 to n.
    - Directed Edges: [a, b] represents a directed edge from a to b (a -> b).

    For each person i:
    - inTrustCount[i]  = in-degree  (number of people who trust person i)
    - outTrustCount[i] = out-degree (number of people person i trusts)

    The Town Judge is a "Universal Sink" (all arrows point in, none point out):
        in-degree  == n - 1
        out-degree == 0

Example (n = 4, trust = [[1, 3], [4, 3], [2, 3]]):

    Directed Graph Representation:
        (1) ------> (3) <------ (4)
                     ^
                     |
                    (2)

    Degree Table:
    +--------+-----------+------------+-------------------------------+
    | Person | In-Degree | Out-Degree | Condition Check               |
    +--------+-----------+------------+-------------------------------+
    |   1    |     0     |     1      | Not judge (out > 0, in != 3)  |
    |   2    |     0     |     1      | Not judge (out > 0, in != 3)  |
    |   3    |     3     |     0      | JUDGE! (in == 3 and out == 0) |
    |   4    |     0     |     1      | Not judge (out > 0, in != 3)  |
    +--------+-----------+------------+-------------------------------+
    Result: 3 is the Town Judge!

Complexity:
    - Time Complexity:  O(T + N), where T = len(trust) and N is the number of people.
                        We iterate through the trust array once (O(T)), and then
                        iterate through people 1 to n once (O(N)).
    - Space Complexity: O(N) to store in-degree and out-degree counts for up to N people.
"""

from collections import defaultdict


def findJudge(n, trust):
    """
    Finds the town judge if one exists, otherwise returns -1.
    Uses in-degree and out-degree tracking in a directed trust graph.
    """
    inTrustCount = defaultdict(int)
    outTrustCount = defaultdict(int)

    # Build graph degrees: edge i -> j
    for i, j in trust:
        inTrustCount[j] += 1   # j receives trust (in-degree)
        outTrustCount[i] += 1  # i gives trust (out-degree)

    # Check which person satisfies both judge criteria
    for i in range(1, n + 1):
        if inTrustCount[i] == n - 1 and outTrustCount[i] == 0:
            return i

    return -1


def main():
    test_cases = [
        (4, [[1, 3], [4, 3], [2, 3]]),     # Expected: 3
        (2, [[1, 2]]),                     # Expected: 2
        (3, [[1, 3], [2, 3], [3, 1]]),     # Expected: -1 (judge trusts someone)
        (3, [[1, 2], [2, 3]]),             # Expected: -1 (nobody has n-1 trusts)
        (1, []),                           # Expected: 1 (single person town)
    ]

    for n, trust in test_cases:
        result = findJudge(n, trust)
        print(f"n = {n}, trust = {trust} -> Judge: {result}")


if __name__ == "__main__":
    main()

