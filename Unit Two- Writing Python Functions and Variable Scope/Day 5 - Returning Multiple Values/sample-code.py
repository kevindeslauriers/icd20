# print("="*10)
# print("Hello"*4)
# print("-"*45)

def sample_function():
    x = 7
    y = 8
    z = 9
    return x, y, z

a, b, c = sample_function()

print(a)    # 7
print(c)    # 9
print(sample_function())    #(7, 8, 9)

d = sample_function()   # returns (7, 8, 9) the whole list and stores it in the 1 variable
print(d*3)

#h, i = sample_function()    # not happy because it returns 3 things and we gave it 2 (so it is confused)