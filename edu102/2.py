def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

def solve(s1,s2):
    a = len(s1)
    b = len(s2)
    lcm = compute_lcm(a,b)
    nih1 = lcm/a
    nih2 = lcm/b
    if s1*nih1 == s2*nih2:
        return s1*nih1
    return -1


for _ in range(input()):
    s1 = raw_input()
    s2 = raw_input()
    
    print solve(s1,s2)