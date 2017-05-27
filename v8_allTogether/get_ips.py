from kazoo.client import KazooClient

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()


count, stat1 = zk.get("/testing/count")
master , stat2 = zk.get("/testing/master") 
node1 , stat3 = zk.get("/testing/node1")
node2 ,stat4 = zk.get("/testing/node2")
node3 ,stat4 = zk.get("/testing/node3")

#ALL_VALS HAS (count masterIP node1IP node2IP node3IP)
ALL_VALS = str(count)+" "+str(master)+" "+str(node1)+" "+str(node2)+" "+str(node3)
print ALL_VALS

zk.stop()


