import random
import math
#from Crypto.Util import number

def isCoprime(p, q):
    """returns true if two integers share no factors/divisors in common besides 1

    Args:
        p, q: integers
    """
    if math.gcd(p, q) == 1:
        return True
    else:
        return False

def modInverse(E, pN):
    """calculates the inverse of E modulo pN using extended Euclidean algorithm

    Args:
        E: integer getting modulo by pN
        pN: integer used to mod E by 
    """
    m0 = pN
    y = 0
    x = 1

    while (E > 1):
        q = E // pN
        t = pN
        pN = E % pN
        E = t
        t = y
        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0

    return x

def getKeys(x, y):
    """Get the right N, E and D for keys starting with 2 primes in range from x to y

    Args: 
        x: starting number that could be prime
        y: ending number that could be prime
    
    Returns:
        K1: an array containing public key E, N
        K2: an array containing private key D, N
    """
    # p = number.getPrime(n) # where n is bit size of prime number
    # Step 1: Pick 2 big prime numbers, p and q
    p = 2
    q = 3
    prime_list = []
    for n in range(x, y):
        isPrime = True
        for num in range(2, n):
            if n % num == 0:
                isPrime = False
        
        if isPrime == True:
            prime_list.append(n)

    p = random.choice(prime_list)
    prime_list.remove(p)
    q = random.choice(prime_list)
    
    # Step 2: p * q = N (our public number) -- Trapdoor: prime factorization
    N = (p * q)
    # Step 3: pi(N) = pi(p) * pi(q) = (p - 1)(q - 1)
    pN = (p - 1) * (q - 1)

    # Step 4: Pick E where 1 < E < pi(N) and coprime with N, pi(N)
    eKey_list = []
    for n in range(2, pN):
        if (isCoprime(n, N) == True) and (isCoprime(n, pN) == True):
            eKey_list.append(n)
    E = random.choice(eKey_list)

    # Step 5: Choose D -- D = (k * pi(N) + 1) / E for some integer k
    #                     s.t. k is (k * pi(N) + 1) % E = 0 and D != E
    #                     OR D * E % pi(N) = 1 
    D = modInverse(E, pN)

    # open lock: (E, N) -- public key
    K1 = [E, N]
    # private key: (D, N)
    K2 = [D, N]
    
    # return p, q, N, pN, E, D
    return K1, K2

def encryption(message, Keys):
    """Encrypts the message using the public key

    Args:
        message: a string that will become encoded and transformed
        Keys: array containing the Encryption and Decryption Keys

    Returns:
        ciphertext: single string containing a list of numbers corresponding to each letter in the message after encryption
    """
    E = Keys[0][0]
    N = Keys[0][1]
    # letter by letter encryption
    encoded = list(message.encode('ascii'))
    newEncoded = []
    for n in encoded:
        newAscii = pow(n, E, N)
        newEncoded.append(newAscii)

    ciphertext = " ".join(map(str, newEncoded))

    return ciphertext


def decryption(ciphertext, Keys):
    """Decrypts the message using the private key
    
    Args:
        ciphertext: single string containing a list of numbers corresponding to each letter in the message after encryption waiting to be decrypted
        Keys: array containing the Encryption and Decryption Keys

    Returns:
        message: string that was the ciphertext after decryption
    """
    D = Keys[1][0]
    N = Keys[1][1]
    # letter by letter decryption
    newEncoded = list(map(int, ciphertext.split()))
    encoded = []
    for n in newEncoded:
        oldAscii = pow(n , D, N)
        oldChar = chr(oldAscii)
        encoded.append(oldChar)

    message = "".join(map(str, encoded))

    return message

def verify(original, decrypted):
    """Checks if original string and decrypted string is the same

    Args:
        original: user input message
        decrypted: message after decrypting the encrypted message

    Returns:

    """
    if (original == decrypted):
        return True
    else:
        return False


# load the 2 key arrays into Keys
Keys = getKeys(101, 205)

def main():
    message = input("Enter Your Message: ")
    # print("\nOriginal Message:", message)
    ciphertext = encryption(message, Keys)
    print("\nCiphertext:", ciphertext)
    newMessage = decryption(ciphertext, Keys)
    print("decrypted Message:", newMessage)
    print("\nThe message and the decrypted message is the same?", verify(message, newMessage))


if __name__ == "__main__":
    main()