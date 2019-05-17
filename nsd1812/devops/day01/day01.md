# tedu_devops_day01
## 多进程
linux采用fork方式执行程序。当运行程序（命令）时，
系统将会把父进程的资源拷贝一份，生成子进程。程序、命令在子进程中运行。
当命令执行完毕后，子进程销毁。
### 执行shell的方式
- bash xxx.sh: 指定使用bash解释脚本，fork执行
- ./xxx.sh: 根据脚本第一行指定的解释器选择解释方法，fork执行
- source xxx.sh: 在当前进程中执行指令，不采用fork方式
### os.fork()方法
os.fork()针对父子进程都有返回值。父进程的返回值是非0值（子进程的ID号），
子进程返回0