import os
import time

os.mkdir("files")
print("The folder 'files' was created.")
print(os.getcwd())
os.chdir("files")
print(os.getcwd())


for i in range(1, 10):
    os.mkdir(str(i))

print("9 folders were created in 'files'.")


if os.path.isfile('2/some_document.txt'):
    print("Yes, It's a file!")
else:
    print("There is no such file!")


dir_list = os.listdir(os.getcwd())
print(dir_list)

# for i in dir_list[6:]:
#     os.rmdir((str(i)))

for dir_name in dir_list:
    if dir_name in ('7', '8', '9'):
        os.rmdir((str(dir_name)))

dir_list = os.listdir(os.getcwd())
print(dir_list)


# Використовуючи бібліотеку time створіть декоратор котрий буде повертатися
# час роботи функції до якої застосовується декоратор.


def decorator_add_runtime(func):
    def time_wrapper(*args, **kwargs):
        seconds_from_begin = time.time()
        print("The runtime is >>>",  time.ctime(seconds_from_begin))
        multiply_result = func(*args, **kwargs)
        return multiply_result

    return time_wrapper


def time_of_execution(func):
    def time_wrapper(*args, **kwargs):
        print("The runtime is >>>",  time.ctime(time.time()))
        start_time = time.time()
        multiply_result = func(*args, **kwargs)
        end_time = time.time()
        duration_of_execution = end_time - start_time
        print(f"The start time is >>> {start_time} sec.")
        print(f"The end time is >>> {end_time} sec.")
        print(f"Duration of execution >>> {duration_of_execution} sec.")
        return multiply_result

    return time_wrapper
#
#
# # @decorator_add_runtime
@time_of_execution
def multiply_num(a, b):
    print("The result of function >>>", a * b**a)
    return a * b/a


# multiply_num = decorator_add_runtime(multiply_num)
multiply_num(8217, 153)

# @time_of_execution
# def get_node(x, y):
#     while x != y:
#         if x > y:
#             x-=y
#         else:
#             y-=x
#     return x
#
#
# get_node(15, 2000000)