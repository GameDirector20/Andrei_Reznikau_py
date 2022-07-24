def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

n = 0

while True:
    print(f'''{'' if n > 0 else 'Dear User,'}
{'P' if n > 0 else 'p'}lease, enter the maximal quantity of symbols in the line (more than 35) {'again' if n > 0 else ''}
in order to justify the text and to make it more beautiful:''')

    n += 1

    width = input()

    if not is_number(width):
        print('\nPlease, type only integer.')
        continue


    if int(width) <= 35:
        print('\nPlease, type the amount of symbols more than 35.')
        continue
    
    break
    
width = int(width)


with open('text.txt', 'r') as f:
    
    line_lst = []
    curs_pos = 0
    
    while True:

        chunk = f.readline(width)


        if not chunk:
            break

        if not '\n' in chunk:
            p_i = ''
            n = 0
            for i in chunk[::-1]:
                            
                if (p_i == ' ' or p_i == '\t') and (i != ' ' and i != '\t'):
                    line_lst.append(chunk[0:len(chunk)-n]) # '\n' was deleted
                    f.seek(f.tell() -n) # It is needed to know how define the current position of coursour aytomatically: Cur_pos - n
                    #curs_pos -= n
                    #curs_pos_1 = f.tell()
                    break
                
                p_i = i
                n += 1
            else:
                line_lst.append(chunk)

            

        else:
            line_lst.append(chunk)


    # with open('text2.txt', 'w') as f_new:
    #     f_new.writelines(line_lst)
    
        
# for op in line_lst:
#     print(op)

# # t_just = chunk

# # script is making the text justified 


for el in range(len(line_lst)):
    
    t_just_l = line_lst[el].split(' ')

    ind = 0
    for ind in range(len(t_just_l)-1):
        if t_just_l[ind] == '':
            t_just_l.pop(ind)
        else:
            break

    t_just = ' '.join(t_just_l)


    if not '\n' in t_just:

    
        while '  ' in t_just:
            t_just = t_just.replace('  ', ' ')
        
        if ' ' in t_just:
            q_sp_wid = width - len(t_just)

            tj_list = t_just.split(' ')
            q_sp_cur = len(tj_list) - 1

        
        if q_sp_wid % q_sp_cur > 0:
            n_i = 0
            for i in range(len(tj_list)):
                n_i += 1
                tj_list[i] = tj_list[i] + ' '

                if q_sp_wid % q_sp_cur == n_i:
                    break

        
        res_sp = ' '*((q_sp_wid // q_sp_cur) + 1)

        res = res_sp.join(tj_list) # STR-result as text justified

        line_lst[el] = res + '\n'

    else:
        line_lst[el] = t_just


with open('text2.txt', 'w') as f_new:
    f_new.writelines(line_lst)
    

print('The file with text justified is recorded. Please, enjoy:)')

# # to check if the file recorded in full
    
# print(chunk)
# print(len(chunk))
    
# print(res)
# print(len(res))   





# print(width, type(width))
