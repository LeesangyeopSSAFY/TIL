def check(n, students):
    ch_list = []
    for i in range(1, n+1):
        ch_list += [str(i)]
    
    for j in ch_list:
        if j in students:
            ch_list.remove(j)
    
    return ' '.join(ch_list)

print(check(7, '1 3 5'))