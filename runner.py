#! /usr/bin/env python

import sys, io, os
import pkg_resources
import cPickle as pickle

from NLTKMaxentEthnicityClassifier import NLTKMaxentEthnicityClassifier as mxec
from setup import PACKAGE_NAME

def unpickle(string):
	pickle_file = open(string, 'rb')
	to_ret = pickle.load(pickle_file)
	return to_ret

ETHNICITY_PKL = "pickled_classifiers/combined.pkl"
def make_classifier():
	path = pkg_resources.resource_filename(PACKAGE_NAME, ETHNICITY_PKL)
	if not os.path.exists(path):
		all_toks = []
		for pickle_file in os.listdir("pickled_names"):
			all_toks.append(unpickle('pickled_names/' + pickle_file))
		clf = mxec(all_toks)
		clf.train()

		pickle.dump(clf, open(path, "wb"))

	else:
		clf = unpickle(path)

	return clf

def main():
	classifier = make_classifier()
	print classifier
	while (True):
		name = raw_input("Enter a name (enter to quit) -->: ")
		if name == "":
			break
		print classifier.classify(name)

if __name__ == "__main__":
	main()
