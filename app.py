from pyriksdagen.utils import paragraph_iterator
from lxml import etree

filename = "example-data/prot-1949--ak--12.xml"
parser = etree.XMLParser(remove_blank_text=True)
root = etree.parse(filename, parser).getroot()

p_iter = paragraph_iterator(root)

for p in p_iter:
    print(p)