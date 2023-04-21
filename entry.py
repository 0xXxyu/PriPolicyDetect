
'''
YEDDA标记内容提取
'''
import re
import os
import sys


# 查找.ann文件中的3种标记，并分别存储在3个txt文件中，每个txt中的各个标记需去重
def get_info_in_label():
    read_path ='I:/IoTSensitiveDataAnalysis/数据/xml文件/标签提取/'                                     #修改1
    read_filename = 'huami.txt.ann'                                   #修改2
    read_file_path = os.path.join(read_path, read_filename)

    # 保存在本地
    write_path = 'I:/IoTSensitiveDataAnalysis/数据/xml文件/标签敏感信息提取/'       #修改3
    write_filename1 = 'huami.txt'
    write_path1 = os.path.join(write_path, write_filename1)

    write_filename2 = '2second.txt'
    write_path2 = os.path.join(write_path, write_filename2)

    write_filename3 = '3third.txt'
    write_path3 = os.path.join(write_path, write_filename3)

    first_class_list = []
    second_class_list = []
    third_class_list = []  # first_class_list = second_class_list = third_class_list = []这样复制就共享一个内存了
    try:
        with open(read_file_path, encoding='utf-8') as f:
            for linex in f:
                line = linex.strip()

                all_re = re.findall(r'\[@.*?级敏感数据\*\]', line)
                if all_re:
                    for i in all_re:
                        if '1级敏感数据'in i:
                            j = i.lstrip('[@').rstrip('#1级敏感数据*]').strip()
                            if j not in first_class_list:
                                first_class_list.append(j)
                        elif '2级敏感数据'in i:
                            j = i.lstrip('[@').rstrip('#2级敏感数据*]').strip()
                            if j not in second_class_list:
                                second_class_list.append(j)
                        elif '3级敏感数据' in i:
                            j = i.lstrip('[@').rstrip('#3级敏感数据*]').strip()
                            if j not in third_class_list:
                                third_class_list.append(j)
                        else:
                            print('提取的数据并非敏感数据，请改善正则表达式')
                            sys.exit()  # 退出程序
    except Exception as e:
        print('detail error:', e)

    # 存储
    try:
        with open(write_path1, 'a', encoding='utf-8') as f1:  # 用a，用于添加
            for i in first_class_list:
                f1.write(i + '\n')  # 写入数据
        '''
        with open(write_path2, 'a', encoding='utf-8') as f2:  # 用a，用于添加
            for i in second_class_list:
                f2.write(i + '\n')  # 写入数据
        with open(write_path3, 'a', encoding='utf-8') as f3:  # 用a，用于添加
            for i in third_class_list:
                f3.write(i + '\n')  # 写入数据
        '''
    except Exception as e:
        print('detail error:', e)
    print('处理完毕')


# 判断原始文本里面是否有敏感数据
def judge_class_in_text():
    # 读取原始文本
    read_path = os.getcwd() + '/data/0raw/xiaomi4'                            #修改4
    read_filename = 'xiaomi4Sum_utf-8.txt'                                            #修改5
    read_file_path = os.path.join(read_path, read_filename)

    first_list = []  # 所有1级敏感数据
    second_list = []  # 所有2级敏感数据
    third_list = []  # 所有3级敏感数据

    # 读取敏感文本
    sen_path = os.getcwd() + '/data/1get_info_in_label/xiaomi4'           #修改6
    sen_filename1 = '1first.txt'
    sen_file_path1 = os.path.join(sen_path, sen_filename1)
    with open(sen_file_path1, encoding='utf-8') as f:
        for linex in f:
            line = linex.strip()
            first_list.append(line)

    sen_filename2 = '2second.txt'
    sen_file_path2 = os.path.join(sen_path, sen_filename2)
    with open(sen_file_path2, encoding='utf-8') as f:
        for linex in f:
            line = linex.strip()
            second_list.append(line)

    sen_filename3 = '3third.txt'
    sen_file_path3 = os.path.join(sen_path, sen_filename3)
    with open(sen_file_path3, encoding='utf-8') as f:
        for linex in f:
            line = linex.strip()
            third_list.append(line)

    # 保存在本地
    write_path = os.getcwd() + '/data/2judge_class_in_text'
    write_filename = 'xiaomi4_class_in_text.txt'                   #修改7
    write_path = os.path.join(write_path, write_filename)

    try:
        with open(read_file_path, encoding='utf-8') as f:
            current_url_flag = False
            current_url = ''
            for linex in f:
                line = linex.strip()
                if current_url_flag:
                    if 'http' in line:  # 如果连续2行都是url，那么取后出现的url作为当前url（不清楚文本是否有这种连续2行都是url的数据）
                        current_url = line
                        current_url_flag = True
                        continue
                    if '{"' in line or '{\'' in line:
                        current_first_list=[]  # 1级敏感数据
                        current_second_list=[]  # 2级敏感数据
                        current_third_list=[]  # 3级敏感数据

                        for i in first_list:  # first_list为所有1级敏感数据
                            if i in line:  # 当前line是否存在敏感数据
                                current_first_list.append(i)
                        for i in second_list:  # second_list为所有2级敏感数据
                            if i in line:  # 当前line是否存在敏感数据
                                current_second_list.append(i)
                        for i in third_list:  # third_list为所有3级敏感数据
                            if i in line:  # 当前line是否存在敏感数据
                                current_third_list.append(i)

                        if (current_first_list!=[]) | (current_second_list!=[]) | (current_third_list!=[]):
                            # 把判断原始文件是否存在敏感数据的结果写入文件中
                            with open(write_path, 'a', encoding='utf-8') as f1:  # 用a，用于添加
                                f1.write(current_url + '\n')  # 写入url
                                if current_first_list:
                                    new_line = ''
                                    for i in current_first_list:
                                        new_line += i+','
                                    new_line = '1级敏感数据：' + new_line.rstrip(',')
                                    f1.write(new_line + '\n')  # 写入数据
                                if current_second_list:
                                    new_line = ''
                                    for i in current_second_list:
                                        new_line += i+','
                                    new_line = '2级敏感数据：' + new_line.rstrip(',')
                                    f1.write(new_line + '\n')  # 写入数据
                                if current_third_list:
                                    new_line = ''
                                    for i in current_third_list:
                                        new_line += i+','
                                    new_line = '3级敏感数据：' + new_line.rstrip(',')
                                    f1.write(new_line + '\n')  # 写入数据
                        # 判断下一组数据前先初始化，一组数据为：url+字典数据
                        current_url_flag = False
                        current_url = ''
                    elif line.startswith('---'):  # url到'----...'之间没有字典数据
                        current_url_flag = False
                        current_url = ''
                    else:  # 可能url和字典数据之间间隔了一行appid数据
                        continue
                else:
                    if 'http' in line:
                        current_url_flag = True
                        current_url = line
                        continue
                    else:
                        continue
    except Exception as e:
        print('detail error:', e)
    print('处理完毕')


'''
def old_get_info_in_label():
    read_path = os.getcwd() + '/data/0raw'
    read_filename = 'HONORSum.txt.ann'
    read_file_path = os.path.join(read_path, read_filename)

    # 保存在本地
    write_path = os.getcwd() + '/data/get_info_in_label'
    write_filename1 = '1first.txt'
    write_path1 = os.path.join(write_path, write_filename1)

    write_filename2 = '2first.txt'
    write_path2 = os.path.join(write_path, write_filename2)

    write_filename3 = '3first.txt'
    write_path3 = os.path.join(write_path, write_filename3)

    first_class_list = second_class_list = third_class_list = []
    try:
        with open(read_file_path, encoding='utf-8') as f:
            for linex in f:
                line = linex.strip()

                # 匹配1级敏感数据
                first_re = re.findall(r'\[@.*?#1级敏感数据\*\]', line)  # 这样可能匹配到:'[@token#3级敏感数据*]":"CgB6e3x9":1,"[@tokenType#1级敏感数据*]'

                if first_re:
                    for i in first_re:
                        j = i.lstrip('[@').rstrip('#1级敏感数据*]').strip()
                        if j not in first_class_list:
                            first_class_list.append(j)

                # 匹配2级敏感数据

                second_re = re.findall(r'\[@.*?#2级敏感数据\*\]', line)
                if second_re:
                    for i in second_re:
                        j = i.lstrip('[@').rstrip('#2级敏感数据*]').strip()
                        if j not in second_class_list:
                            second_class_list.append(j)

                # 匹配3级敏感数据
                third_re = re.findall(r'\[@.*?#3级敏感数据\*\]', line)
                if third_re:
                    for i in third_re:
                        j = i.lstrip('[@').rstrip('#3级敏感数据*]').strip()
                        if j not in third_class_list:
                            third_class_list.append(j)

                if third_re:
                    first_class=line
                    second_class=line
                    third_class=line
                    with open(write_path, 'a', encoding='utf-8') as print_name_and_version_f:  # 用a，用于添加
                        print_name_and_version_f.write('s' + '\n')  # 写入数据
    except Exception as e:
        print('detail error:',e)
        print('...')
'''


if __name__ == '__main__':
    get_info_in_label()  # 查找.ann文件中的3种标记，并分别存储在3个txt文件中，每个txt中的各个标记需去重
    # judge_class_in_text()  # 判断原始文本里面是否有敏感数据


