class Solution:
    def myAtoi(self, s: str) -> int:
        t=""
        start=True
        sign=[]
        l=['-','+',' ']
        for i in s:
            if not i.isnumeric():
                if i not in l:
                    break
            if(len(sign)>1):
                break
            
            if(i==" " and start):
                continue
            if(i==" " and not start):
                break
            if not i.isnumeric() and not start:
                break
            if i=="-" or i=="+":
                sign.append(i)
                start=False
            else:
                t+=i
                start=False
                continue
       
        if len(sign)>0:
            if sign[0]=="-" and len(sign)==1 and len(t)>0:
                t="-"+t
            if sign[0]=="-" and len(sign)==1 and len(t)==0:
                return 0
        if(len(t)==0):
            return 0
        t=int(t)
        if(t>2**31-1):
            return 2**31-1
        if(t<-2**31):
            return -2**31
        return t;