a = [1,2,3]


try :
    a.index(5)
except ValueError as e:
    print(e)