class Solution:
    def reverse(self, x: int) -> int:
        r=str(x)
        if(r[0]=='-'):
            a=r[1:len(r)]
            a=a[::-1]
            a=str(int(a))
            a='-'+a
            if(int(a)>(2**31-1) or int(a)<(-2**31) ):
                return 0
        else:
            a=r[0:len(r)]
            a=a[::-1]
            a=str(int(a))
            if(int(a)>(2**31-1) or int(a)<(-2**31) ):
                return 0
        return a