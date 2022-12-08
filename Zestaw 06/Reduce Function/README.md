# Reduce Function

Given a list of rational numbers, find their product.

## Concept

The `reduce()` function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say `[1,2,3]` and you have to find its sum.

```py
>>> reduce(lambda x, y : x + y,[1,2,3])
6
```

You can also define an initial value. If it is specified, the function will assume initial value as the value given, and then reduce. It is equivalent to adding the initial value at the beginning of the list. For example:

```py
>>> reduce(lambda x, y : x + y, [1,2,3], -3)
3

>>> from fractions import gcd
>>> reduce(gcd, [2,4,8], 3)
1
```

## Input Format

First line contains `n`, the number of rational numbers.

The `i-th` of next `n` lines contain two integers each, the `numerator (Ni)` and `denominator (Di)` of the `i-th` rational number in the list.

## Constraints

- 1 ≤ n ≤ 100
- 1 ≤ Ni, Di ≤ 10⁹

## Output Format

Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form, i.e. numerator and denominator have no common divisor other than `1`.

## Sample Input 0

```text
3
1 2
3 4
10 6
```

## Sample Output 0

```text
5 8
```

## Explanation 0

Required product is:

$$\frac{1}{2}\frac{3}{4}\frac{10}{6}=\frac{5}{8}$$
