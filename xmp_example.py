import xml.etree.ElementTree as EL

xml_data = """
<person>
    <name>John Doe</name>
    <age>30</age>
    <city>New York</city>
</person>

"""

root = EL.fromstring(xml_data)

print('Person Name: ', root.find('name').text)
print('Person Age: ', root.find('age').text)