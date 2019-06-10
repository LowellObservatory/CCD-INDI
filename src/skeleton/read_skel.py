from lxml import etree

# All we do is parse the XML skeleton file to see if the DTD/XML is working.

parser = etree.XMLParser(dtd_validation=True)
tree = etree.parse("examp_skel.xml", parser)
