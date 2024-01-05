
# def bm(string, find):
#     # find +='*'
#     #rfind = find[::-1]
#     table = [(j,i) for i, j in enumerate(find[::-1])]
#     table[0] = (find[-1], len(find))
    

#     for i in range(len(table)):
#         sub = find[i:len(find):-1]
#         print(sub)
#         # if table[i][0] in sub:
#         #     for j in range(len(sub)):
                
#     table.reverse()
#     table.append(('*',len(find)))
#     print(table)
#     print(find)

s = 'Привёт, Лёша!'
f = 'Лёша!'


def get_table(find):
    table = {} 
    for i, j in enumerate(find[-2::-1],1):
        if j not in table.keys():
            table[j] = i
            
    if find[-1] not in table.keys(): 
        table[find[-1]] = len(find)
    
    table['*']=len(find)
    return table

print(get_table(f))


def dm(str, find, tab):
    k = 0
    for i in range(len(str)):
        for j in reversed(range(len(find))):
            
            if str[i+j] == find[j]:
                k+=1
            else:
                k = 0
                if str[i] in tab.keys():
                    i += tab[str[i]]
                else:
                    i += tab['*']
                break

            if k == len(find): return True, k
    return False
print(dm(s, f, get_table(f)))

