class Demo:
    a= 4


o= Demo()
print(o.a)  # print the class attribute because instance attibute is not present.
o.a = 0     # instance attribute is set.
print(o.a)  # Print the instance attribte because instance attribute is present.
print(Demo.a)    # print class attribute.