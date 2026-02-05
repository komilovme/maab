#==============================
# Number Data Type Questions
#==============================

# answer - 1
# print(f"{float(input()):.2f}")

# answer - 2
# nums = [int(i) for i in input().split()]
# print(max(nums), min(nums))

# answer - 3
# km = int(input())
# print(f"{km * 1000} km and {km * 1000 * 100} sm")

# answer - 4
# a, b = map(int, input().split())
# print(a/b, a%b)

# answer - 5
# selsiy = int(input())
# print(selsiy * (9/5) + 32, "°F")

# answer - 6
# print(int(input()[-1]))

# answer - 7
# print(["Juft", "Toq"][int(input()) % 2])

# ===============================
# String Questions:
# ===============================

# answer - 1
# name = input()
# birth = int(input())
# print(f"{name} sizning yoshingiz {2026 - birth}")

# answer - 2
# s = "LMaasleitbtui"
# fCar = s[0] + s[2] + s[4] + s[6] + s[8] + s[10] + s[12]
# sCar = s[1] + s[3] + s[5] + s[7] + s[9] + s[11]
# print(fCar, sCar)

# answer - 3
# data = input()
# print(len(data))
# print(data.upper(), data.lower())

# answer  - 4
# text = input()
# print("YES" if text == text[::-1] else "NO")

# answer - 5
# unli = "aeiou"
# undosh = "qwrtypsdfghjklzxcvbnm"
# text = input()
# count_unli = 0
# count_undosh = 0
# for ch in text :
#   if ch in unli:
#     count_unli += 1
#   else:
#     count_undosh += 1
# print(f"Unli harflar : {count_unli}, Undosh harflar : {count_undosh}")

# answer - 6
# fString = input()
# sString = input()
# if fString in sString or sString in fString:
#   print("YES")
# else:
#   print("NO")

# answer - 7
# text = "Men olmalarni yaxshi ko'raman"
# newFruit = input()
# text = text.replace("olma", newFruit)
# print(text)

# answer - 8
# text = input()
# print(text[0], text[-1])

# answer = 9
# print(input()[::-1])

# answer - 10
# text = input()
# print(text.count(" ") + 1)

# answer - 11
# print(input().isalnum())

# answer  - 12
# words = [str(i) for i in input().split()]
# print("-".join(words))

# answer  - 13
# text = input().replace(" ", "")
# print(text)

# answer - 14
# fText, sText = map(str, input().split())
# print("YES" if len(fText) == len(sText) else "NO")

# answer - 15
# words = [str(_) for _ in input().split()]
# shortText = ""
# for ch in words:
#   shortText += ch[0]
# print(shortText.upper())

# naswer - 16
# text = input()
# symbol = input()
# text = text.replace(symbol, "")
# print(text)

# answer - 17
# unli = "aeuio"
# text = input()
# for ch in text :
#   if ch in unli:
#     text = text.replace(ch, "*")
# print(text)

# answer - 18
# words = [str(i) for i in input().split()]
# print(words[0], words[-1])

# ==============================================
# Boolean Data Type Questions:
# ==============================================

# answer - 1
# username = input("Your username: ")
# password = input("Password : ")
# if username != "" and password != "" :
#   print(True)
# else:
#   print(False)

# naswer - 2
# a, b = map(int, input().split())
# if a == b :
#   print("Equal")
# else:
#   print("Not Equal")

# answer = 3
# print(["Just", "Toq"][int(input()) % 2])

# answer - 4
# a, b, c = map(int, input().split())
# if len(set(a, b, c)) == 3:
#   print(False)
# else: print(True)

# answer - 5
# a = input()
# b = input()
# if len(a) == len(b):
#   print(True)
# else:
#   print(False)

# answer - 6
# a = int(input())
# if a % 3 == 0 or a % 5 == 0:
#   print(True)
# else:
#   print(False)

# answer - 7
# part 1
# a, b = map(float, input().split())
# if a + b > 50.8:
#   print("Katta")
# else: print("Kichik")

#part 2
# a = int(input())
# if 10 <= a <= 10:
#   print(True)
# else:
#   print(False)