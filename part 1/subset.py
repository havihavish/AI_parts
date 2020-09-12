subset_lst = [int(i) for i in input("Enter the subset numbers: ").split()]

def generate_subset(lst):
    if len(lst) == 1: return [[],[lst[0]]]
    head = lst[0]
    tail = lst[1:]
    ans = generate_subset(tail)
    for i in range(len(ans)):
        ans.append([head]+ans[i])
    return ans
print(generate_subset(subset_lst))