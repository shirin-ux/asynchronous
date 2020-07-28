def f1(x):
    print("start function f1")
    for i in range(0, x):
        print("x right now is {}".format(i))
    print("end function f1")


def f2(my_str,times):
    print("start function f2")
    for i in range(0, times):
        print(my_str)
    print("end function f2")

def f3(my_str1,my_str2):
    print("start function f3")
    print(my_str1+my_str2)
    print("end function f3")

def synchronous():
    f1(3)
    f2("hello",3)
    f3("hello","goodby")

synchronous()