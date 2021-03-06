# 计算机网络编程

使用C/C++的socket进行的网络编程

|        Name         |                        Description                         | Note |
| :-----------------: | :--------------------------------------------------------: | :--: |
|      time_sync      |               基于流式套接字的时间同步服务器               |      |
|      readline       | 基于流式套接字的服务器回射程序，每次交互读取用户的一行输入 |      |
|   fixedLengthRecv   |      基于流式套接字的服务器回射程序，定长方式接收数据      |      |
| variableLengthRecv  |      基于流式套接字的服务器回射程序，变长方式接收数据      |      |
|  concurrencyServer  |   基于流式套接字的服务器回射程序，服务器采用并发方式设计   |      |
|    udpEcho-cycle    |    基于数据报套接字的回射程序，服务器采用循环服务器设计    |      |
| udpEcho-concurrency |    基于数据报套接字的回射程序，服务器采用并发服务器设计    |      |

## 简介

### 基于流式套接字的时间同步服务器

要求使用流式套接字编程，实现时间同步服务器和客户端，该服务器能够接收客户端的查询请求，获取本地时间，并将结果发送回客户端，客户端将该时间显示出来，如图1所示。

提示&注意：

+  time()函数、ctime()函数为时间处理函数。

+ 客户的recv函数需要循环接收。

![image-20201106164142603](https://gitee.com/yubinCloud/my-imgs-repo/raw/main/img/image-20201106164142603.png)

### 基于流式套接字的服务器回射程序

编写一服务器程序和客户程序，要求客户每输入数据，服务器接收后**原样**回送给客户程序。

![image-20201106211814784](https://gitee.com/yubinCloud/my-imgs-repo/raw/main/img/image-20201106211814784.png)

+ 实现并发服务器时，要求并发服务器的实现采用创建线程或子进程的方式实现。

  >  主线程/主进程：
  >
  > 创建套接字并将其绑定到服务器所使用的熟知地址上。
  >
  > 重复调用accept接收客户端的请求,并且创建子线程/子进程处理响应。
  >
  > 子线程/子进程：
  >
  > 与客户端进行交互：接收请求并发回应答；
  >
  > 关闭连接并退出。子线程/子进程在处理完来自一个客户端的所有请求后退出。

### 基于数据报套接字的回射程序

编写一服务器程序和客户程序， 如图1， 要求客户每输入一行数据，服务器接收后加上echo:回送给客户程序，当客户输入“q”后退出。  

![image-20201107161812083](https://gitee.com/yubinCloud/my-imgs-repo/raw/main/img/image-20201107161812083.png)

要求分别以循环服务器和并发服务器实现。  