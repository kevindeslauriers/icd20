# def count_char(str):
#     str = str.upper()

#     char_count = [0]*26

#     for s in str:
#         char_count[ord(s)-65]+=1

#     return char_count


# print(count_char("abczaaac"))


def mystery(nums):
    result = []

    for index in range(len(nums)):
        if nums[index] < 0:
            result.append(index)
    
    return result


print(mystery([1,6,4,-2,-4,0,8,-1]))



