def count_string(s):
    result=""
    count=0
    for i in range(len(s)):
        if s[i].isdigit():
            count = int(s[i])
        else:
            result += s[i] * count
    return result
s="2a2b2c"
print(count_string(s))
