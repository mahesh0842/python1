class negativeError(Exception):
    pass
def area(length,breadth):
    if length  >= 0 and breadth >= 0:
        
        a= length*breadth
        return a
    else:
        raise negativeError("-ve dimension not allowed")
print(area(-5, 6))