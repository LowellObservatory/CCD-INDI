from lxml import etree

parser = etree.XMLParser(dtd_validation=True)
tree = etree.parse("examp_skel.xml", parser)
