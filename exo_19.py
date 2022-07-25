def test(a):
    b=5
    def add(a,b):
        tmp=a
        a=b
        b=tmp
    return b
    
func=test(3)
print(func)
    
