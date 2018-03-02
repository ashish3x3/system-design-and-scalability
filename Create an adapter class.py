

'''
Create an adapter class that automatically loads a two-dimensional array of objects into a dictionary as key-value pairs.

http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html
'''

from pprint import pprint

class NodeObj:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __repr__(self):
		return 'Node: %s' % id(self)

class ProxyAdaptor:
	def __init__(self, nodes):
		self.mp = {}
		r = len(nodes)
		c = len(nodes[0])

		for x in range(r):
			for y in range(c):
				self.mp[nodes[x][y].x] = nodes[x][y].y

	def __repr__(self):
		for x, y in self.mp.iteritems():
			# print '{} => {}'.format(x, y)
			return '<%s : %s>' % (self.__class__.__name__ ,repr(self.mp))

class Test:
	def __init__(self):
		self.nodes = [[NodeObj(i,j) for j in range(4)] for i in range(4)]
		pprint(self.nodes) # what i have
		adaptor = ProxyAdaptor(self.nodes)
		print adaptor # what I want

	def callAdaptor(self):
		adaptor = ProxyAdaptor(self.nodes)
		print adaptor



t = Test()
# t.callAdaptor()



'''
[[Node: 88132168, Node: 88175432, Node: 88175496, Node: 88175560],
 [Node: 88175624, Node: 88175688, Node: 88175752, Node: 88175816],
 [Node: 88175880, Node: 88175944, Node: 88176008, Node: 88176072],
 [Node: 88176136, Node: 88176200, Node: 88176264, Node: 88176328]]
<ProxyAdaptor : {0: 3, 1: 3, 2: 3, 3: 3}>

'''







