import sys
from fractions import Fraction

def main(decimal):
    sign = 0
    right = len(decimal.split(".")[1])
    decimal = float(decimal)
    #Convert to pos, note sign
    if decimal < 0.0:
        decimal = decimal * -1
        sign = 1
    dec_as_frac = Fraction(decimal)
    upper = int(str(dec_as_frac).split("/")[0])
    lower = int(str(dec_as_frac).split("/")[1])
    dec_bin_num = float_bin(decimal)
    #dec_places =  -1 *(right)+2
    #formatted_bin = moveDecimalPoint(float(dec_bin_num), dec_places)
    print("Decimal in binary is {}".format(dec_bin_num))
    formatted_bin = input("Bin after shifted dot (NOTE: shifting right is neg):\n")
    dec_places = input("Num of places Shifted: \n")

    print("we have {} base 10 = ({}/{}) base 2 = {} x 2^{}\n".format(dec_as_frac, bin(upper), bin(lower), formatted_bin, dec_places))

    exp_excess = 127 + int(dec_places)
    print("Exponent is {} (base 10) = {} (base 2)".format(exp_excess, bin(exp_excess)))
    bit_exp_8 = format(exp_excess, '08b')

    partial_signi = formatted_bin.split(".")[1]
    for i in range(23-len(partial_signi)):
        partial_signi += '0'
    print("{:<5} {:<10} {:<30}".format(sign, bit_exp_8, partial_signi))
    print("{:<5} {:<10} {:<30}\n".format("sign", "exponent", "significant"))

    bitstring = str(sign) + bit_exp_8 + partial_signi

    hstr = '%0*X' % ((len(bitstring) + 3) // 4, int(bitstring, 2))
    print("Hex string {}".format(hstr))

 #Function returns octal representation
def float_bin(number):

    # split() seperates whole number and decimal
    # part and stores it in two seperate variables
    whole, dec = str(number).split(".")
    places = len(dec)
    # Convert both whole number and decimal
    # part from string type to integer type
    whole = int(whole)
    dec = int (dec)

    # Convert the whole number part to it's
    # respective binary form and remove the
    # "0b" from it.
    res = bin(whole).lstrip("0b") + "."

    # Iterate the number of times, we want
    # the number of decimal places to be
    for x in range(places):

        # Multiply the decimal value by 2
        # and seperate the whole number part
        # and decimal part
        whole, dec = str((decimal_converter(dec)) * 2).split(".")

        # Convert the decimal part
        # to integer again
        dec = int(dec)

        # Keep adding the integer parts
        # receive to the result variable
        res += whole

    return res

def moveDecimalPoint(num, decimal_places):
    '''
    Move the decimal place in a given number.

    args:
        num (int)(float) = The number in which you are modifying.
        decimal_places (int) = The number of decimal places to move.

    returns:
        (float)

    ex. moveDecimalPoint(11.05, -2) returns: 0.1105
    '''
    dec_num = 0
    for _ in range(abs(decimal_places)):

        if decimal_places>0:
            num *= 10; #shifts decimal place right
        else:
            num /= 10.; #shifts decimal place left

    print("moved {:d} places".format(dec_num))
    return float(num)

# Function converts the value passed as
# parameter to it's decimal representation
def decimal_converter(num):
    while num > 1:
        num /= 10
    return num

if __name__ == '__main__':
    main(sys.argv[1])
