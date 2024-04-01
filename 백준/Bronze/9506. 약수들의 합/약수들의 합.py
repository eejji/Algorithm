while True:
    n = int(input())
    nli= []
    sum=0

    if n == -1:
        break

    for i in range(1, n//2+1):
        if n % i == 0:
            nli.append(i)
            sum += i
    
    if sum == n:
        temp = ' + '.join(str(i) for i in nli)
        print(n, '=', temp)
    else:
        print(f"{n} is NOT perfect.")
