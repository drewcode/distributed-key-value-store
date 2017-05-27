from kazoo.client import KazooClient

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

#insert command to check if that node exists
data, stat = zk.get("/testing/node1")	#gets it
print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

zk.stop()