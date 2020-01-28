# import os
#os.mkdir('I:\\Users\\doc_test\\os.txt')
# fsers\\doc_test\\text.txt',1,'r')
# help(os.open)
import re

# f =  open('I:\\Users\\doc_test\\158.plt', 'r')

# 创建一个list存放PD数据
# PD_list = []
x_data = []
y_data = []
pattern = r"PD(.*?);"
# for line in f.readlines():
#     print(line)
# print(f)
with open('I:\\Users\\doc_test\\1214.plt', 'r') as f:
    content = f.read()
    # print(content)
    result = re.findall(pattern, content)       # 返回一个字符串列表
    # data = ','.join(result)
    # print(result)

for j in range(len(result)):        # 遍历所有的坐标、将X坐标、Y坐标添加到列表中
    x_data.append(int(result[j].split(',')[0]))
    y_data.append(int(result[j].split(',')[1]))

print("x轴、y轴的坐标为: ", x_data, y_data)
print('X轴坐标的范围为: ', sorted(x_data)[0], sorted(x_data)[-1])
print('Y轴的坐标范围为: ', sorted(y_data)[0], sorted(y_data)[-1])



# f.close()