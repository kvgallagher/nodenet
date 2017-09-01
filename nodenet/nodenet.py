from uuid import uuid4

class Nodenet:
	def __init__(self, name = None):
		self.uid = uuid4()
		self.name = name
		self.node_dict = {}
		self.layers = []
		self.links_list = []
		self.exit_node_list = None

	@property
	def name(self):
	    return self.name if self.name else self.uid

	@name.setter
	def name(self, value):
	    self.name = value

	@property
	def node_dict(self, name):
		return self.node_dict[name]

	def add_layers(self, layers):
		self.layers = layers
		[self.add_nodes(layer) for layer in layers]

	def add_nodes(self, layer):
		[self.add_node(node) for node in layer]

	def add_node(self, node):
		self.node_dict[node.name] = node

	def add_link(self, link):
		self.links_list.append(link)
