
file = open("primeText.txt", "w")
num = 2
primes = ""
while num < 10000:
    for count in range(2, int(num/2)):
        rem = num % count
        if rem == 0:
            break
    else:
        primes = primes + str(num) + ","
        file.write(str(num) + ",")
    num = num + 1
    print(num)
file.close()
print(primes)