"""NESTED FUNCTION
ACCESS NON-LOCAL VARIABLE
RETURN NESTED FUN
CALLER CLASS"""
def closer():
    msg='hello'
    def display():
        print('*'*10)
        print(msg)
        print('*'*10)
    return(display)

