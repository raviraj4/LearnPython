#  EXAMPLE 01 >>>

numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
for nums in numlist:
    if nums % 2 == 0:
        print(nums)
some_no = 0
for nums in numlist:
    some_no = nums + some_no
print(f"addition is:\n {some_no}")

# EXAMPLE 02 >>>

# var = int(input("enter how much kg milk you want: "))
# var2 = int(input("enter how much packet of bread: "))
# var3 = int(input("enter how many eggs you want: "))
# k1 = 30*var
# k2 = 20*var2
# k3 = 6*var3
# thislist = [("milk", k1), ("bread", k2), ("eggs", k3)]
# for x, y in thislist:
#     print(x, "total-", y)
# d01 = k1 + k2 + k3
# print("bill-->", d01)
# d1 = k1 + k2 + k3 - 10
# if k1+k2+k3 > 100:
#     print(
#         f"congratulations you gota discount of 10 rupees! \n total price:{d1}")
