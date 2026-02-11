# =================
# Task 1
# temperature.py
# =================

# answer-1 convert_cel_to_far
def convert_cel_to_far(c):
    return c * 9/5 + 32


# answer-2 convert_far_to_cel
def convert_far_to_cel(f):
    return (f - 32) * 5/9


# main logic
f_input = float(input("Enter a temperature in degrees F: "))
c_result = round(convert_far_to_cel(f_input), 2)
print(f"{f_input} degrees F = {c_result:.2f} degrees C")

c_input = float(input("\nEnter a temperature in degrees C: "))
f_result = round(convert_cel_to_far(c_input), 2)
print(f"{c_input} degrees C = {f_result:.2f} degrees F")



# =================
# Task 2
# invest.py
# =================

# answer-1 invest function
def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {year}: ${amount:.2f}")


# main logic
principal = float(input("\nEnter initial amount: "))
annual_rate = float(input("Enter annual rate (e.g. 0.05 for 5%): "))
years = int(input("Enter number of years: "))

invest(principal, annual_rate, years)



# =================
# Task 3
# factors.py
# =================

number = int(input("\nEnter a positive integer: "))

for i in range(1, number + 1):
    if number % i == 0:
        print(f"{i} is a factor of {number}")



# =================
# Task 4
# University statistics
# =================

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


# answer-1 enrollment_stats
def enrollment_stats(data):
    students = []
    tuition = []

    for uni in data:
        students.append(uni[1])
        tuition.append(uni[2])

    return students, tuition


# answer-2 mean
def mean(values):
    return sum(values) / len(values)


# answer-3 median
def median(values):
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    else:
        return sorted_vals[mid]


# calculations
students, tuition = enrollment_stats(universities)

total_students = sum(students)
total_tuition = sum(tuition)

student_mean = mean(students)
student_median = median(students)

tuition_mean = mean(tuition)
tuition_median = median(tuition)

# formatted output
print("\n******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}\n")

print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}\n")

print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")
print("******************************")



# =================
# Task 5
# is_prime function
# =================

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


