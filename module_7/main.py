from my_package import *
# from my_package import foo, log, mul, sum
# import my_package as my
import requests
from django.utils import timezone

def mul(a):
    return a * 100


if __name__ == "__main__":
    r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    print(r.status_code)
    # print(foo.foo("Jack"))
    # print(foo("Lisa"))
    # print(sum(3, 5))
    # # print(mul(4, 4))
    # log("testing")
    # print(temp())
    # print(mul(5))
    # print(...)

