# https://codeforces.com/problemset/problem/2193/C 
# this is going to be ugly

import sys
import threading

input = sys.stdin.readline

def inp(): return int(input())
def inlt(): return list(map(int, input().split()))
def insr(): return list(input().strip())
def invr(): return map(int, input().split())

def fixArr(arr, n):
    for i in range(n-1,0,-1):
        if arr[i] > arr[i-1]:
            arr[i-1] = arr[i]


def solve():
    # parse input
    n, q = invr()
    l1 = inlt()
    l2 = inlt()
    # create the most optimal array only left to use operation one on this array and calc the sum
    arr = [max(a,b) for a,b in zip(l1,l2)]
    fixArr(arr,n)
    # cache
    tab = [arr[0]]
    for i in range(1,n):
        k = arr[i] + tab[i-1]
        tab.append(k)
    res = []
    for _ in range(q):
        l, r = invr()
        lm = tab[r-1] 
        if l-2 >= 0:
            lm -= tab[l-2]
        res.append(lm)
    print(*res) 

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()
