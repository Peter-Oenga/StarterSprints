def reversed(S):
    result = ""

    for i in S:
        result = i + result

    return result
S = "oenga"
print(S)
print(reversed(S))