'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
# Write your code here
for _ in range(input()):
    text1 = raw_input()
    text2 = raw_input()

    dict1 = {}
    dict2 = {}
    for i in text1:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
        if i not in dict2:
            dict2[i]=0
    # print dict1
    for j in text2:
        if j in dict2:
            dict2[j]+=1
        else:
            dict2[j]=1
        if j not in dict1:
            dict1[j]=0
    ans = 0
    # print dict1
    # print dict2
    for i in dict1:
        ans += abs(dict1[i]-dict2[i])
        dict1[i] = 0
        dict2[i] = 0
    for i in dict2:
        ans += abs(dict1[i]-dict2[i])
    print ans
