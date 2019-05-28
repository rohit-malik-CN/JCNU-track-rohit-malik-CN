import xml.etree.ElementTree as ET
from py2neo import Node, Relationship, Graph

tree = ET.parse('book.xml')
root = tree.getroot()

#print(root)
#print(root.tag)
#print(root[0].tag)
#print(root[0].attrib)

node_list = []
rel_list = []
visited = []
real_node_list = []


def dfs(node, temp_real_node):
    if node in visited:
        return
    else:
        visited.append(node)
        node_list.append(node)
        real_node = temp_real_node
        if real_node not in real_node_list:
            real_node_list.append(real_node)
        for key, value in node.attrib.items():
            attr_node = Node("AttributeNode", name=key, attribute_value=value)
            rele = Relationship(real_node, "ATTRIBUTE", attr_node)
            real_node_list.append(attr_node)
            rel_list.append(rele)
        for n in node:
            if n == node:
                continue
            temp_real_node = Node("TagNode", name=n.tag)
            rele = Relationship(temp_real_node, "IS_CHILD_OF", real_node)
            if rele not in rel_list:
                rel_list.append(rele)
            dfs(n, temp_real_node)
    return


root_real_node = Node("TagNode", name=root.tag)
dfs(root, root_real_node)
#print(real_node_list)
#print(rel_list)

graph = Graph("http://localhost:7474/db/data/")
for rel in rel_list:
    graph.create(rel)

