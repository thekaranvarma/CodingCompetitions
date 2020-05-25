def spit(n, case):
    n_str = str(n)
    a=''
    for i in range(len(n_str)):
        if n_str[i] =='4':
            a = a+'3'
        else:
            a = a + n_str[i]
    a = int(a)
    b = n -a
    print(f'Case #{case +1}',a,b)

cases = int(input())
n=[]
for case in range(cases):
    n.append(int(input()))
for case in range(cases):
    spit(n[case], case)
