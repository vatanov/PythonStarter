# Get max item of the list using max() function
my_list = [1, -98, 56783456, 43, 7, -312334, 9, 56, 672]
max_item = max(my_list)
print(max_item)

# Get max item of the list using loop and condition
a = 0
for i in my_list:
    if i > a:
        a = i

print(a)
