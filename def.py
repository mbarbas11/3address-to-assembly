#!/usr/bin/env python3
# Michael Barbas CSC437

# import re


def def_translate(l):
    # handles definition for initial values in .data after obtaining 3 address...
    cur_line = l.split()
    with open('output.s', 'a') as o:  # append assembly conversion file
        if cur_line[0] == "INT":
            o.write("\n{} dq {}".format(cur_line[1], cur_line[2]));
        if cur_line[0] == "CHAR":
            o.write("\n{} db {} {} {}, 0".format(cur_line[1], cur_line[2], cur_line[3], cur_line[4]));


def code_translate(line, step):
    cur_line = line.replace(",", "").split()

    with open('output.s', 'a') as o:  # append to file
        print(cur_line[0])
        if cur_line[0] == "JUMP":
            o.write("\n\nL{}:".format(step))
            o.write("\nmov rax, [{}]".format(cur_line[3]))
            o.write("\ncmp rax, [{}]".format(cur_line[4]))
            o.write("\nj{} L{}".format(cur_line[1], cur_line[2]))
        elif cur_line[0] == "MASK":
            o.write("\n\nL{}:".format(step))
            o.write("\nmov rax, [{}]".format(cur_line[3]))
            o.write("\nmov rax, [{}]".format(cur_line[4]))
            o.write("\nj{} L{}".format(cur_line[1], cur_line[2]))
        elif cur_line[0] == "PRINT":
            o.write("\n\nL{}:".format(step))
            o.write("\nmov rdi, [{}]".format(cur_line[1]))
            o.write("\nmov rsi, [{}]".format(cur_line[2]))
            o.write("\nmov rdx, [{}]".format(cur_line[3]))
            o.write("\ncall printf")
        elif cur_line[0] == "INC":
            o.write("\n\nL{}:".format(step))
            o.write("\nmov rax, [{}]".format(cur_line[1]))
            o.write("\ninc rax")
            o.write("\nmov [{}], rax".format(cur_line[1]))
        elif cur_line[0] == "GOTO":
            o.write("\n\nL{}:".format(step))
            o.write("\njmp L{}".format(cur_line[1]))
        elif cur_line[0] == "END":
            o.write("\n\nL{}:".format(step))
            o.write("\nadd rsp, 0x28")
            o.write("\nret")


def main():
    with open('output.s', 'w') as o:
        o.write('global main')
        o.write('\nextern main')
        o.write('\nextern sleep')
        o.write('\n\nsection .data')

    with open("addr.txt", "r") as addr:  # read 3 address to obtain values to define.
        c = 0
        ran = False
        for cur_line in addr:
            ran = False
            print(cur_line)
            c += 1
            sep_line = cur_line[:-1].split(" ")

            if sep_line[0] == "INT" or sep_line[0] == "CHAR":

                # print(sep_line[0])
                def_translate(cur_line)
            else:
                # print("\n")
                # print(se"p_line[0])
                if not ran:
                    print(c)
                    if c == 4:
                        with open("output.s", "a") as o:
                            o.write("\n\nsection .text")
                            o.write("\nmain:")
                            o.write("\nsub rsp, 0x28")
                    ran = True
                    code_translate(cur_line, c)


if __name__ == "__main__":
    main()
