def solution(s):
    new_val=""
    first_index_used = 0
    last_index = 0
    
    if len(s) == 0:
        return s
    elif (s == s.lower()):
        return s
    else:
        for i in range(0, len(s)):
            if s[i].isupper():
                if first_index_used == 1:
                    new_val = new_val + s[last_index:i] + " "
                    last_index = i
                else:
                    new_val = new_val + s[first_index_used:i] + " "
                    first_index_used = 1
                    last_index = i
    
    new_val = new_val + s[last_index:]
    return new_val

val = "breakCamelCase"
new_val = solution(val)
print(f"New Value: {new_val}")

"""

Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

"""
