from typing import List

string = ["h", "e", "l", "l", "o"]


def reverse_string(s: List[str]) -> None:
    s.reverse()

reverse_string(string)
print(string)