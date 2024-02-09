test_str = "qwertyqwe123"

count = 0
 
for i in test_str:
    if i == 'e':
        count = count + 1
 
# printing result
print("Count of e in qwertyqwe123 is : "
      + str(count))