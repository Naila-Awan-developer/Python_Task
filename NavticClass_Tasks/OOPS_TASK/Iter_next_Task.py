class PrimeIterator:#Iterator class to generate the first n prime numbers.
    def __init__(self, n):#Initialize PrimeIterator object."""
        self.n = n
        self.count = 0
        self.num = 2
    def __iter__(self):#Return the iterator object itself.
        return self

    def __next__(self):#Return the next prime number.
        if self.count < self.n:
            while not self.is_prime(self.num):
                self.num += 1
            prime = self.num
            self.num += 1
            self.count += 1
            return prime
        else:
            raise StopIteration
    @staticmethod
    def is_prime(num):#Check if a number is prime.
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
# Example usage:
n = 10
prime_iterator = PrimeIterator(n)
for prime in prime_iterator:
    print(prime)


