import sys

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
    print("{:<5} {:<10} {:<30}\n".format("sign", "exponant", "significant"))

if __name__ == '__main__':
    main(sys.argv[1])
