import sys
import math
import struct

def main(bitstring):
    # Code to convert hex to binary
    n = int(bitstring, 16)
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    res = bStr
    sign = res[0]
    bit_exp_8 = res[1:9]
    bit_signi_23 = res[9:]

    print("{:<5} {:<10} {:<30}".format(sign, bit_exp_8, bit_signi_23))
    print("{:<5} {:<10} {:<30}\n".format("sign", "exponent", "significant"))

    exp_excess = int(bit_exp_8, 2)
    exponent = exp_excess - 127
    print("Exponent is {} - 127 = {}".format(exp_excess, exponent))

    factor_n = 0
    num = 1
    print("Computing factor_n")
    for bit in bit_signi_23:
        if int(bit) == 1:
            devisor = math.pow(2, num)
            factor_n += 1 / devisor
            print("{}/{}".format(1,devisor))
        num += 1
    print("factor_n = {}".format(factor_n))
    factor_d = 1 + factor_n
    print("factor_d = {}".format(factor_d))

    if int(sign) == 1:
        dec_num = -1 * factor_d * math.pow(2, exponent)
    print("Decimal number: {}".format(dec_num))

if __name__ == '__main__':
    main(sys.argv[1])
