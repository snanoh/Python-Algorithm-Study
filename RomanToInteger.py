
s = "IV"

def roman_to_int( s: str) -> int:
    result = 0
    map = {"I": 1, "V": 5, "X":10, "L": 50, "C":100, "D": 500, "M":1000}
    for i in s:
        result += int(map[i])

    return result

print(roman_to_int(s))