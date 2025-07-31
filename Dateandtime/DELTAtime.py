from datetime import  *
dt1 = datetime(2023, 10, 1, 12, 20, 30)
dt2 = datetime(2020, 10, 2, 14, 25, 35)
td=dt2-dt1
dbvmod =divmod(td.days,365)
print("Difference in years:", dbvmod[0])