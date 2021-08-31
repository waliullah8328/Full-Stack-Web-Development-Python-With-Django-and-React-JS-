# Loop -- এর উদাহরন লাটিম (লাটিম যেমন তার চারপাশ ঘুরে তেমনি লুপ ও ঘুরে)

# Loop --- 1.For Loop & 2.While Loop

# For Loop
for i in range(10):  # 0 -- 9  print করবে । কারন i এর মান ০ থেকে শুরু হয়েছে
    print(i)

print('*'*20)
for i in range(1, 10):  # ১ -- ৯   print করবে । এখানে শুরুর  ১ এবং শেষের ৯ (n-1)
    print(i)

print('*'*20)
for i in range(1, 10, 2):  # এখানে ২ করে বারবে
   print(i)

print('*'*20)
sum = 0
for i in range(1, 10, 2):  # এখানে ১ থেকে ৯ অব্ধি বিজোড় সংখার যোগফ্ল print করবে।
   sum = sum + i

print(sum)
print('*'*20)

# While Loop

i = 1
n = 10

while i <= n:  # ১ -- ১০   print করবে । এখানে শুরুর  ১ এবং শেষের ১০
    print(i)
    i = i + 1

print('*'*20)
i = 1
n = 10
sum = 0

while i <= n:  # এখানে ১ থেকে 10 অব্ধি  সংখার যোগফল print করবে।
    sum = sum + i
    i = i + 1

print(sum)

