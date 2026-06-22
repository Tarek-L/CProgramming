class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        def execOp(l, a, b):
            if l == '+':
                return int(a) + int(b)
            if l == '-':
                return int(b) - int(a)
            if l == '*':
                return int(a) * int(b)
            return int(int(b) / int(a))

        ops = {'+','*','-','/'}
        s = []
        for i in tokens:
            if i in ops:
                s.append(execOp(i, s.pop(), s.pop()))
            else:
                s.append(i)

        return int(s[0])
#        def solve(t):
#            res = []
#            res.append(t.pop())
#            arg1 = t.pop()
#            if arg1 in ops:
#                t.append(arg1)
#                res.append(solve(t))
#            else:
#                res.append(arg1)
#            arg2 = t.pop()
#            if arg2 in ops:
#                t.append(arg2)
#                res.append(solve(t))
#            else:
#                res.append(arg2)
#
#            return execOp(res)
#
#        return solve(tokens)

    
        
