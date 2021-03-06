""" 
Parses and unpacks datasets for feeding into network. 
join_sets() scrambles two separate datasets into a single combined set.
"""

import numpy as np

from file_parsers import MNIST_fp, MNIST_micropsi_fp, math_ops_fp

def parse_data(data_type, run_type):
	if data_type == "MNIST":
		return MNIST_fp.read(run_type)
	elif data_type == "math_ops":
		return math_ops_fp.read(run_type)
	else:
		raise ValueError("%s is not a recognized data type", data_type)

def unpack_data(*data):
	MNIST_data = data[0]
	math_ops_data = data[1]

	MNIST_images = MNIST_data["images"]
	MNIST_labels = MNIST_data["labels"]
	MNIST = zip(MNIST_images, MNIST_labels)

	math_ops_images = math_ops_data["images"]
	math_ops_labels = math_ops_data["labels"]
	math_ops = zip(math_ops_images, math_ops_labels)

	combined_set = join_sets(MNIST, math_ops)

	images = combined_set[0]
	labels = combined_set[1]

	return images, labels

def join_sets(MNIST, math_ops):

	# combine MNIST data set with math operation symbols

	combined_zip = np.append(MNIST, math_ops, axis=0)

	np.random.shuffle(combined_zip)

	combined_images = [image for image, label in combined_zip]
	combined_labels = [label for image, label in combined_zip]

	return combined_images, combined_labels
