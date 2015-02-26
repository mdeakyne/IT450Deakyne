def bin_to_str(pos, binary_digit):
    if pos == 1:
        ret_str = ".."
    elif pos == 2 or pos == 4 or pos == 6:
        ret_str = "...."
    elif pos == 3 or pos == 5:
        ret_str = "..."
    else:
        return -1

    r_pos = -1

    for i in binary_digit[:1:-1]:
        if i == '1':
            if(r_pos == -1):
                ret_str = ret_str[:-1]+"-"
            else:
                ret_str = ret_str[:r_pos]+"-"+ret_str[r_pos+1:]
        r_pos -= 1
    #print binary_digit, 'becomes', ret_str
    return ret_str

def checkio(time_string):
    ts = time_string.split(":")
    for i in range(len(ts)):
        if len(ts[i]) < 2:
            ts[i] = "0" + ts[i]

    binary_digits = ""
    pos = 1
    for section in ts:
        #print("Section is",section)
        for digit in section:
            bdigit = bin(int(digit))
            #print("Binary number is: ",bdigit)
            binary_digits += bin_to_str(pos,bdigit)
            pos += 1
            binary_digits += " "
        binary_digits += ": "
    print(ts)
    #replace this for solution
    binary_digits = binary_digits[:-3]
    print binary_digits
    return binary_digits

if __name__ == '__main__':
    checkio("10:37:49")
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

