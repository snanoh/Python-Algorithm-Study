
s = "MCMXCIL"

def roman_to_int( s: str) -> int:
    result = 0
    map = {"I": 1, "V": 5, "X":10, "L": 50, "C":100, "D": 500, "M":1000}
    for i in range(len(s)-1):
        #print(map[s[i]])
        num = map[s[i]]
        next_num = map[s[i+1]]
        if num >= next_num:
            result += num
        else:
            result -= num

    result += map[s[len(s)-1]]


    return result

print(roman_to_int(s))