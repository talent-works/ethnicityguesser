#!/usr/bin/python

from NLTKMaxentEthnicityClassifier import NLTKMaxentEthnicityClassifier as mxec
import sys, io, os
from .setup import PACKAGE_NAME
import cPickle as pickle

def unpickle(string):
	pickle_file = open(string, 'rb')
	to_ret = pickle.load(pickle_file)
	return to_ret

ETHNICITY_PKL = "pickled_classifiers/danish_irish_chinese_czech_japanese_french_jewish_indian_spanish_italian_.pkl"
def make_classifier():
	# Can't use pkg_resources because the pickled files don't get installed for some reason. -e?
	path = os.path.join(os.environ["APP_ROOT"], "src", PACKAGE_NAME, ETHNICITY_PKL)
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
