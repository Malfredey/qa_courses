# feet = 10
# inches = 5
# feet *= 30.48
# inches *= 2.54
# sum_all = feet + inches
# print(sum_all, "cm")

# sum_n = 0
# for value in range(0, 3):
#     sum_n += value
#     print(value)
# print(sum_n)
#
# n = 10
# sum_n = 0
# for value in range(1, n + 1):
#     sum_n += value
# print(sum_n)


# list_of_values = [10, 5, 12, 25, 13, 6, 4, 22, 106, 94, 46]
# for value in list_of_values:
#     if value / 4 > 5:
#         print(value)

# HOME_WORK 2.1
# def palindrome(text):
#     text = text.lower()
#     text = ' '.join(char for char in text if char.isalpha())
#     return text == text[::-1]
# assert palindrome("mom") == True
# assert palindrome("dom") == False


# HOME_WORK 2.2
# def count_symbols(text: str | int):
#     text = str(text)
#     total = len(text)
#     return total
# print(count_symbols(12))


# HOME_WORK 2.3
# from functools import reduce
# from operator import mul
# def drakon(*args):
#     counting = {}
#     for char in args:
#         if len(args) <= 1:
#             return list({args})
#         elif len(args) >=1:
#             return list(str({reduce(mul, args)}))
# print(drakon (10, 10))

# def drakon(*args):
#     total = 1
#     for char in args:
#         total *= char
#     return list(str(total))
#
# print(drakon(10, 10))


# HOME_WORK 2.4
# def password (*args):
#     args = str(args)
#     args = args.replace(" ", "").replace("'", "").replace('"', '')
#     for count in args:
#         if len(args) <=10:
#             return "min 8 symbols"
#         if not any(char.isdigit() for char in args):
#             return "password must contain at least one number"
#         if not any(char.isupper() for char in args):
#             return "password must contain at least one uppercase letter"
#         else:
#             return "Password has been created successfully"
# print(password("qqqqQqq1q"))