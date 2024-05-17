import xml.etree.ElementTree as ET


tree = ET.parse("../files_for_parsing/example.xml")

root = tree.getroot()

# print(root)

# for index, child in enumerate(root):
#     print(f'Index: {index}')
#     print(child.text.strip())
#     print(child.tag.strip())

magazine_with_id_2 = root.findall(".//magazine/issue[1]")


# magazine_with_id_2 = root.findall(".//*[@id='1']/issue")
print([obj.text for obj in magazine_with_id_2])