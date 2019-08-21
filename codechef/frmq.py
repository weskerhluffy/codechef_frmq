'''
Created on 20 ago 2019

@author: ernestoalvarado
'''

# XXX: https://www.codechef.com/problems/FRMQ
import sys
import os


# XXX: https://gist.github.com/m00nlight/1f226777a49cfc40ed8f
class RMQ:

    def __init__(self, n):
        self.sz = 1
        self.inf = -sys.maxsize
        while self.sz <= n:
            self.sz <<= 1
        self.dat = [self.inf] * (2 * self.sz - 1)

    def update(self, idx, x):
            idx += self.sz - 1
            self.dat[idx] = x
            while idx > 0:
                idx = (idx - 1) >> 1
                self.dat[idx] = max(self.dat[idx * 2 + 1], self.dat[idx * 2 + 2])

    def query(self, a, b):
        return self.query_help(a, b, 0, 0, self.sz - 1)

    def query_help(self, a, b, k, l, r):
        if r < a or b < l:
            return self.inf
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            return max(self.query_help(a, b, 2 * k + 1, l, (l + r) >> 1), self.query_help(a, b, 2 * k + 2, ((l + r) >> 1) + 1, r))


if __name__ == '__main__':
    if "STDIN" in os.environ:
        f = open(os.environ["STDIN"], "r")
        input_fn = f.readline
    else:
        input_fn = input
    n = int(input_fn())
    rmq = RMQ(n)
    a = [int(x) for x in input_fn().strip().split(" ")]
    for i, x in enumerate(a):
        rmq.update(i, x)
    m, x, y = [int(x) for x in input_fn().strip().split(" ")]
    
    r = 0
    for _ in range(m):
        r += rmq.query(min(x, y), max(x, y))
        x, y = ((x % (n - 1)) + 7) % (n - 1), ((y % n) + 11) % n
    print("{}".format(r))
    
