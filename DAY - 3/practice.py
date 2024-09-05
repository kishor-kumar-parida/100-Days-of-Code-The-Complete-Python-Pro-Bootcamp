# if condition:
#   do this
# else:
#   do that

height = int(input("what is your height?\n"))

if height > 120:
    age = int(input("comment your age\n"))
    if age > 18:
        print("yes")

    elif age == 18:
        print("ok")

    else:
        print("no")

elif height == 120:
    print("ok")

else:
    print("no")
