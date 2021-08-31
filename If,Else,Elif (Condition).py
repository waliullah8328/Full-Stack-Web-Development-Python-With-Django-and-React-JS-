# Condition
"""
1. if -- যদি
2. else -- যদি না হয় তবে
3. elif -- যদি এর পরে যদি কিছু থাকে
"""

is_varsity_open = True

if is_varsity_open == True:
    print("I will go")

else:
    print("I will not go")


# Nested Condition

is_school_open = True
lockdown = True

if is_school_open == True:
    print("It's True,but is there lockdown?")
    if lockdown == True:
        print("I will not go")

    else:
        print("I will go")

else:
    print("It's not True")

#  Elif
mark = 87
if mark >=80:
    print("A+")
elif mark >=70 and mark < 80:
    print("A")
elif mark >=60 and mark < 70:
    print("A-")
else:
    print("Fail")