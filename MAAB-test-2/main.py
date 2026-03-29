# Puzzle 1

s = input()
find = False
for ch in s:
    if s.count(ch) == 1:
        find = True
        print(s.index(ch) + 1)
        break
    else:
        continue

if not find :
    print(-1)

# Puzzle 2
nums = [int(i) for i in input().split()]
n = len(nums)
for num in nums:
    target = n // 2
    if nums.count(num) > target:
        print(f"Satr majori : {num}")
        break
    else:
        continue

# Puzzle 3

nums = [int(_) for _ in input().split()]
mx = max(nums)
for k in range(1, mx + 1):
    nums.append(k)
for num in nums:
    if nums.count(num) == 1:
        print(num)
        break

# Puzzle 4
def Fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return Fib(n - 1) + Fib(n - 2)
n = int(input())
mod = 10 ** 19 + 7
res = []
for i in range(1, mod + 1):
    if Fib(i) < n:
        res.append(Fib(i))
    else:
        break
print(res)

# Puzzle 5
nums = [int(i) for i in input().split()]
ans = []
for i in range(len(nums)):
	gen = nums.copy()
	gen.pop(i)
	res = 1
	for j in gen :
		res *= j
	ans.append(res)
print(ans)		
