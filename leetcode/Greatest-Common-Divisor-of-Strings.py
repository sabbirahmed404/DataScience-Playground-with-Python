import math

def commondivisor(str1,str2):
    if str1+ str2 == str2 + str1:
        gcd_length = math.gcd(len(str1), len(str2))
        if len(str1) > len(str2):
            return str1[:gcd_length]
        else:
            return str2[:gcd_length]

    else :
        return ""

result = commondivisor("ABCDABC","ABC")
print(result)