def createCounter():
    def counter(j):
        def g():
            return j
        return g
    for j in range(1,6):   
        return counter(j)