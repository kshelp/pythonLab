for k in range(5):
    if(k == 2):
        continue
    print(k)
'''
0
1
3
4
'''

k = 0
while True:
    k = k + 1
    if (k == 2):
        print("continue next")
        continue
    if(k > 4):
        break
    print(k)
'''
1
continue next
3
4
'''
