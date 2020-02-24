import os


class WarmUp:
    def __init__(self):
        self.__message = "Django Challenge"

    def ready(self):
        print("---------------------------------")
        print(f"Ready for {self.__message}")
        os.system("python -m django --version")
        print("---------------------------------")


use_me = ["code", 1, ("ready", {"there": "where", "here": [
                      1, WarmUp(), 3]}, "study"), "girls"]

obj = use_me[2][1]['here'][1]
obj.ready()
