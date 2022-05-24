

### Chinese Remainder Theorem - cycles - lcm

1. determine cycle for each moon  
2. determine relative start step for each moon  
3. Chinese remainder theorem --> reverse gcd sort of thing  
4. Extended Euclidean Algorithm - Inverse modular arithmetic


### tests - tests - Tests - TESTS!!!


### triangular numbers
```python
def triangular(x: int) -> int:
    return x * (x + 1) // 2
```


### farey sequence
- add farey sequence (extract from AOC)
- add the all int slope vectors in 2D


### coprimes = relatively prime numbers
Two numbers are relatively prime (coprime) if they have 
no prime factor in common, and their only common factor is 1
if `gcd(a, b) == 1` --> `a` and `b` are relatively prime
`gcd` = Greatesd Common Divisor
`hcf` = Highest Common Factor
These two definitions are the same
```python
>>> coprime(4, 13)
>>> True

>>> coprime(15, 21)
>>> False

>>> coprime(11, 17)
>>> True

>>> coprime(11, 21)
>>> True

>>> coprime(12, 77) # [1, 2, 2, 3] [1, 7, 11]
>>> True

>>> coprime(790, 121) # [1, 2, 5, 79, 395] [1, 11, 11]
>>> True

```



