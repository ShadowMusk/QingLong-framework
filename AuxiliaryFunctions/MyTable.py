from tabulate import tabulate


def createTable(headers, mydata):  # 定义表头

    # 定义数据
    data = mydata
    # 创建表格
    table = tabulate(data, headers=headers)
    # 输出表格
    print(table)
