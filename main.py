import time

# basically this is used to add something to code for ex something before or after or 
# to add some function before or after or in between or to run the function multiple times.
def delay_decorator(function):
    def wraper_function():
        time.sleep(5)
        # DO something before
        function()
        function()
        function()
        # Do something after 
    return wraper_function

@delay_decorator
def say_hello():
    print("hello")


def say_bye():
    print("bye")


def say_greeting():
    print("greetings unknown person")

say_hello()
say_bye()
say_greeting()
