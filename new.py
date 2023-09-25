import time
# Approach 1: Using in operator
start_time = time.time()
main_list = [11, 21, 19, 46]

if 19 in main_list:
    print("Element is in the list")
else:
    print("Element is not in the list")

end_time = time.time()
print(f"Approach 'in operator' took {end_time - start_time:.4f} seconds.")

# Approach 2: Using enumerate
start_time = time.time()
main_list = [11, 21, 19, 18, 46]
search_element = 19
found_element = False

for index, item in enumerate(main_list):
    if item == search_element:
        found_element = True
        print(f"{search_element} found_element at index {index}")
        break

if not found_element:
    print(f"{search_element} not found_element in the list")
end_time = time.time()
print(f"Approach 'enumerate()' took {end_time - start_time:.4f} seconds.")

# Approach 3: Using list comprehension to get indices
start_time = time.time()
main_list = [11, 21, 19, 18, 46]
search_element = 19

indices = [index for index, item in enumerate(
            main_list) if item == search_element]

if indices:
  print(f"{search_element} found at indices {indices}")
else:
  print(f"{search_element} not found in the list")
end_time = time.time()
print(f"Approach 'list comprehension' took {end_time - start_time:.4f} seconds.")

# Approach 4: Using index() method
start_time = time.time()
streaming = ['netflix', 'hulu', 'disney+', 'appletv+']
index = streaming.index('disney+')
print('The index of disney+ is:', index)
end_time = time.time()
print(f"Approach 'list comprehension' took {end_time - start_time:.4f} seconds.")

# Approach 5: Using count() method
start_time = time.time()
main_list = [11, 21, 19, 46]
count = main_list.count(21)

if count > 0:
  print("Element is in the list")
else:
  print("Element is not in the list")
end_time = time.time()
print(f"Approach 'count()' took {end_time - start_time:.4f} seconds.")

# Approach 6: Using list comprehension with any()
start_time = time.time()
main_list = [11, 21, 19, 46]
output = any(item in main_list for item in main_list if item == 22)
print(str(bool(output)))
end_time = time.time()
print(f"Approach 'index()' took {end_time - start_time:.4f} seconds.")

# Approach 7: Using filter() method
start_time = time.time()
main_list = [11, 21, 19, 46]
filtered = filter(lambda element: element == 19, main_list)
print(list(filtered))
end_time = time.time()
print(f"Approach 'filter()' took {end_time - start_time:.4f} seconds.")

# Approach 8: Using the for loop
start_time = time.time()
main_list = [11, 21, 19, 46]

for i in main_list:
  if(i == 46):
    print("Element Exists")
end_time = time.time()
print(f"Approach 'for loop' took {end_time - start_time:.4f} seconds.")