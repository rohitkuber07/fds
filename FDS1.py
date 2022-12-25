def intersection(l1,l2):
    res = []
    for student in l1:
        if student in l2:
            res.append(student)
    return res

a = [1,2,3,4,5,6,7]
b = [2,3,6,7,10]
c = [2,4,6,8,10,12]
print(f"A={a}|\nB={b}|\nc={c}\n")
print(f"a) List of student who play both cricket and badminton = ", end=" ")
print(intersection(a, b))

def union(l1,l2):
    res = l2.copy()
    for student in l1:
        if not student in l2:
            res.append(student)
    return res

def diff(l1,l2):
    res = []
    for student in l1:
        if not student in l2:
            res.append(student)
    return res

u = union(a, b)
i = intersection(a, b)
print(f"b) List of student who play either cricket or badminton but not both =",end=" ")
print(diff(u, i))

diffcb = diff(c, b)
print(f"c) Number of student who play neither cricket nor badminton =", end=" ")
print(diff(diffcb, a))

unionac = union(a, c)
print(f"c) number of student who play neither cricket nor badminton =", end=" ")
print(diff(unionac, b))
