#this is useful online isnide the function
def fun():
    try:
        x=int('abc')
        return x
    except Exception as e:
        raise e
    finally:
        print("End of function")

try:        
    res= fun()
    print(res)
except Exception as e:   # <-- Define 'e' here
    print("Caught Exception:", e) 