# _*_ coding:UTF-8 _*_

count_nonstandard = 0
count_fen_for = 0


def handle_line(line):
    list_str1 = list(line)
    for i in range(0, len(list_str1)):  # 给每个符号前加空格为统一函数名变量名做基础
        if list_str1[i] == ';':  # 因为符号贴在变量名、保留字等上面时会影响到这些变量名、保留字的识别
            list_str1[i] = ' ; '  # 因此在符号前后加上空格，使符号能被识别
        elif list_str1[i] == '\n':
            list_str1[i] = ' \n'
        elif list_str1[i] == '\t':
            list_str1[i] = ' '  # '\t'这种对程序逻辑不影响的符号直接就把它去除了
        elif list_str1[i] == '\r':  # 还有'\r'
            list_str1[i] = ' '
        elif list_str1[i] == ',':
            list_str1[i] = ' , '
        elif list_str1[i] == '(':
            list_str1[i] = ' ( '
        elif list_str1[i] == ')':
            list_str1[i] = ' ) '
        elif list_str1[i] == "=":
            list_str1[i] = ' = '
        elif list_str1[i] == "+":
            list_str1[i] = ' + '
        elif list_str1[i] == "-":
            list_str1[i] = ' - '
        elif list_str1[i] == "*":
            list_str1[i] = ' * '
        elif list_str1[i] == "/":
            list_str1[i] = ' / '
        elif list_str1[i] == "[":
            list_str1[i] = ' [ '
        elif list_str1[i] == "]":
            list_str1[i] = ' ] '
        elif list_str1[i] == "{":
            list_str1[i] = ' { '
        elif list_str1[i] == "}":
            list_str1[i] = ' } '
        if list_str1[i] == '!':
            list_str1[i] = ' ! '
        elif list_str1[i] == '~':
            list_str1[i] = ' ~ '
        elif list_str1[i] == '&':
            list_str1[i] = ' & '
        elif list_str1[i] == '%':
            list_str1[i] = ' % '
        elif list_str1[i] == '>':
            list_str1[i] = ' > '
        elif list_str1[i] == "<":
            list_str1[i] = ' < '
        elif list_str1[i] == "^":
            list_str1[i] = ' ^ '
        elif list_str1[i] == "|":
            list_str1[i] = ' | '
        elif list_str1[i] == "?":
            list_str1[i] = ' ? '
        elif list_str1[i] == ":":
            list_str1[i] = ' : '
        elif list_str1[i] == '\"':
            list_str1[i] = ' \" '
        elif list_str1[i] == '\'':
            list_str1[i] = ' \' '
        elif list_str1[i] == "#":
            list_str1[i] = ' # '
        elif list_str1[i] == ".":
            list_str1[i] = ' . '

    line = "".join(list_str1)  # 上面步骤处理完后，重新将list_str1[]组成一个字符串
    while line.find('  ') >= 0:  # 去掉一些多余的空格
        line = line.replace("  ", " ")

    if line.find('+ =') >= 0:
        line = line.replace('+ =', '+=')
    if line.find('+ +') >= 0:
        line = line.replace('+ +', '++')
    if line.find('- =') >= 0:
        line = line.replace('- =', '-=')
    if line.find('- -') >= 0:
        line = line.replace('- -', '--')
    if line.find('* =') >= 0:
        line = line.replace('* =', '*=')
    if line.find('/ =') >= 0:
        line = line.replace('/ =', '/=')
    if line.find('% =') >= 0:
        line = line.replace('% =', '%=')
    if line.find('| |') >= 0:
        line = line.replace('| |', '||')
    if line.find('& &') >= 0:
        line = line.replace('& &', '&&')
    if line.find('> =') >= 0:
        line = line.replace('> =', '>=')
    if line.find('< =') >= 0:
        line = line.replace('< =', '<=')
    if line.find('- >') >= 0:
        line = line.replace('- >', '->')
    if line.find(': :') >= 0:
        line = line.replace(': :', '::')
    if line.find('| =') >= 0:
        line = line.replace('| =', '|=')
    if line.find('! =') >= 0:
        line = line.replace('! =', '!=')
    if line.find('> >') >= 0:
        line = line.replace('> >', '>>')
    if line.find('< <') >= 0:
        line = line.replace('< <', '<<')
    if line.find('& =') >= 0:
        line = line.replace('& =', '&=')
    if line.find('^ =') >= 0:
        line = line.replace('^ =', '^=')
    if line.find('>> =') >= 0:
        line = line.replace('>> =', '>>=')
    if line.find('<< =') >= 0:
        line = line.replace('<< =', '<<=')
    line = line.lstrip()  # 去掉左右两边的空格
    return line


def solve_format(line, judge):
    '''去掉每一行左右两端的空格'''
    line = line.strip()
    '''首先删掉/**/注释中的内容'''
    i = line.find('/*')
    j = line.find('*/')
    if i >= 0 or j >= 0:
        if j > i and i >= 0:  # /* 和 */ 都存在时
            line = line[0:i] + line[j + 2:len(line)]
        elif j == -1:  # 只有 /* 存在时
            line = line[0:i]
            judge = False
        elif i == -1:  # 只有 */ 存在时
            line = line[j + 2:len(line)]
            judge = True
    elif judge is False:  # 当此行为注释的内容时，直接去掉该行
        return "", judge
    '''再删掉//注释中的内容'''
    i = line.find('//')  # 标准化1：进行字符串操作，去掉//后的注释
    if i >= 0:
        line = line[0:i]

    line = handle_line(line + "\n")
    '''删除多余的换行符'''
    if len(line) < 2:
        return "", judge
    return line, judge


def nonexist(line, lines, multidef_or_nonstand):
    # print("都没有 ", line)
    global count_nonstandard
    start_solve11 = ['int', 'long', 'bool', 'short', 'struct', 'char', 'static', 'extern', 'const', 'double', 'float',
                     'void', 'return', 'typedef', 'if', 'do', 'scanf', 'printf', 'fscanf', 'fprintf', '#', 'else',
                     'exit', 'switch', 'case', 'for', 'using']
    list_line = line.split(" ")
    idj = line.find("#")
    while idj != -1:
        if idj > 0:
            lines[len(lines) - 1] = lines[len(lines) - 1].strip() + " " + line[0:idj - 1] + " \n"
            count_nonstandard = count_nonstandard + 1
            line = line[idj:len(line)]
        else:  # 说明idj=0，即list_line[0]="#"
            i = 1
            while i < len(list_line):
                if list_line[i] in start_solve11:
                    ids = line.find(list_line[i])
                    lines.append(line[0:ids - 1] + " \n")
                    line = line[ids:len(line)]
                    break
                i = i + 1
            if i == len(list_line):
                lines.append(line)
                return lines, multidef_or_nonstand
        idj = line.find("#")
    if len(line) > 2:
        multidef_or_nonstand = multidef_or_nonstand + line
        # count_nonstandard = count_nonstandard + 1
    return lines, multidef_or_nonstand


def yk_exist(line, iyk, lines, multidef_or_nonstand):
    # print("右括号 ", line)
    if len(line) <= 3:  # } \n
        lines.append(line)
        return lines, multidef_or_nonstand
    else:  # 经过处理，已经这一行已经不能是数组或者结构体变量的多行定义了，所以如果出现单独的一个右括号，应该是如下的形式
        if len(line) < 3:
            return lines, multidef_or_nonstand
        while len(line) >= 3:
            line1 = line[0:iyk + 1]
            line = line[iyk + 2:len(line)]
            lines.append(line1 + " \n")
            iyk = line.find("}")
            if iyk == -1 and len(line) >= 3:  # {};都不存在
                return nonexist(line, lines, multidef_or_nonstand)
        return lines, multidef_or_nonstand


def zk_exist(line, izk, lines, multidef_or_nonstand):
    # print("左括号 ", line)
    while len(line) >= 3:
        if len(line) == 3:  # 则此行代码就只有括号一个
            lines.append(line)
            return lines, multidef_or_nonstand
        if line[izk - 2] == "=":  # 说明是数组或者结构体变量的赋值定义，归入下一行,且算他规范
            multidef_or_nonstand = multidef_or_nonstand + line
            return lines, multidef_or_nonstand
        else:  # 说明不是数组的赋值定义或者结构体变量的赋值定义
            '''while switch if else 函数头、结构体的定义'''
            if izk - 1 >= 0:
                lines.append(line[0:izk - 1] + " \n")
            lines.append("{ \n")
            line = line[izk + 2:len(line)]
            izk = line.find("{")
        if izk == -1 and len(line) >= 3:  # {}和;都不存在
            return nonexist(line, lines, multidef_or_nonstand)
    return lines, multidef_or_nonstand


def fen_line_solve(line, lines):
    # print("分号前处理 ", line)
    line_list = line.split(" ")
    if line_list[0] == 'if' or (line_list[0] == 'else' and line_list[1] == 'if') or line_list[0] == 'switch':
        izk = line.find("(")
        i = izk + 1
        countk = 1
        while i < len(line):
            if line[i] == "(":
                countk = countk + 1
            elif line[i] == ")":
                countk = countk - 1
            if countk == 0:
                break
            i = i + 1
        if i < len(line):
            lines.append(line[0:i + 1] + " \n")
            lines.append(line[i + 2:len(line)] + " \n")
        else:  # 说明代码有错，只要编译过了就不会有错，所以这种情况不可能发生
            lines.append(line + " \n")
    elif line_list[0] == 'else' or line_list[0] == 'do':
        lines.append(line_list[0] + " \n")
        lines.append(line[len(line_list[0]) + 1:len(line)] + " \n")
    elif line_list[0] == 'case' or line_list[0] == 'default':
        idm = line.find(":")
        lines.append(line[0:idm + 1] + " \n")
        lines.append(line[idm + 2:len(line)] + " \n")
    else:
        lines.append(line + " \n")
    return lines


def fen_exist(ifen, line, lines, multidef_or_nonstand):
    # print("分号 ", line)
    global count_nonstandard
    ifor = line.find("for")
    while ifor >= 0 and len(line) >= 3:
        while ifen >= 0 and ifor > ifen:  # 将for语句之前的语句以分号结束
            line1 = line[0:ifen + 1]
            line = line[ifen + 2:len(line)]
            lines = fen_line_solve(line1, lines)
            ifen = line.find(";")
            ifor = line.find("for")
        # while结束，一定是分号在for语句后面，或者不存在分号
        izk = line.find("(")
        i = izk + 1
        countk = 1
        while i < len(line):
            if line[i] == "(":
                countk = countk + 1
            elif line[i] == ")":
                countk = countk - 1
            if countk == 0:
                break
            i = i + 1
        if i < len(line):
            lines.append(line[0:i + 1] + " \n")
            line = line[i + 2:len(line)]
            ifen = line.find(";")
            ifor = line.find("for")
        else:  # ----不规范，归入下一行
            multidef_or_nonstand = multidef_or_nonstand + line
            count_nonstandard = count_nonstandard + 1
            # print("找for")
            return lines, multidef_or_nonstand
        if ifor == -1 and ifen == -1 and len(line) >= 3:
            (lines, multidef_or_nonstand) = nonexist(line, lines, multidef_or_nonstand)
            return lines, multidef_or_nonstand
    while ifen >= 0:
        '''如果此时还存在分号，则以分号断句'''
        line1 = line[0:ifen + 1]
        line = line[ifen + 2:len(line)]
        lines = fen_line_solve(line1, lines)
        ifen = line.find(";")
    if len(line) >= 3:
        # count_nonstandard = count_nonstandard + 1
        multidef_or_nonstand = multidef_or_nonstand + line
    return lines, multidef_or_nonstand


def zyk_exist(izk, iyk, line, multidef_or_nonstand, lines):
    # print("左右括号 ", line)
    global count_nonstandard
    if izk == -1:  # 只有右括号
        return yk_exist(line, iyk, lines, multidef_or_nonstand)
    elif iyk == -1:  # 只有左括号-----对后面括号和分号的判断有很大的影响
        '''可能是数组的多行定义，或者while switch if else 函数头、结构体的定义，还有可能是单独一个左括号：规范'''
        '''{do 要考虑这种情况'''
        '''还有这种情况st={a,b,c,d,{}}'''
        return zk_exist(line, izk, lines, multidef_or_nonstand)
    else:  # 左右括号都存在
        while len(line) >= 3:
            while iyk >= 0 and izk > iyk:  # 如果右括号在左括号的左边，则将右括号包括其之前的内容保存到lines中，余下的在进行判断
                line1 = line[0:iyk + 1]
                line = line[iyk + 2: len(line)]
                lines.append(line1 + " \n")
                iyk = line.find("}")
                izk = line.find("{")
            # 出来以后，右括号在左括号的右边，或者不存在右括号,一定存在左括号
            if iyk == -1:  # 此时不存在右括号，则只有左括号
                return zk_exist(line, izk, lines, multidef_or_nonstand)
            # 这里时，说明左右括号都存在，并且左括号在右括号左边{}
            if izk - 2 >= 0 and line[izk - 2] == "=":  # 不规范，数组或者结构体变量的赋值定义，但是没有以分号结束，并入下一行找分号
                multidef_or_nonstand = multidef_or_nonstand + line
                count_nonstandard = count_nonstandard + 1
                # print("找分号")
                return lines, multidef_or_nonstand
            while izk >= 0 and iyk > izk:  # 到这儿，说明不是数组或者结构体变量的赋值定义
                '''可以考虑这种情况
                if (a>1){}
                struct aa{}
                    st;
                则将左括号及其之前的代码保存到lines中，余下再继续判断
                '''
                line2 = line[0:iyk - 1] + " \n"
                multidef_or_nonstand1 = ''
                lines, multidef_or_nonstand1 = zk_exist(line2, izk, lines, multidef_or_nonstand1)
                line = multidef_or_nonstand1.strip() + " " + line[iyk:len(line)]
                iyk = line.find("}")
                izk = line.find("{")
            if izk == -1:  # 说明只剩下右括号
                # print("只有右括号了")
                return yk_exist(line, iyk, lines, multidef_or_nonstand)
    return lines, multidef_or_nonstand


def zkf_exist(izk, ifen, line, multidef_or_nonstand, lines):
    # print("左括号分号 ", line)
    if ifen == -1:  # 只存在左括号
        return zk_exist(line, izk, lines, multidef_or_nonstand)
    elif izk == -1:  # 只存在分号
        return fen_exist(ifen, line, lines, multidef_or_nonstand)
    else:  # 左括号和分号都存在
        while len(line) >= 3:
            while izk >= 0 and ifen > izk:  # 若分号在左括号的右边 {for(;;)
                if izk - 1 >= 0:
                    lines.append(line[0:izk - 1] + " \n")
                lines.append("{ \n")
                line = line[izk + 2:len(line)]
                izk = line.find("{")
                ifen = line.find(";")
            # 出来之后，第一个分号在第一个左括号左边，或者不存在左括号，并且肯定存在分号
            while ifen >= 0 and izk > ifen:
                '''如果左括号存在，则一定在第一个分号的右边 for(;;) do{'''
                multidef_or_nonstand1 = ''
                line2 = line[0:izk - 1] + " \n"
                line = line[izk + 2:len(line)]
                lines, multidef_or_nonstand1 = fen_exist(ifen, line2, lines, multidef_or_nonstand1)
                if len(multidef_or_nonstand1) >= 3:
                    line = multidef_or_nonstand1.strip() + " { " + line
                else:
                    lines.append("{ \n")
                ifen = line.find(";")
                izk = line.find("{")
            # 出来之后，第一个左括号在第一个分号前面
            if izk == -1 and ifen != -1:  # 此时只剩下分号
                return fen_exist(ifen, line, lines, multidef_or_nonstand)
            elif ifen == -1 and izk != -1:  # 只剩下左括号
                return zk_exist(line, izk, lines, multidef_or_nonstand)
            elif izk == -1 and ifen == -1:
                return nonexist(line, lines, multidef_or_nonstand)
    return lines, multidef_or_nonstand


def ykf_exist(iyk, ifen, line, multidef_or_nonstand, lines):
    # print("右括号分号 ", line)
    if iyk == -1:  # 只存在分号
        return fen_exist(ifen, line, lines, multidef_or_nonstand)
    elif ifen == -1:  # 只存在右括号
        return yk_exist(line, iyk, lines, multidef_or_nonstand)
    else:  # 右括号或者分号都存在
        while len(line) >= 3:
            while ifen >= 0 and iyk > ifen:
                line1 = line[0:iyk - 1] + " \n"
                multidef_or_nonstand1 = ''
                line = line[iyk:len(line)]
                lines, multidef_or_nonstand1 = fen_exist(ifen, line1, lines, multidef_or_nonstand1)
                if len(multidef_or_nonstand1) >= 3:
                    lines.append(multidef_or_nonstand1)
                ifen = line.find(";")
                iyk = line.find("}")
            # 出来时分号在右括号的右边，或者不存在分号
            if ifen == -1:  # 只存在右括号
                return yk_exist(line, iyk, lines, multidef_or_nonstand)
            if line[iyk + 2:iyk + 7] == "while":
                lines.append(line[iyk:ifen + 1] + " \n")
                line = line[ifen + 2:len(line)]
            else:
                line1 = line[0:iyk + 1]
                line = line[iyk + 2:len(line)]
                lines.append(line1 + " \n")
            ifen = line.find(";")
            iyk = line.find("}")
            if iyk == -1 and ifen != -1:  # 只存在分号
                return fen_exist(ifen, line, lines, multidef_or_nonstand)
            elif ifen == -1 and iyk != -1:  # 只存在右括号
                return yk_exist(line, iyk, lines, multidef_or_nonstand)
            elif iyk == -1 and ifen == -1:  # 都不存在
                return nonexist(line, lines, multidef_or_nonstand)
    return lines, multidef_or_nonstand


def standardisation(text):  # ********************************************************************************代码标准化
    global count_nonstandard
    global count_fen_for
    """
    1、参数text：传入需要标准化的程序
    2、标准化包括但不限于：去注释（两种）、去空格（包括Tab）、处理printf后的内容、统一变量名、函数名等
    """
    lines = []
    judge = True
    multidef_or_nonstand = ''
    for line in text:  # 取出文本每一行

        line, judge = solve_format(line, judge)
        if len(line) <= 2:
            continue

        count_fen_for1 = line.count(";") - 2 * line.count("for") - 1
        if count_fen_for1 > 0:
            count_nonstandard = count_nonstandard + count_fen_for1
            count_fen_for = count_fen_for + count_fen_for1

        if len(multidef_or_nonstand) >= 3:
            multidef_or_nonstand = multidef_or_nonstand.strip()
            line = multidef_or_nonstand + " " + line
        multidef_or_nonstand = ''

        izk = line.find("{")
        iyk = line.find("}")
        ifen = line.find(";")
        if ifen == -1 and izk == -1 and iyk == -1:  # 三个都不存在
            # print("doumeiyou ", line)
            (lines, multidef_or_nonstand) = nonexist(line, lines, multidef_or_nonstand)
            continue
        elif ifen == -1:  # 存在左或者右括号
            # print("zuoyou ", line)
            lines, multidef_or_nonstand = zyk_exist(izk, iyk, line, multidef_or_nonstand, lines)
            continue
        elif iyk == -1:  # 存在分号或者左括号
            # print("fenzuo ", line)
            lines, multidef_or_nonstand = zkf_exist(izk, ifen, line, multidef_or_nonstand, lines)
            continue
        elif izk == -1:  # 存在右括号或者分号
            # print("fenyou ", line)
            lines, multidef_or_nonstand = ykf_exist(iyk, ifen, line, multidef_or_nonstand, lines)
            continue
        else:  # 三个都存在
            # print("douyou ", line)
            while ifen >= 0 or izk >= 0 or iyk >= 0 and len(line) >= 3:
                while ifen < iyk and izk < iyk and ifen >= 0 and izk >= 0:  # 截出分号和左括号之间的代码，调用函数完成
                    if ifen > izk:
                        line1 = line[0:ifen + 1] + " \n"
                        line = line[ifen + 2:len(line)]
                    else:
                        line1 = line[0:izk + 1] + " \n"
                        line = line[izk + 2:len(line)]
                    lines, multidef_or_nonstand = zkf_exist(izk, ifen, line1, multidef_or_nonstand, lines)
                    ifen = line.find(";")
                    izk = line.find("{")
                    iyk = line.find("}")
                while iyk < izk and ifen < izk and iyk >= 0 and ifen >= 0:  # 截出右括号和分号号之间的代码，调用函数完成
                    if ifen > iyk:
                        line1 = line[0:ifen + 1] + " \n"
                        line = line[ifen + 2:len(line)]
                    else:
                        line1 = line[0:iyk + 1] + " \n"
                        line = line[iyk + 2:len(line)]
                    lines, multidef_or_nonstand = ykf_exist(iyk, ifen, line1, multidef_or_nonstand, lines)
                    ifen = line.find(";")
                    izk = line.find("{")
                    iyk = line.find("}")
                while iyk < ifen and izk < ifen and izk >= 0 and iyk >= 0:  # 截出右括号和左括号之间的代码，调用函数完成
                    if izk - 2 >= 0 and line[izk - 2] == "=":
                        lines.append(line[0:ifen + 1] + " \n")
                        line = line[ifen + 2:len(line)]
                    else:
                        if izk > iyk:
                            line1 = line[0:izk + 1] + " \n"
                            line = line[izk + 2:len(line)]
                        else:
                            line1 = line[0:iyk + 1]
                            line = line[iyk + 2:len(line)] + " \n"
                        lines, multidef_or_nonstand = zyk_exist(izk, iyk, line1, multidef_or_nonstand, lines)
                    if len(line) < 3:
                        ifen = izk = iyk = -1
                        break
                    ifen = line.find(";")
                    izk = line.find("{")
                    iyk = line.find("}")
                if ifen == -1 and len(line) > 1:  # 只有左括号和右括号
                    lines, multidef_or_nonstand = zyk_exist(izk, iyk, line, multidef_or_nonstand, lines)
                    break
                elif izk == -1 and len(line) > 1:  # 只有右括号和分号
                    lines, multidef_or_nonstand = ykf_exist(iyk, ifen, line, multidef_or_nonstand, lines)
                    break
                elif iyk == -1 and len(line) > 1:  # 只有左括号和分号
                    lines, multidef_or_nonstand = zkf_exist(izk, ifen, line, multidef_or_nonstand, lines)
                    break
                elif iyk == -1 and izk == -1 and ifen == -1:  # 都不存在
                    if len(line) < 3:
                        break
                    lines, multidef_or_nonstand = nonexist(line, lines, multidef_or_nonstand)
                    break
            continue
    return lines


def remove_variable(lines):
    global count_nonstandard
    global count_fen_for
    indvariable = []  # 自变量
    function = []  # 函数
    shenming_function = []  # 函数声明
    array = []  # 数组
    define = []  # 宏定义
    typedef = []  # typedef
    typedef_type = []

    enum_val = []
    enum = []

    judge_action_scope = False
    count_scope = -1  # 同名不可见的判断

    struct_name = []  # 不同的结构体类型名
    shengming_struct = []  # 结构体的提前声明
    judge_struct_variable = True
    judge_struct = True  # 判断结构体的定义有没有完结
    type = ['void', 'int', 'double', 'char', 'bool', 'FILE']
    before_type = ['static', 'extern', 'const']
    behind_type = ['*', 'const', '&']

    for ii in range(len(lines)):
        line = lines[ii]
        # 5、删除printf(cout中的内容有待补充)，为后续步骤做准备
        if line.find('printf') >= 0 or line.find("fopen") >= 0 or line.find("fscanf") >= 0 or line.find("scanf") >= 0:
            st = line.find('\"')
            ed = line.rfind('\"')
            line = line[0:st] + " " + line[ed + 1: len(line)]
        list = line.split(" ")
        if count_scope > 0:
            for ic in range(len(list)):
                if list[ic] == "{":
                    count_scope = count_scope + 1
                elif list[ic] == "}":
                    count_scope = count_scope - 1
        i = 0

        while i < len(list):
            if list[i] in typedef and judge_action_scope is False:
                if i == 0 or list[i - 1] not in struct_name and list[i - 1] not in type:
                    list[i] = typedef_type[typedef.index(list[i])]

            '''1、首先将所有整型都归为int，浮点型都归为 double'''
            if list[i] == "short":
                if list[i + 1] == "int":
                    list.pop(i)
                else:
                    list[i] = "int"
            elif list[i] == "long":
                if list[i + 1] == "int":
                    list.pop(i)
                elif list[i + 1] == "long":
                    list[i] = "int"
                    list.pop(i + 1)
                elif list[i + 1] == "double":
                    list.pop(i)
                else:
                    list[i] = "int"
            elif list[i] == "int" and list[i + 1] == "int":
                list.pop(i)
            elif list[i] == "float":
                list[i] = "double"
            i = i + 1
        lines[ii] = " ".join(list)

        i = 0
        '''if list[0]==结构体 或者 类 或者 宏定义 或者 typedef'''
        if list[i] == "#" and list[i + 1] == "define":  # 说明是宏定义#define Maxsize(a,b) a*b*10005
            define.append(list[i + 2])
            list.pop(i + 2)
            lines[ii] = " ".join(list)
            continue
        if list[i] == "typedef" and list[i + 1] in before_type:
            list.pop(i + 1)
        if list[i] == "typedef" and list[i + 1] != "struct" and list[i + 1] != "enum":
            # 说明形如 typedef int KeyType; 或者 typedef char* str;
            typedef.append(list[i + 2])
            list.pop(i + 2)
            lines[ii] = " ".join(list)
            typedef_type.append(list[i + 1])
            continue  # ---------------------------------typedef char* str;-------------------------------------有待完善



        elif list[i] == "typedef" and list[i + 1] == "enum":  # 枚举类型
            if line.find(";") == -1:
                lines[ii] = ''
                lines[ii + 1] = line.strip() + " " + lines[ii + 1]
                continue
            else:
                while list[i] != "{":
                    i = i + 1
                i = i + 1
                while list[i] != "}":
                    if list[i] != ",":
                        enum_val.append(list[i])
                    i = i + 1
                i = i + 1
                while list[i] != ";":
                    if list[i] != ",":
                        enum.append(list[i])
                    i = i + 1
            continue


        # --------------------------typedef const struct{}name;-------------------------------------------------有待完善
        elif list[i] == "typedef" and list[i + 1] == "struct":
            if list[i + 2] != "{" and list[i + 2] != "\n":
                list[i + 1] = list[i + 1] + " " + list[i + 2]
                list.pop(i + 2)  # 此时list[i+2]应该是'\n' 或者'{' 或者 name结构体别名

                if list[i + 1] in struct_name and list[i + 1] not in shengming_struct:
                    '''typedef struct name name1; 该结构体已经定义过了，这个时候是另外起别名'''
                    i = i + 2
                    while i < len(list) and list[i] != ";":
                        if list[i] != "," and list[i] != '\n':  # 注意这里还应该考虑最后一个字符是换行符的情况
                            struct_name.append(list[i])
                        i = i + 1
                else:
                    '''说明该结构体没有定义过，这个时候定义，有可能还起别名,也可能是提前声明'''
                    if (lines[ii].find(";") >= 0 and lines[ii].find("{") == -1) or (
                            lines[ii].find("{") == -1 and lines[ii].find(";") == -1 and ii + 1 < len(lines) and lines[
                        ii + 1].find("{") == -1 and lines[ii + 1].find(";") >= 0):
                        '''是结构体的提前声明 typedef struct name name1;'''
                        shengming_struct.append(list[i + 1])
                        i = i + 2
                        while i < len(list) and list[i] != ";":
                            if list[i] != "," and list[i] != '\n':  # 注意这里还应该考虑最后一个字符是换行符的情况
                                struct_name.append(list[i])
                            i = i + 1
                    else:
                        '''typedef struct name{}name1,*name2,name3;'''
                        if list[i + 1] in shengming_struct:
                            shengming_struct.remove(list[i + 1])
                        judge_struct = False
                        struct_name.append(list[i + 1])
            else:
                '''typedef struct{}name1,name2,name3;'''
                judge_struct = False
            continue

        elif list[i] == "struct":
            jd_sm_variable = -1
            if list[i] + " " + list[i + 1] in shengming_struct:  # 在此之前肯定还没有定义这个结构体
                '''这里应该是定义结构体或者定义变量'''
                '''定义变量有一个特点，它必须是指针类型，即struct name (const) *变量;'''
                if (line.find("*") >= 0 and line.find("{") == -1) or (
                        ii + 1 < len(lines) and lines[ii + 1].find("*") >= 0 and lines[ii + 1].find("{") == -1):
                    '''说明是定义变量'''
                    jd_sm_variable = 1
                else:
                    '''说明是定义结构体'''
                    jd_sm_variable = 0

            if list[i] + " " + list[i + 1] in struct_name or jd_sm_variable == 1:
                '''struct name 变量1,变量2,变量3;'''
                list[i] = list[i] + " " + list[i + 1]
                list.pop(i + 1)
            elif (list[i] + " " + list[i + 1] not in struct_name and list[
                i + 1] != "{" and list[i + 1] != "\n") or jd_sm_variable == 0:  # 定义结构体类型
                '''struct name{};'''
                '''struct name{}变量1,变量2,变量3;'''
                '''struct name;结构体的提前声明'''
                list[i] = list[i] + " " + list[i + 1]
                list.pop(i + 1)  # 这个时候list[i+1]可能是";" 或者"{"或者"\n"
                struct_name.append(list[i])
                if i + 1 < len(list) and list[i + 1] == ";":
                    '''struct name;结构体的提前声明'''
                    shengming_struct.append(list[i])
                    continue
                elif list[i + 1] == "{" or list[i + 1] == "\n":
                    '''struct name{};'''
                    '''struct name{}变量1,变量2,变量3;'''
                    if jd_sm_variable == 0:
                        shengming_struct.remove(list[i])
                    judge_struct_variable = False
                    continue
            else:  # 是 struct {}变量1,变量2,变量3;--------#只能在定义结构体变量，不能定义结构体类型
                judge_struct_variable = False
                continue
        '''2、处理变量名,函数名'''
        '''变量和函数名都必须有基本类型或者用户自定义类型
        # int a[]={1,2,3},b=1,c;
        # int a[4]={0};
        '''
        "这是一行代码，一行代码中知可能出项一种基本类型或者一种用户自定义类型（参数除外）"
        while list[i] in before_type:
            i = i + 1
        if list[i] in type or list[i] in struct_name or list[i] in enum:
            i = i + 1
            while i < len(list) - 1:
                while list[i] in behind_type:  # 指针或者常量的存在
                    i = i + 1
                varorfun = list[i]  # 说明是个变量或者数组或者函数
                if varorfun in typedef:  # 判断同名：typedef别名和变量名同名，此时变量名作用域中别名不可见
                    judge_action_scope = True
                    count_scope = 1

                if list[i + 1] == "[":
                    '''说明是个数组,避免出现数组定义多行,需要特殊处理'''
                    array.append(varorfun)
                    while i < len(list) and list[i] != ";" and (
                            list[i] != "," or (list[i] == "," and list[i - 1] != "}" and list[i - 1] != "]")):
                        i = i + 1
                    if i == len(list):  # 说明该行就定义了一个数组，且该数组定义了多行
                        '''例如：int a[]={1,2,3,4
                                    5,6,7}; 判断多行数组的延续'''
                        while lines[ii + 1].find("}") == -1:  # 说明是数组的多行定义,并且该行没有结束定义
                            ii = ii + 1
                        ii = ii + 1
                        line = lines[ii]
                        ik = line.find("}")
                        if line[ik + 2] == ";":  # 说明数组结束定义，且后面没有变量定义了
                            break
                        elif line[ik + 2] == ",":  # 说明数组结束定义，且后面还有变量定义
                            line = line[ik + 2:len(line)]
                            list = line.split(" ")
                            i = 0

                elif list[i + 1] == "=" or list[i + 1] == "," or list[i + 1] == ";":
                    '''说明是自变量(不排除是指针)'''
                    indvariable.append(varorfun)
                    if list[i + 1] == "=":
                        judge = True
                        while i < len(list) - 1 and list[i] != ";" \
                                and (list[i] != "," or (list[i] == "," and judge is False)):
                            if list[i] == "(":
                                judge = False
                            elif list[i] == ")":
                                judge = True
                            i = i + 1

                # 类或者结构体类型函数的定义--------------------------------------------------------------------有待完善
                elif list[i + 1] == "(":
                    '''T=pre();'''
                    '''说明是函数定义，或者函数声明,需要另外再处理'''
                    function.append(varorfun)
                    i = i + 2  # 此时list[i]是基本类型或者用户定义的类型
                    while i < len(list) - 1 and list[i] != ")":  # 进来时 list[i]是"("或者","或者")"

                        if list[i] in type or list[i] in struct_name or list[i] in enum:
                            i = i + 1
                            if list[i] == "," or list[i] == ")" or list[len(list) - 2] == ";":  # 说明是函数声明
                                shenming_function.append(varorfun)
                                function.remove(varorfun)
                                break
                            while i < len(list) - 1 and list[i] in behind_type:  # 指针或者常量的存在
                                i = i + 1
                            if list[i] == "," or list[i] == ")" or list[len(list) - 2] == ";":  # 说明是函数声明
                                shenming_function.append(varorfun)
                                function.remove(varorfun)
                                break
                            varorfun = list[i]  # 保存这个变量或者数组
                            if list[i + 1] == "[":  # 说明是个数组
                                array.append(varorfun)
                                while i < len(list) and list[i] != ";" and (list[i] != "," or (
                                        list[i] == "," and list[i - 1] != "}" and list[i - 1] != "]")):
                                    i = i + 1
                            elif list[i + 1] == "," or list[i + 1] == ")":  # 说明是个变量
                                indvariable.append(varorfun)
                        i = i + 1
                    break
                i = i + 1  # 如果list[i]是","或者";"，则此处加一正好处理这个问题

        elif list[i] == "}" and judge_struct is False:
            # 说明这行代码结束结构体的定义,可能有起别名----------------------------------------------直到找到分号才算结束
            if line.find(";") >= 0:
                judge_struct = True
                i = i + 1
                while i < len(list) - 1:
                    while i < len(list) and list[i] in behind_type:
                        i = i + 1
                    struct_name.append(list[i])
                    i = i + 1
                    if list[i] == ",":
                        i = i + 1
                    elif list[i] == ";":
                        break
            else:
                lines[ii] = ""
                lines[ii + 1] = line.strip() + " " + lines[ii + 1]

        elif list[i] == "}" and judge_struct_variable is False:
            # 定义变量，这行代码结束结构体的定义----------------------------------------------直到找到分号才算结束
            if line.find(";") >= 0:
                judge_struct_variable = True
                if list[i + 1] == ";":
                    continue
                else:
                    i = i + 1
                    while list[i] in behind_type:
                        i = i + 1
                    while i < len(list) and list[i] != "\n":
                        indvariable.append(list[i])
                        while i < len(list) and list[i] != ";" and (
                                list[i] != "," or (list[i] == "," and list[i - 1] != "}" and list[i - 1] != "]")):
                            i = i + 1
                        i = i + 1
                continue
            else:
                lines[ii] = ""
                lines[ii + 1] = line.strip() + " " + lines[ii + 1]
        if count_scope == 0:
            judge_action_scope = False

    lines_list = []
    for line in lines:
        list = line.split(" ")
        i = 0
        if line.find("scanf") >= 0:
            i = list.index(",")
        while i < len(list):
            if (list[i] in array) or (list[i] in function) or (list[i] in indvariable):
                if list[i] == "main":
                    break
                try:
                    list.pop(i)
                except:
                    pass
            elif list[i] in define:
                list[i] = "define"
            elif list[i] in typedef:
                list[i] = typedef_type[typedef.index(list[i])]
            elif list[i] == "struct" and list[i + 1] != "{":
                list.pop(i + 1)
            elif list[i] in struct_name:
                list[i] = "struct"
            elif line.find("include") >= 0:
                list = []
            elif list[i] in enum:
                list[i] = "enum"
            elif list[i] in enum_val:
                list[i] = "enum_val"
            i = i + 1
        if " ".join(list).find("struct struct") >= 0:
            lines_list.append(" ".join(list).replace("struct struct", "struct"))
        else:
            lines_list.append(" ".join(list))
    # print("函数声明：",shenming_function)
    return lines_list, array, indvariable, function, typedef, struct_name, define, enum, enum_val, count_nonstandard, count_fen_for


def solve(text):
    solve_char = [']', ')', '}']
    liness = []
    lines = standardisation(text)
    lines, array, indvariable, function, typedef, struct_name, define, enum, enum_val, count_nonstandard, count_fen_for = remove_variable(
        lines)
    for line in lines:
        list = line.strip().split(" ")
        i = 0
        while i < len(list):
            if list[i] in solve_char:
                list.pop(i)
            elif list[i] == "int":
                list[i] = 'A'
            elif list[i] == "double":
                list[i] = 'B'
            elif list[i] == "char":
                list[i] = 'C'
            elif list[i] == "unsigned":
                list[i] = 'D'
            elif list[i] == "short":
                list[i] = 'E'
            elif list[i] == "struct":
                list[i] = 'F'
            elif list[i] == "enum":
                list[i] = 'G'
            elif list[i] == "define":
                list[i] = 'H'
            elif list[i] == "typedef":
                list[i] = 'I'
            elif list[i] == "static":
                list[i] = 'J'
            elif list[i] == "const":
                list[i] = 'K'
            elif list[i] == "bool":
                list[i] = 'L'
            elif list[i] == "void":
                list[i] = 'M'
            elif list[i] == "float":
                list[i] = 'N'
            elif list[i] == "sizeof":
                list[i] = 'A'
            elif list[i] == "scanf":
                list[i] = 'O'
            elif list[i] == "fscanf":
                list[i] = 'P'
            elif list[i] == "printf":
                list[i] = 'Q'
            elif list[i] == "fprintf":
                list[i] = 'R'
            elif list[i] == "return":
                list[i] = 'S'
            elif list[i] == "do":
                list[i] = 'T'
            elif list[i] == "if":
                list[i] = 'U'
            elif list[i] == "else":
                list[i] = 'V'
            elif list[i] == "while":
                list[i] = 'W'
            elif list[i] == "switch":
                list[i] = 'X'
            elif list[i] == "case":
                list[i] = 'Y'
            elif list[i] == "break":
                list[i] = 'Z'
            elif list[i] == "continue":
                list[i] = 'a'
            elif list[i] == "default":
                list[i] = 'b'
            elif list[i] == "using":
                list[i] = 'c'
            elif list[i] == "for":
                list[i] = 'd'
            elif list[i] == "inline":
                list[i] = 'e'
            elif list[i] == "extern":
                list[i] = 'f'
            elif list[i] == 'main':
                list[i] = "m"
            i = i + 1
        liness.append("".join(list))
        # liness.extend(list)
    return liness


file1 = open(r'try1.txt', 'r')
text1 = file1.readlines()
file1.close()
lines1 = solve(text1)
lines_1 = ''.join(lines1)
file11 = open(r'try11.txt', 'w')
file11.write(lines_1)
file11.close()

file2 = open(r'try2.txt', 'r')
text2 = file2.readlines()
file2.close()
lines2 = solve(text2)
lines_2 = ''.join(lines2)
file22 = open(r'try22.txt', 'w')
file22.write(lines_2)
file22.close()

'''
file1 = open(r'try2.txt', 'r')
text1 = file1.readlines()
file1.close()
lines = standardisation(text1)
lines, array, indvariable, function, typedef, struct_name, define, enum, enum_val, count_nonstandard, count_fen_for = remove_variable(
    lines)
print("数组：")
print(array)
print("自变量：")
print(indvariable)
print("函数：")
print(function)
print("typedef:")
print(typedef)
print("宏定义：")
print(define)
print("结构体")
print(struct_name)
print("枚举类")
print(enum)
print("枚举内容")
print(enum_val)
print("不规范次数")
print(count_nonstandard)
print("多句一行数")
print(count_fen_for)
Lines = []
string = ''
for str in lines:
    ''
    if str not in Lines:
        Lines.append(str)
        string = string + str
    ''
    string = string + str
file2 = open(r'try22.txt', 'w')
file2.write(string)
file2.close()

'''

count_same = 0
sum1 = len(lines1) + len(lines2)
list_string1 = lines1[:]
string12 = []
for line in lines2:
    if line in list_string1:
        list_string1.remove(line)
        count_same = count_same + 1
    else:
        string12.append(line)
sum2 = len(list_string1) + count_same + len(string12)
sim = (sum1 - sum2) * 1.0 / len(lines1)
print('相似度：', sim)

'''
count_same = 0
sum1 = len(lines1) + len(lines2)
list_string1 = lines1[:]
string12 = []
for str in lines2:
    if str in list_string1:
        list_string1.remove(str)
        count_same = count_same + 1
    else:
        string12.append(str)
sum2 = len(string12) + len(list_string1) + count_same
sim = (sum1 - sum2) * 1.0 / len(lines1)
print("相似度1：", sim)
'''
