birthday={'mk':'08/07/2000',
          'ak':'08/06/2004'}
name = input("enter name")
if name in birthday:
    print('mr {} was born on {}'.format(name,birthday[name]))
