def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def prime_counts(L):
    count=0
    for i in range(len(L)):
        if is_prime(i) and is_prime(L[i]):
            count+=1
    return count

print(prime_counts([1,2,3,4,5,6,7]))