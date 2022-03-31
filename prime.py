def is_prime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                print("False")
                break
        else:
            print("True")
    else:
        print("False")