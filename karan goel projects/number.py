def callcPi(limit):
    q, r, t, k, n, l, = 1, 0, 1, 1, 3, 3
    decimal = limit
    counter = 0
    while counter != decimal + 1:
        if 4*q+r-t < n*t:
            yield n
            if counter == 0:
                yield '.'
            if decimal == counter:
                print('')
                break
            counter += 1
            nr = 10*(r-n*t)
            n = ((10*(3*q+r))//t) - 10*n
            q *= 10
            r = nr
        else:
            nr = (2*q+r)*l
            nn = (q*(7*k)+2+(r*l)) // (t*l)
            q *= k
            t *= l
            k += 1
            l += 2
            n = nn
            r = nr

def main():
    x = int(input("Enter the number of decimals to calculate to:\n"))
    while x > 1000:
        print("Try within reason")
        x = int(input("Enter the number of decimals to calculate to:\n"))
    else:
        pi_digits = callcPi(x)
        i = 0
        
        for d in pi_digits:
            print(d, end='')
            i += 1
            if i == 40:
                print("")
                i = 0

if __name__ == '__main__':
    main()