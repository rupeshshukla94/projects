class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        a=[]
        
        l=[]
        def printAllKLength(set, k,l):
            n = len(set)
            printAllKLengthRec(set, "", n, k,l)
        
        def printAllKLengthRec(set, prefix, n, k,l):
            if (k == 0) :
                l+=[prefix]
                return
            for i in range(n):
                newPrefix = prefix + set[i]
                printAllKLengthRec(set, newPrefix, n, k - 1,l)

        d={
                '2':["a","b","c"],
                '3':["d","e","f"],
                '4':["g","h","i"],
                '5':["j","k","l"],
                '6':["m","n","o"]
            }
        for i in digits:
            a.extend(d[i])
        a=list((a))
        printAllKLength(a,len(digits),l)
        print(l)
        
            

        