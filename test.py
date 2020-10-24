def find_it(seq):
    sorted_list = sorted(seq)
    count = 1
    if len(sorted_list) == 1:
        return sorted_list[0]
    for i in sorted_list:
        a = 0
        b = a + 1
        if sorted_list[a] == sorted_list[b]:
            count += 1
        
            
        


print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))