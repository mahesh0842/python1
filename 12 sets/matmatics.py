# set ,subset ,suerset,proper subset ,proper superset,Disjoint sets{not common value in sets}
#set operation in mathmatics
A={1,2,3,5,7}
B={5,7,9,10,11}
print(A.union(B))
print(A.intersection(B))
print('======DIFFRENCE======')
print('FOR A-B = ',A.difference(B))
print('FOR B-A = ',B.difference(A))
print('====SYMMETRIC-DIFFRENCE====')
print(A.symmetric_difference(B))
A={1,2,3,4,5,6,7,8,9,10}
B={1,2,3,5,7}
C={4,6,8,10}
print(B.issubset(A))
print(A.issubset(B))
print(B.isdisjoint(C))
