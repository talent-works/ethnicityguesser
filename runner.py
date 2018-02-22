#! /usr/bin/env python

import sys, io, os
import pkg_resources
import dill

import NLTKMaxentEthnicityClassifier as mec
from setup import PACKAGE_NAME

def unpickle(string):
	pickle_file = open(string, 'rb')
	to_ret = dill.load(pickle_file)
	return to_ret

ETHNICITY_PKL = "pickled_classifiers/combined.dill"
def make_classifier():
	# path = pkg_resources.resource_filename(PACKAGE_NAME, ETHNICITY_PKL)
	# if not os.path.exists(path):
	all_toks = []
	basedir = pkg_resources.resource_filename(PACKAGE_NAME, "pickled_names")
	for pickle_file in os.listdir(basedir):
		all_toks.append(unpickle(os.path.join(basedir, pickle_file)))

	clf = mec.NLTKMaxentEthnicityClassifier(all_toks)
	clf.train(min_lldelta=0.500)

	# dill.dump(clf, open(path, "wb"))

	# else:
	# 	clf = unpickle(path)

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
