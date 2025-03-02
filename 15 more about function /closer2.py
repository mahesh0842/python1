class dept:
    def __init__(self):
        self.depts={'hr':'Human resource',
                    'acc':'account and finance',
                    'sd':'sales and ditribution',
                    'mkt':'marketing'}
    def __call__(self, dept):
        return self.depts[dept]   

d= dept()
s= d('hr')
print(s) 
print(d('mkt'))       