from pyriksdagen.utils import paragraph_iterator
from pyriksdagen.utils import speeches_with_name
from pyriksdagen.utils import parlaclarin_to_txt
from lxml import etree

filename = "example-data/prot-1949--ak--12.xml"
parser = etree.XMLParser(remove_blank_text=True)
root = etree.parse(filename, parser).getroot()

p_iter = paragraph_iterator(root)
p_iter = speeches_with_name(root)

#for p in p_iter:
#    print(p)

filename = "example-data/prot-1949--ak--12.txt"
txt = parlaclarin_to_txt(root)
f = open(filename, "w")
for line in txt.split("\n"):
    f.write(line.strip() + "\n")
f.close()