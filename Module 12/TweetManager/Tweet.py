# Tweet Class
# Andrew Kim (AHKYQX)

import time


class Tweet:
    def __init__(self, author, text) -> None:
        self.__author = author
        self.__text = text
        self.__age = time.time()  # Set based on current time

    def get_author(self):
        return self.__author

    def get_text(self):
        return self.__text

    def get_age(self):
        # Calculate difference between current time and time of tweet
        diff = abs(time.time() - self.__age)

        # Consolidate to most significant unit
        if diff < 60:
            return str(int(diff)) + "s"  # Seconds
        elif diff < 3600:
            return str(int(diff // 60)) + "m"  # Minutes
        elif diff < 86400:
            return str(int(diff // 3600)) + "h"  # Hours
        else:
            return str(int(diff // 86400)) + "d"  # Days
