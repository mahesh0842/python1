def net_sal(basic,allowance,deduction):
    print(basic)
    print(allowance)
    print(deduction)
    net = basic + allowance - deduction
    return net
n = net_sal(8000,6000,200)
print(n)