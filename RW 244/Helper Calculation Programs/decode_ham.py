import sys
def main(codeword):
    codeword = parse(codeword)
    dataword = []
    print("Input: {}\n".format(codeword))
    non_pow_2_bit = "b8   b4   b2   b1"
    calc_parity_arr = []
    rec_par_dig = []
    bit_names = []
    bit_postion = 1
    for element in codeword:
        bit = int(element)
        if not (bit_postion == 1 or bit_postion == 2 or bit_postion == 4 or bit_postion == 8):
            dataword.append(element)
            if bit == 1:
                bin_pos = format(bit_postion, '04b')
                bin_pos_arr = [bin_pos[0], bin_pos[1], bin_pos[2], bin_pos[3]]
                calc_parity_arr.append(bin_pos_arr)
                bit_names.append("b{}".format(bit_postion))
        bit_postion += 1
    print("Calculate parity by computing the bitwise xor of all bit positions that contain 1.")
    print("{:>23}".format(non_pow_2_bit))
    i = 0
    for element in calc_parity_arr:
        print("{:<4}{}".format(bit_names[i], element))
        i += 1

    calc_par_dig = do_xor(calc_parity_arr)
    print("XOR {}\n".format(calc_par_dig))

    rec_par_dig.append(codeword[7])
    rec_par_dig.append(codeword[3])
    rec_par_dig.append(codeword[1])
    rec_par_dig.append(codeword[0])

    join_arr = [calc_par_dig, rec_par_dig]
    print("xor the calculated parity bits with the received parity bits.")
    print("{:>17}".format("b8 b4 b2 b1"))
    xor_calc_rec = do_xor(join_arr)
    print("Calc {}\nRecv {}\n XOR {}".format(join_arr[0], join_arr[1], xor_calc_rec))
    bin_str = str("0b{}{}{}{}".format(xor_calc_rec[0], xor_calc_rec[1], xor_calc_rec[2], xor_calc_rec[3]))
    faulty_bit = int(bin_str, 2)

    if faulty_bit == 0:
        print("Decoded Dataword {}".format(dataword))
    else:
        print("Faulty Bit: {}".format(faulty_bit))
        codeword[faulty_bit-1] ^= codeword[faulty_bit-1]
        dataword = []
        bit_postion = 1

        for element in codeword:
            if not (bit_postion == 1 or bit_postion == 2 or bit_postion == 4 or bit_postion == 8):
                dataword.append(element)
            bit_postion += 1
        print("New decoded Dataword {}".format(dataword))


def parse(codeword):
    new_codeword = []
    for i in range(len(codeword)):
        new_codeword.append(int(codeword[i]))
    return new_codeword

def do_xor(arr):
    xor_arr = []
    col_arr = []

    for i in range(4):
        temp = []
        for k in range(len(arr)):
            temp.append(arr[k][i])
        col_arr.append(temp)

    for row in range(len(col_arr)):
        result = int(col_arr[row][0])
        for i in range(1,len(col_arr[0])):
            result = result ^ int(col_arr[row][i])
        xor_arr.append(int(result))
    return xor_arr

if __name__ == '__main__':
    main(sys.argv[1])
