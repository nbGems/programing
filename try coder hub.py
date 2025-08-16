# def repetitions(s):
#     s=s.upper()
#     s= list(s)
#     c= list()
#     b= 1
#     for x,h in zip(s[0:],s[1:]):
#         if h is x:
#             b+= 1
#             c.append(b)
#         else:
#             b=1
#     return max(c)
#
# while True:
#     f= input()
#     print(f"{repetitions(f)}\n")

def repetitions(s):
    if not s:
        return None, 0

    max_char = s[0]
    max_count = 1
    current_char = s[0]
    current_count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_char = current_char
            current_char = s[i]
            current_count = 1

    if current_count > max_count:
        max_count = current_count
        max_char = current_char

    return max_char, max_count


print(repetitions('AMMMDDCCCMD'))