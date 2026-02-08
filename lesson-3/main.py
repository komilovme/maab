# =================
# List Tasks
# =================

lst = [1, 2, 3, 2, 4, 2, 5]

# answer-1 Count Occurrences
lst.count(2)

# answer-2 Sum of Elements
sum(lst)

# answer-3 Max Element
max(lst) if lst else None

# answer-4 Min Element
min(lst) if lst else None

# answer-5 Check Element
2 in lst

# answer-6 First Element
lst[0] if lst else None

# answer-7 Last Element
lst[-1] if lst else None

# answer-8 Slice List
lst[:3]

# answer-9 Reverse List
lst[::-1]

# answer-10 Sort List
sorted(lst)

# answer-11 Remove Duplicates (order preserved)
list(dict.fromkeys(lst))

# answer-12 Insert Element
lst.insert(2, 99)

# answer-13 Index of Element
lst.index(2) if 2 in lst else -1

# answer-14 Check for Empty List
not lst

# answer-15 Count Even Numbers
sum(1 for x in lst if x % 2 == 0)

# answer-16 Count Odd Numbers
sum(1 for x in lst if x % 2 != 0)

# answer-17 Concatenate Lists
lst + [6, 7]

# answer-18 Find Sublist
sub = [2, 4]
any(lst[i:i+len(sub)] == sub for i in range(len(lst) - len(sub) + 1))

# answer-19 Replace FIRST occurrence
try:
    lst[lst.index(2)] = 100
except ValueError:
    pass

# answer-20 Find Second Largest (safe)
uniq = sorted(set(lst))
uniq[-2] if len(uniq) >= 2 else None

# answer-21 Find Second Smallest (safe)
uniq[1] if len(uniq) >= 2 else None

# answer-22 Filter Even Numbers
[x for x in lst if x % 2 == 0]

# answer-23 Filter Odd Numbers
[x for x in lst if x % 2 != 0]

# answer-24 List Length
len(lst)

# answer-25 Create a Copy
lst.copy()

# answer-26 Get Middle Element
mid = len(lst) // 2
lst[mid] if len(lst) % 2 else lst[mid-1:mid+1]

# answer-27 Max of Sublist
max(lst[1:4]) if lst[1:4] else None

# answer-28 Min of Sublist
min(lst[1:4]) if lst[1:4] else None

# answer-29 Remove Element by Index
if 0 <= 2 < len(lst):
    lst.pop(2)

# answer-30 Check if List is Sorted
lst == sorted(lst)

# answer-31 Repeat Elements
[x for x in lst for _ in range(2)]

# answer-32 Merge and Sort
sorted(lst + [9, 8, 7])

# answer-33 Find All Indices
[i for i, v in enumerate(lst) if v == 2]

# answer-34 Rotate List (right)
k = 2
lst[-k:] + lst[:-k]

# answer-35 Create Range List
list(range(1, 11))

# answer-36 Sum of Positive Numbers
sum(x for x in lst if x > 0)

# answer-37 Sum of Negative Numbers
sum(x for x in lst if x < 0)

# answer-38 Check Palindrome
lst == lst[::-1]

# answer-39 Create Nested List
n = 2
[lst[i:i+n] for i in range(0, len(lst), n)]

# answer-40 Unique Elements in Order
list(dict.fromkeys(lst))


# =================
# Tuple Tasks
# =================

t = (1, 2, 3, 2, 4)

# answer-1 Count Occurrences
t.count(2)

# answer-2 Max Element
max(t) if t else None

# answer-3 Min Element
min(t) if t else None

# answer-4 Check Element
2 in t

# answer-5 First Element
t[0] if t else None

# answer-6 Last Element
t[-1] if t else None

# answer-7 Tuple Length
len(t)

# answer-8 Slice Tuple
t[:3]

# answer-9 Concatenate Tuples
t + (5, 6)

# answer-10 Check if Tuple is Empty
not t

# answer-11 All Indices
[i for i, v in enumerate(t) if v == 2]

# answer-12 Second Largest (safe)
uniq_t = sorted(set(t))
uniq_t[-2] if len(uniq_t) >= 2 else None

# answer-13 Second Smallest (safe)
uniq_t[1] if len(uniq_t) >= 2 else None

# answer-14 Single Element Tuple
(5,)

# answer-15 Convert List to Tuple
tuple(lst)

# answer-16 Check if Sorted
t == tuple(sorted(t))

# answer-17 Max of Subtuple
max(t[1:4]) if t[1:4] else None

# answer-18 Min of Subtuple
min(t[1:4]) if t[1:4] else None

# answer-19 Remove FIRST occurrence by value
if 2 in t:
    i = t.index(2)
    t_new = t[:i] + t[i+1:]
else:
    t_new = t

# answer-20 Create Nested Tuple
n = 2
tuple(t[i:i+n] for i in range(0, len(t), n))

# answer-21 Repeat Elements
tuple(x for x in t for _ in range(2))

# answer-22 Create Range Tuple
tuple(range(1, 11))

# answer-23 Reverse Tuple
t[::-1]

# answer-24 Check Palindrome
t == t[::-1]

# answer-25 Unique Elements in Order
tuple(dict.fromkeys(t))


# =================
# Set Tasks
# =================

a = {1, 2, 3}
b = {3, 4, 5}

# answer-1 Union
a | b

# answer-2 Intersection
a & b

# answer-3 Difference
a - b

# answer-4 Check Subset
a.issubset(b)

# answer-5 Check Element
2 in a

# answer-6 Set Length
len(a)

# answer-7 List to Set
set(lst)

# answer-8 Remove Element
a.discard(2)

# answer-9 Clear Set
set()

# answer-10 Check Empty
not a

# answer-11 Symmetric Difference
a ^ b

# answer-12 Add Element
a.add(10)

# answer-13 Pop Element
a.pop() if a else None

# answer-14 Max Element
max(a) if a else None

# answer-15 Min Element
min(a) if a else None

# answer-16 Filter Even Numbers
{x for x in a if x % 2 == 0}

# answer-17 Filter Odd Numbers
{x for x in a if x % 2 != 0}

# answer-18 Range Set
set(range(1, 11))

# answer-19 Merge & Deduplicate
set(lst + [9, 9, 8])

# answer-20 Disjoint Sets
a.isdisjoint(b)

# answer-21 Remove Duplicates from List
list(set(lst))

# answer-22 Count Unique Elements
len(set(lst))


# =================
# Dictionary Tasks
# =================

d = {"a": 1, "b": 2, "c": 1}

# answer-1 Get Value
d.get("a")

# answer-2 Check Key
"a" in d

# answer-3 Count Keys
len(d)

# answer-4 Get All Keys
list(d.keys())

# answer-5 Get All Values
list(d.values())

# answer-6 Merge Dictionaries
{**d, **{"d": 4}}

# answer-7 Remove Key
d.pop("a", None)

# answer-8 Clear Dictionary
{}

# answer-9 Check Empty
not d

# answer-10 Get Key-Value Pair
key = "a"
val = d.get(key)
(key, val) if val is not None else None

# answer-11 Update Value
d["a"] = 10

# answer-12 Count Value Occurrences
list(d.values()).count(1)

# answer-13 Invert Dictionary
{v: k for k, v in d.items()}

# answer-14 Find Keys with Value
[k for k, v in d.items() if v == 1]

# answer-15 Dictionary from Lists
dict(zip(["x", "y"], [1, 2]))

# answer-16 Check Nested Dictionary
any(isinstance(v, dict) for v in d.values())

# answer-17 Get Nested Value
nested = {"a": {"b": 5}}
nested["a"]["b"]

# answer-18 Default Dictionary
from collections import defaultdict
defaultdict(int)

# answer-19 Count Unique Values
len(set(d.values()))

# answer-20 Sort by Key
dict(sorted(d.items()))

# answer-21 Sort by Value
dict(sorted(d.items(), key=lambda x: x[1]))

# answer-22 Filter by Value
{k: v for k, v in d.items() if v > 1}

# answer-23 Check Common Keys
bool(set(d) & {"a", "z"})

# answer-24 Dictionary from Tuple
dict((("a", 1), ("b", 2)))

# answer-25 First Key-Value Pair
next(iter(d.items()))
