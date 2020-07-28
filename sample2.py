import asyncio


async def f1(x):
    print("start function f1")
    for i in range(0, x):
        print("x right now is {}".format(i))
        await asyncio.sleep(0.01)
    print("end function f1")


async def f2(my_str, times):
    print("start function f2")
    for i in range(0, times):
        print(my_str)
        await asyncio.sleep(0.01)
    print("end function f2")


async def f3(my_str1, my_str2):
    print("start function f3")
    print(my_str1 + my_str2)
    print("end function f3")


async def async_call():
    f1_obj=event_loop.create_task(f1(10))
    f2_obj=event_loop.create_task(f2("hello", 10))
    f3_obj = event_loop.create_task(f3("hello", "goodby"))
    await asyncio.wait([f1_obj, f2_obj, f3_obj])


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(async_call())
event_loop.close()
