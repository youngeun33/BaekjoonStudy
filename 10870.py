import sys
sys.setrecursionlimit(10**6)
dict = {1:1,2:1}
def fibo(n):
    if n in dict:
        return dict[n]
    else:
        output = fibo(n-1) + fibo(n-2)
        dict[n] = output
        return output
a  = int(input())
print(fibo(a))