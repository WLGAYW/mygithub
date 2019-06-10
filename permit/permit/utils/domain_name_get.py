import os
import re


# 进行文件内容提取
def get_domain_name():
    main_path = os.getcwd()
    os.chdir(main_path + '/' + 'permit' + '/' + 'permit' + '/' + 'essential_resource')

    domain_name_list = []
    with open('part-00000', 'r') as f:
        for line in f:
            re_one_data = line.replace('http://', '')
            re_two_data = re_one_data.replace('https://', '')
            re_three_data = re_two_data.replace('www.', '')
            domain_name = re_three_data.split()[0]
            domain_name_list.append(domain_name)

    return domain_name_list
