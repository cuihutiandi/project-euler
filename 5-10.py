'''
Sum square difference: The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385. 
The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025. 
Hence the difference between the sum of the squares of the first ten natural numbers and 
the square of the sum is 3025 - 385 = 2640. 
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


'''

def sum_square_difference(n):
    sum_of_squares = sum(i**2 for i in range(1, n+1))
    square_of_sum = sum(range(1, n+1)) ** 2
    return square_of_sum - sum_of_squares

print(sum_square_difference(100))

'''
In this code, sum_square_difference calculates and returns the difference between 
the square of the sum and the sum of the squares of the first n natural numbers. 
The sum function is used with a generator expression to calculate the sum of the squares and the sum, 
and the range function is used to generate the sequence of numbers from 1 to n.

However, this solution could be made more efficient by using mathematical formulas 
for the sum of natural numbers and the sum of squares of natural numbers:

The sum of the first n natural numbers is n*(n+1)/2.
The sum of the squares of the first n natural numbers is n*(n+1)*(2n+1)/6.

This solution is faster because it calculates the sum and the sum of squares in constant time, 
while the previous solution requires linear time.
'''

def sum_square_difference(n):
    sum_of_squares = n*(n+1)*(2*n+1) // 6
    square_of_sum = (n*(n+1) // 2) ** 2
    return square_of_sum - sum_of_squares

print(sum_square_difference(100))


'''
10001st prime: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. 
What is the 10,001st prime number?

'''

def nth_prime(n):
    primes = [2]
    attempt = 3
    while len(primes) < n:
        if all(attempt % p > 0 for p in primes):
            primes.append(attempt)
        attempt += 2
    return primes[-1]

print(nth_prime(10001))

'''
In this code, nth_prime finds and returns the n-th prime number. 
It keeps a list of prime numbers found so far, starting with 2. 
Then it checks odd numbers starting from 3 (stored in attempt). 
For each number, it checks if it's divisible by any of the primes found so far (attempt % p > 0 for p in primes). 
If it's not divisible, it's a prime number, so we add it to the list. 
We stop as soon as we find n prime numbers. Finally, we return the last prime found (primes[-1]).

However, this solution is not very efficient, as it tests divisibility by all primes found so far, 
not just those up to the square root of the number. Also, as the list of primes grows, 
checking divisibility becomes slower. But for finding the 10,001st prime, it works within a reasonable time.

To improve the speed, we could use a more complex algorithm such as the Sieve of Eratosthenes, 
but implementing it to find the n-th prime number is more challenging.

The Sieve of Eratosthenes algorithm can be used for a more efficient calculation of the n-th prime. 
However, it requires an upper limit to be known. 
Since we don't know the upper limit for the 10,001st prime, we might have to guess and check. 
A common approximation used for the n-th prime number is n * log(n) + n * log(log(n)) for n >= 6, 
which is derived from the prime number theorem. We'll use this as an initial guess and increase if needed.
'''

import numpy as np

def nth_prime(n):
    upper_bound = int(n * np.log(n) + n * np.log(np.log(n)))  # Estimate upper bound
    sieve = np.ones(upper_bound, dtype=bool)  # Initialize sieve
    sieve[0:2] = False  # 0 and 1 are not prime
    for i in range(2, int(np.sqrt(upper_bound)) + 1):
        if sieve[i]:
            sieve[i*i::i] = False
    primes = np.where(sieve)[0]
    while len(primes) < n:  # If our initial guess was too low
        upper_bound *= 2
        sieve = np.ones(upper_bound, dtype=bool)
        sieve[0:2] = False
        for i in range(2, int(np.sqrt(upper_bound)) + 1):
            if sieve[i]:
                sieve[i*i::i] = False
        primes = np.where(sieve)[0]
    return primes[n-1]

print(nth_prime(10001))

'''
 this code, nth_prime first estimates an upper bound for the 10,001st prime (upper_bound). 
 It initializes a boolean array sieve of this size, with all elements set to True (indicating potential primes). 
 It then marks as False the multiples of each number up to the square root of upper_bound 
 (since any non-prime number must have a factor no greater than its square root). 
 The remaining True values in the sieve are primes. 
 If the sieve doesn't contain enough primes, the size of the sieve is doubled and the process is repeated.

This code uses NumPy for efficient array operations. 
It's much faster than the simple primality test for large n, 
because the Sieve of Eratosthenes identifies primes in a "batch" process, avoiding redundant work. 
However, it uses more memory, because it needs to store the entire sieve in memory.

'''

'''
Largest product in a series: 
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

(Here is provided a 1000-digit number)

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. 
What is the value of this product?
'''

def largest_product_in_series(n, series):
    largest_product = 0
    for i in range(0, len(series) - n):
        product = 1
        for j in range(i, i + n):
            product *= int(series[j])
        if product > largest_product:
            largest_product = product
    return largest_product


'''
series=
"7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494
95459501737958331952853208805511125406987471585238630507156932909632952274430435576689664895044524452316173185640309871
11217223831136222989342338030813533627661428280644448664523874930358907296290491560440772390713810515859307960866701724
27121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483
95864467063244157221553975369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535
10047482166370484403199890008895243450658541227588666881164271714799244429282308634656748139191231628245861786645835912
45665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987
87992724428490918884580156166097919133875499200524063689912560717606058861164671094050775410022569831552000559357297257
1636269561882670428252483600823257530420752963450"
'''
print(largest_product_in_series(13, series))


'''
In this code, largest_product_in_series calculates and returns the largest product of n adjacent digits in series. 
It does this by iterating over all possible n-digit substrings of series (from series[i] to series[i + n - 1]), 
calculating the product of the digits in each substring, and updating largest_product 
if the product is greater than the current largest_product.

This solution is straightforward and works well for the problem as stated,
but it's not very efficient because it re-calculates the product from scratch for each substring. 
If performance is a concern, this code could be optimized to keep a running product 
and update it for each new digit by dividing out the digit leaving the substring and multiplying in the digit entering the substring. 
However, that would make the code more complex.
'''

def largest_product_in_series(n, series):
    largest_product = 0
    product = 1
    queue = []
    for digit in series:
        digit = int(digit)
        queue.append(digit)
        product *= digit
        if len(queue) > n:
            product //= queue[0]  # remove the first digit from product
            queue.pop(0)  # remove the first digit from queue
        if product > largest_product and len(queue) == n:
            largest_product = product
        if digit == 0:  # reset for zero
            product = 1
            queue = []
    return largest_product


'''
This solution maintains a queue with n elements, corresponding to the sliding window. 
As each digit is added to the queue, it's also multiplied into product. 
If the queue's size exceeds n, the first digit in the queue is removed and divided out of product. 
The maximum product seen so far is updated if the product is greater and the queue's size is n.

We also reset the product and queue when a 0 is encountered since it would nullify the product. 
This optimization reduces the time complexity from O(n^2) to O(n), 
which would be a substantial improvement for large series.
'''

'''
Special Pythagorean triplet: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def find_pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if a*a + b*b == c*c:
                return a*b*c

print(find_pythagorean_triplet(1000))

'''
In this code, find_pythagorean_triplet iterates over all pairs of a and b less than n, 
then computes c as n - a - b (since a + b + c must equal n). 
It checks if a, b, and c form a Pythagorean triplet (a*a + b*b == c*c) and, 
if they do, returns their product. This brute-force solution has a time complexity of O(n^2), 
but it works reasonably quickly for n = 1000 because the inner loop doesn't start from 1 
but from a, which reduces the number of iterations.

Given a + b + c = 1000 and a² + b² = c², we can substitute c = 1000 - a - b into the second equation, 
yielding a² + b² = (1000 - a - b)². 
Expanding and rearranging terms gives a² + b² = 1000000 + a² + b² - 2000a - 2000b + 2ab,
 which simplifies to 0 = 1000000 - 2000a - 2000b + 2ab. Then, solving for b gives b = (1000000 - 2000a) / (2000 - 2a).

We can loop over a from 1 to 999, calculate b using the above equation, and check if b is an integer. 
If b is an integer and less than a (since a < b < c), 
then a, b, and c = 1000 - a - b form the required Pythagorean triplet. 
Here is the Python code that implements this optimized solution:
'''



def find_pythagorean_triplet(n):
    for a in range(1, n):
        b = (n*n - 2*n*a) / (2*n - 2*a)
        if b.is_integer() and b > a:
            c = n - a - b
            return int(a*b*c)

print(find_pythagorean_triplet(1000))


'''
This code loops over a from 1 to n - 1, computes b as (n*n - 2*n*a) / (2*n - 2*a), 
and checks if b is an integer and greater than a. If these conditions are met, 
it computes c as n - a - b and returns the product a*b*c. 
This solution is more efficient than the previous one because it only requires a single loop, 
making it an O(n) algorithm.

'''


'''
Summation of primes: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Here's a simple Python solution to this problem using the Sieve of Eratosthenes, 
a well-known algorithm for finding all prime numbers up to a given limit:
'''

def sum_of_primes(n):
    sieve = [True] * n
    sieve[0:2] = [False, False]
    for i, is_prime in enumerate(sieve):
        if is_prime:
            for j in range(i*i, n, i):
                sieve[j] = False
    primes = [p for p, is_prime in enumerate(sieve) if is_prime]
    return sum(primes)

print(sum_of_primes(2000000))

'''
In this code, sum_of_primes first creates a boolean list (sieve) of size n, with all elements initially set to True. 
It then sets sieve[0] and sieve[1] to False (since 0 and 1 are not prime). 
Next, it iterates over sieve and, for each prime number it finds (i.e., where sieve[i] is True), 
it marks its multiples as not prime (by setting sieve[j] to False for j = i*i, i*(i+1), i*(i+2), ..., n). 
Finally, it creates a list of primes (the indices of True values in sieve) and returns their sum. 
This algorithm has a time complexity of O(n log log n), which is efficient enough for n = 2000000.

'''

def sum_of_primes(n):
    sieve = [True] * n
    sieve[0:2] = [False, False]
    sum = 0
    for i, is_prime in enumerate(sieve):
        if is_prime:
            sum += i
            for j in range(i*i, n, i):
                sieve[j] = False
    return sum

print(sum_of_primes(2000000))

'''
In this optimized version, we keep a running total of the sum of the prime numbers 
instead of storing all prime numbers in a separate list, which significantly reduces memory usage. 
We also stop the inner loop once j exceeds n, which can potentially speed up the computation.

The time complexity of this solution is still O(n log log n), which is the best possible time complexity 
for this problem because it involves finding all primes less than n. 
However, this version uses less memory and may run faster in practice because it performs fewer operations inside the loops.

'''
