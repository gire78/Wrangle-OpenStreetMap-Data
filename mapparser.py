#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the 
tag name as the key and number of times this tag can be encountered in 
the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict

OSM_FILE = 'mapRH.osm'
OSMFILE = 'sample.osm'

def count_tags(filename):
        count = defaultdict(int)
        for event, node in ET.iterparse(filename):
            if event == 'end':
                count[node.tag] += 1
            node.clear()
        return count
    

if __name__ == "__main__":
    ct = count_tags(sample.osm)
    pprint.pprint(ct)

def test():

    tags = count_tags('sample.osm')
    pprint.pprint(tags)
    assert tags == {'bounds': 1,
                     'member': 3,
                     'nd': 4,
                     'node': 20,
                     'osm': 1,
                     'relation': 1,
                     'tag': 7,
                     'way': 1}

    

if __name__ == "__main__":
