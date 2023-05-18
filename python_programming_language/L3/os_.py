# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 19:09
# @Author  : yanfa
# @user   : yanfa 
# @File    : os_.py
# @remark: 操作系统模块
"""
os: Operating System
os 模块的常用功能
跨平台的差异"""

"""os的使用
导入os模块"""
import os

# help(os)
# print(dir(os)) #查看属性和常用方法['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_KILLED', 'CLD_STOPPED', 'CLD_TRAPPED', 'DirEntry', 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE', 'F_LOCK', 'F_OK', 'F_TEST', 'F_TLOCK', 'F_ULOCK', 'GenericAlias', 'Mapping', 'MutableMapping', 'NGROUPS_MAX', 'O_ACCMODE', 'O_APPEND', 'O_ASYNC', 'O_CLOEXEC', 'O_CREAT', 'O_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_EXLOCK', 'O_NDELAY', 'O_NOCTTY', 'O_NOFOLLOW', 'O_NONBLOCK', 'O_RDONLY', 'O_RDWR', 'O_SHLOCK', 'O_SYNC', 'O_TRUNC', 'O_WRONLY', 'POSIX_SPAWN_CLOSE', 'POSIX_SPAWN_DUP2', 'POSIX_SPAWN_OPEN', 'PRIO_PGRP', 'PRIO_PROCESS', 'PRIO_USER', 'P_ALL', 'P_NOWAIT', 'P_NOWAITO', 'P_PGID', 'P_PID', 'P_WAIT', 'PathLike', 'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE', 'RTLD_NOLOAD', 'RTLD_NOW', 'R_OK', 'SCHED_FIFO', 'SCHED_OTHER', 'SCHED_RR', 'SEEK_CUR', 'SEEK_DATA', 'SEEK_END', 'SEEK_HOLE', 'SEEK_SET', 'ST_NOSUID', 'ST_RDONLY', 'TMP_MAX', 'WCONTINUED', 'WCOREDUMP', 'WEXITED', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED', 'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG', 'WNOWAIT', 'WSTOPPED', 'WSTOPSIG', 'WTERMSIG', 'WUNTRACED', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_fwalk', '_get_exports_list', '_spawnvef', '_system', '_walk', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chflags', 'chmod', 'chown', 'chroot', 'close', 'closerange', 'confstr', 'confstr_names', 'cpu_count', 'ctermid', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'environb', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchdir', 'fchmod', 'fchown', 'fdopen', 'fork', 'forkpty', 'fpathconf', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 'fwalk', 'get_blocking', 'get_exec_path', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid', 'getgid', 'getgrouplist', 'getgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp', 'getpid', 'getppid', 'getpriority', 'getsid', 'getuid', 'initgroups', 'isatty', 'kill', 'killpg', 'lchflags', 'lchmod', 'lchown', 'linesep', 'link', 'listdir', 'lockf', 'lseek', 'lstat', 'major', 'makedev', 'makedirs', 'minor', 'mkdir', 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty', 'pardir', 'path', 'pathconf', 'pathconf_names', 'pathsep', 'pipe', 'popen', 'posix_spawn', 'posix_spawnp', 'pread', 'preadv', 'putenv', 'pwrite', 'pwritev', 'read', 'readlink', 'readv', 'register_at_fork', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sched_get_priority_max', 'sched_get_priority_min', 'sched_yield', 'sendfile', 'sep', 'set_blocking', 'set_inheritable', 'setegid', 'seteuid', 'setgid', 'setgroups', 'setpgid', 'setpgrp', 'setpriority', 'setregid', 'setreuid', 'setsid', 'setuid', 'spawnl', 'spawnle', 'spawnlp', 'spawnlpe', 'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'st', 'stat', 'stat_result', 'statvfs', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sync', 'sys', 'sysconf', 'sysconf_names', 'system', 'tcgetpgrp', 'tcsetpgrp', 'terminal_size', 'times', 'times_result', 'truncate', 'ttyname', 'umask', 'uname', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'wait', 'wait3', 'wait4', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write', 'writev']



"""一、操作系统相关
"""
#1.获取系统名称
# print(os.name) #posix

#2.获取系统环境变量信息
# print(os.environ) #environ({'PATH': '/usr/bin:/bin:/usr/sbin:/sbin', '__CFBundleIdentifier': 'com.jetbrains.pycharm', 'PYTHONPATH': '/Users/yanfa/PycharmProjects/hogwarts:/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend:/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display', 'SHELL': '/bin/zsh', 'PYTHONIOENCODING': 'UTF-8', 'USER': 'yanfa', 'TMPDIR': '/var/folders/2p/7kdv7_2x3978t76fh68n4nbh0000gn/T/', 'COMMAND_MODE': 'unix2003', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.PyJhEum5wY/Listeners', 'XPC_FLAGS': '0x0', 'PYTHONUNBUFFERED': '1', '__CF_USER_TEXT_ENCODING': '0x1F5:0x19:0x34', 'LOGNAME': 'yanfa', 'LC_CTYPE': 'zh_CN.UTF-8', 'XPC_SERVICE_NAME': 'application.com.jetbrains.pycharm.1007493.1008428', 'PWD': '/Users/yanfa/PycharmProjects/hogwarts/L3', 'PYCHARM_HOSTED': '1', 'HOME': '/Users/yanfa', 'PYCHARM_DISPLAY_PORT': '63342', 'SDKROOT': '/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk', 'CPATH': '/usr/local/include', 'LIBRARY_PATH': '/usr/local/lib'})

#3.获取指定名称的环境变量信息
# print(os.getenv('PATH')) #/usr/bin:/bin:/usr/sbin:/sbin

#4.执行系统指令
# os.system('pwd') #/Users/yanfa/PycharmProjects/hogwarts/L3

"""二、os目录相关
os.getcwd():    获取当前目录
os.chdir():   切换目录
os.listdir():   列出当前目录内容
os.mkdir(): 创建空目录
os.makedirs():  递归创建多级目录
os.rmdir(): 删除空目录
os.rename():    重命名目录
os.remove():    删除文件
"""
#1、os.getcwd():    获取当前目录
# print(os.getcwd()) #/Users/yanfa/PycharmProjects/hogwarts/L3

#2、os.chdir():   切换目录
# os.chdir('..')
# print(os.getcwd())  #/Users/yanfa/PycharmProjects/hogwarts

#3、os.listdir():   列出当前目录内容
# print(os.listdir()) #['huawei', 'L3', 'L2', 'live', '.git', 'L1', 'main.py', '.idea']

#4、os.mkdir(): 创建空目录
# os.mkdir('new')

#5、os.makedirs():  递归创建多级目录
# os.makedirs('a/b/c')

#6、os.rmdir(): 删除空目录
# os.chdir('..')
# print(os.getcwd())
# os.rmdir('new')

#7、os.rename():    重命名目录
# os.rename('a','a1')

#8、os.remove():    删除文件
# os.chdir('..')
# os.remove('main.py')

"""三、os路径相关"""
#1、返回绝对路径 os.path.abspath()
print(os.path.abspath('os_.py')) #/Users/yanfa/PycharmProjects/hogwarts/L3/os_.py

#2、返回文件名 os.path.basename()
print(os.path.basename('os_.py')) #os_.py

#3、返回文件路径 os.path.dirname()
print(os.path.dirname('/python_programming_language/L3/os_.py')) #o/Users/yanfa/PycharmProjects/hogwarts/L3

#4、分割路径 os.path.split()
print(os.path.split('/python_programming_language/L3/os_.py')) #('/Users/yanfa/PycharmProjects/hogwarts/L3', 'os_.py')

#5、拼接路径 os.path.join()
print(os.path.join('/python_programming_language/L3', 'os_.py'))

#6、判断路径是否存在 os.path.exists()
print(os.path.exists('/python_programming_language/L3')) #True

#7、判断是否是目录os.path.isdir()
print(os.path.isdir('/python_programming_language/L3'))  #True
print(os.path.isdir('/python_programming_language/L3/os_.py'))  #False

#8、判断是否是文件
print(os.path.isfile('/python_programming_language/L3/os_.py')) #True
print(os.path.isfile('/python_programming_language/L3')) #False

#9、获取文件大小,字节数
print(os.path.getsize('/python_programming_language/L3/os_.py')) #7455




