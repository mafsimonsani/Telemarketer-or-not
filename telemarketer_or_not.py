# CCC '18 J1 - Telemarketer or not?

first = int(input())
second = int(input())
third = int(input())
last = int(input())

# Output either ignore if the number matches the pattern for a telemarketer 
# number; otherwise, output answer.
 
if ((first == 8 or first == 9) and (last == 8 or last == 9) and 
    second == third):
    print('ignore')
else:
    print('answer')