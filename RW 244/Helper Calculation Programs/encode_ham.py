import sys

def main(dataword):
    codeword = parse(dataword)
    print("Input: {}".format(codeword))
    bit_postion = 1
    calc_parity_arr = []
    for element in codeword:
        bit = int(element)
        if bit == 1:
            bin_pos = format(bit_postion, '04b')
            bin_pos_arr = [bin_pos[0], bin_pos[1], bin_pos[2], bin_pos[3]]
            calc_parity_arr.append(bin_pos_arr)

        bit_postion += 1
    for element in calc_parity_arr:
        print(element)
    calc_par_dig = do_xor(calc_parity_arr)
    print("XOR {}".format(calc_par_dig))

    codeword[0] = calc_par_dig[3]
    codeword[1] = calc_par_dig[2]
    codeword[3] = calc_par_dig[1]
    codeword[7] = calc_par_dig[0]

    print("Codeword: {}".format(codeword))

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

def parse(dataword):
    codeword = [0,0,0,0,0,0,0,0,0,0,0,0]

    codeword[2] = int(dataword[0])
    codeword[4] = int(dataword[1])
    codeword[5] = int(dataword[2])
    codeword[6] = int(dataword[3])
    codeword[8] = int(dataword[4])
    codeword[9] = int(dataword[5])
    codeword[10] = int(dataword[6])
    codeword[11] = int(dataword[7])

    return codeword

if __name__ == '__main__':
    main(sys.argv[1])
