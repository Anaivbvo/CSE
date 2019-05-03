number = str[1707909249311050]


def valid_card_number(num: str):
    list(number)
    number.pop(15)
    number. reverse()
    print(number)


print(valid_card_number(number))

def remove(string):
    print(S[:-1])

    def valid_card_number(num: str):
        number = 1707909249311050
        print(number[:-1])
        print(number[::-1])
        new = number[(0, 2, 4, 6, 8, 10, 12, 14) * 2]
        list(new)
        if 9 in new:

"""
def validate(num: int):
    num = list(num)
    if len(num) == 16:
        last_num = num[15]
        num.pop(15)
        num = num[:: - 1]
        odds = num[0:15:2]
        even = num[1:15:2]
        o = 0
        for i in odds:
            odds[o] = int(odds[o])
            odds[o] *= 2
            if int(odds[o]) >= 10:
                odds[o] = int(odds[o]) - 9
                o += 1
            else:
                o += 1
        oddadd = int(odds[0]) + int(odds[1]) + int(odds[2]) + int(odds[3]) + int(odds[4]) + int(odds[5]) + int(odds[6])\
            + int(odds[7])
        evenadd = int(even[0]) + int(even[1]) + int(even[2]) + int(even[3]) + int(even[4]) + int(even[5]) + int(even[6])
        allnum = oddadd + evenadd
        if int(allnum) % 10 is int(last_num):
            return True
        else:
            return False
    return False
"""