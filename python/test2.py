ssh.connect("124.160.108.60",60000,"root", "dahuafire")
if __name__ == '__main__':

    for host in host_lists:
        try:
            info = getServerInfo(host[0],host[1],host[2],host[3])
            a = host[0]
            b = host[1]
            c = host[2]
            d = host[4]
            print(''.join(a),''.join(b))

        except:
            pass

