import random
from random_useragent.random_useragent import Randomize

device_types = ("desktop",)
os = ("linux", "windows", "mac")


def random_pick():
    r_agent = Randomize()
    return r_agent.random_agent(device_type=random.choice(device_types), os=random.choice(os))
