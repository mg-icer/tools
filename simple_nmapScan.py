#!/usr/local/python3
# coding:utf-8
# nmap端口扫描器简略版
# 教程参考：https://juejin.cn/post/6976264296732819463
#       https://www.cnblogs.com/bmjoker/p/10574598.html
###########
# 使用方法：
# python .\nmap_scan.py 192.168.0.1 线程数
# python .\nmap_scan.py 192.168.0.0/24 线程数
###########
import sys
from concurrent.futures import ThreadPoolExecutor
import netaddr
import nmap


# mun = 10

def alive(ip):
    # print(ip)
    nm = nmap.PortScanner()
    data = nm.scan(hosts=ip)
    # print(data)
    for ip in data['scan'].keys():
        print('ip存活：' + ip)
        for port in data['scan'][ip]['tcp'].keys():
            # print(port)
            resoult1 = ip + ':' + str(port)  # 将端口转换为字符串并拼接到IP地址上
            # print(resoult)
            product = data['scan'][ip]['tcp'][port]['product']
            resoult2 = resoult1 + '    ' + product  # 将端口转换为字符串并拼接到IP地址上
            print(resoult2)


def main():
    ips = sys.argv[1]
    num = int(sys.argv[2])
    pool = ThreadPoolExecutor(num)  # 创建线程池
    # processes=5
    # pool=threading.Semaphore(processes)#多线程数
    target_ips = netaddr.IPNetwork(ips)  # 将一个字符串识别为一个网络号
    # print(target_ips)
    with pool:
        for ip in target_ips:
            ip_str = str(ip)
            # print(ip_str)
            pool.submit(alive, ip_str)  # 开启线程，调用alive函数
            # scan_threath = threading.Thread(target=alive, args=(ip_str,))
            # scan_threath.start()
    pool.shutdown()


if __name__ == "__main__":
    main()
