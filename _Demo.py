from tkinter import *
import requests
import re

# 查询函数, 接收用户输入的ip地址
def find_position():
    # 获取输入信息
    ip = ip_input.get()
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Referer': 'https://www.ipip.net/ip.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    # 向ip查询网址发送请求并获取返回数据
    r = requests.get('https://www.ipip.net/ip/{}.html'.format(ip), headers=headers).text
    # 正则表达式
    address = re.search(r'地理位置.*?;">(.*?)</span>', r, re.S)
    #啊po瑞得儿
    operator = re.search(r'运营商.*?;">(.*?)</span>', r, re.S)
    time = re.search(r'时区.*?;">(.*?)</span>', r, re.S)
    wrap = re.search(r'地区中心经纬度.*?;">(.*?)</span>', r, re.S)

    # 判断是否匹配成功
    if address:
        # 匹配成功则一定有ip和地理位置信息
        ip_info = ['地理位置:   ' + address.group(1), '当前IP:   ' + ip]
        # 分别判断其他信息匹配结果, 成功则加入临时列表
        if operator:
            ip_info.insert(0, '所有者/运营商:   ' + operator.group(1))
        if time:
            ip_info.insert(0, '时区:   ' + time.group(1))
        if wrap:
            ip_info.insert(0, '地区中心经纬度:   ' + wrap.group(1))
        # 清空之前的回显列表
        display_info.delete(0, 5)

        # 为回显列表赋值
        for item in ip_info:
            display_info.insert(0, item)
    else:
        display_info.delete(0, 5)
        display_info.insert(0, "无效的ip!")


# 创建主窗口
root = Tk()
# 设置标题内容
root.title("逻辑-ip定位")
# 创建输入框并设置尺寸
ip_input = Entry(root, width=40)
# 创建一个回显列表
display_info = Listbox(root, width=60, height=10)
# 创建查询按钮
result_button = Button(root, command=find_position, text=" 查 询 ")

if __name__ == '__main__':
    # 完成布局  显示
    ip_input.pack()
    display_info.pack()
    result_button.pack()
    root.mainloop()
