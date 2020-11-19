'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
num_to_type = {
    1 : 'WS',
    2 : 'MS',
    3 : 'AS',
    4 : 'AS',
    5 : 'MS',
    6 : 'WS',
    7 : 'WS',
    8 : 'MS',
    9 : 'AS',
    10 : 'AS',
    11 : 'MS',
    0 : 'WS'
}

num_to_num = {}
for i in range(12):
    num_to_num[i] = (12-i+1)%12
# print num_to_num
for _ in range(input()):
    n = input()
    # print "num num"
    # print n%12
    ehe = num_to_num[n%12]+(n-(n%12))
    ans = str(ehe) + " " + num_to_type[n%12]
    print ans



