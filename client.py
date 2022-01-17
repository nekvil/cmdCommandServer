import socket
import manager as m


def command(n):
    if n.isspace() or n == "":
        return
    elif n == "ls":
        m.ls()
        return
    elif "pwd" in n:
        m.pwd()
        return
    elif n == "help":
        m.help_()
        return
    elif "mkdir" in n:
        if len(n.split()) != 2:
            print("\033[31m" + 'Usage: crdir [dir_name]' + '\033[0m')
        else:
            m.mkdir(n.split()[1])
        return
    elif "rmdir" in n:
        if len(n.split()) != 2:
            print("\033[31m" + 'Usage: dldir [dir_name]' + '\033[0m')
        else:
            m.rmdir(n.split()[1])
        return
    elif "rm" in n:
        if len(n.split()) != 2:
            print("\033[31m" + 'Usage: dl [file_name]' + '\033[0m')
        else:
            m.rm(n.split()[1])
        return
    elif "cd" in n:
        if len(n.split()) == 1:
            m.cd("..")
        elif len(n.split()) > 2:
            print("\033[31m" + 'Usage: cd [dir_name]' + '\033[0m')
        else:
            m.cd(n.split()[1])
        return
    elif "touch" in n:
        if len(n.split()) != 2:
            print("\033[31m" + 'Usage: create [file_name]' + '\033[0m')
        else:
            m.touch(n.split()[1])
        return
    elif "cat" in n:
        if len(n.split()) != 2:
            print("\033[31m" + 'Usage: read [file_name]' + '\033[0m')
        else:
            m.cat(n.split()[1])
        return
    elif "write" in n:
        if len(n.split()) <= 2:
            print("\033[31m" + 'Usage: write [file_name][info]' + '\033[0m')
        else:
            m.write(n.split()[1], ' '.join(n.split()[2:]))
        return
    elif "rename" in n:
        if len(n.split()) != 3:
            print("\033[31m" + 'Usage: rnm [file_name][new_file_name]' + '\033[0m')
        else:
            m.rename(n.split()[1], n.split()[2])
        return
    elif "replace" in n:
        if len(n.split()) != 3:
            print("\033[31m" + 'Usage: rpl [file_name][dir_name]' + '\033[0m')
        else:
            m.replace(n.split()[1], n.split()[2])
        return
    elif "cp" in n:
        if len(n.split()) != 3:
            print("\033[31m" + 'Usage: copy [file_name][dir_name]' + '\033[0m')
        else:
            m.cp(n.split()[1], n.split()[2])
        return
    else:
        print("\033[31m" + ('ERROR_1: unknown command ' + "\""+str(n)+"\"."+'Try help') + '\033[0m')


sock = socket.socket()
sock.connect(('localhost', 9090))
BUFFER_SIZE = 1024
CMD = ["ls", "pwd", "help", "mkdir", "rmdir", "rm", "cd", "touch", "cat", "write", "rename", "replace", "cp"]
m.start()

while True:
    msg = input("-> ")
    sock.send(msg.encode())
    msg = sock.recv(BUFFER_SIZE).decode("utf8")
    if msg == "exit":
        sock.close()
        break
    print(msg.split()[0])
    if msg.split()[0] in CMD:
        command(msg)
    else:
        print("[ОТВЕТ СЕРВЕРА]: "+msg)

exit()

