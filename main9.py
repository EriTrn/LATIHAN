def count_up_to(n):
    num = 0
    while num < n:
        yield num
        num += 1
gen = count_up_to(5)
for i in gen:
    print(i)


# def count_up_to(n):
#     result = []
#     num = 0
#     while num < n:
#         result.append(num)
#         num +=1
#     return result
# gen = count_up_to(5)
# for i in gen:
#     print(i)