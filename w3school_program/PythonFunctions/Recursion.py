def userRecusion(k):
    if (k) > 0:
        r = k + userRecusion(k - 1)
        print(r)
    else:
        r = 0
    return r
print("\n\nRecursion Example Results")

userRecusion(6)









# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)
