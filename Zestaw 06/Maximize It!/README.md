# Maximize It

You are given a function `f(X) = X²`. You are also given `K` lists. The `i-th` list consists of `Ni` elements.

You have to pick one element from each list so that the value from the equation below is maximized:

```text
S = (f(X1) + f(X2) + ... + f(Xk)) % M
```

- `Xi` denotes the element picked from the `i-th` list. Find the maximized value `Smax` obtained.
- `%` denotes the modulo operator.

> Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

## Input format

The first line contains `2` space separated integers `K` and `M`.

The next `K` lines each contains an integer `Ni`, denoting the number of elements in the `i-th` list, followed by `Ni` space separated integers denoting the elements in the list.

## Constraints

- 1 ≤ `K` ≤ 7
- 1 ≤ `M` < 1000
- 1 ≤ `Ni` ≤ 7
- 1 ≤ Magnitude of elements in list ≤ 10⁹

## Output Format

Output a single integer denoting the value `Smax`.

## Sample Input

```text
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10
```

## Sample Output

```text
206
```

## Explanation

Picking `5` from the `1st` list, `9` from the `2nd` list and `10` from the `3rd` list gives the maximum `S` value equal to `(5² + 9² + 10²) % 1000 = 206`
