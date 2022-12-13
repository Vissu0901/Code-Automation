import os
from pathlib import Path

list_xml_files = []
list_xsd_files = []
list_of_files = []
def find_the_files(path):
    files = os.listdir(path)
    for item in files:
        if os.path.isdir(os.path.join(path,item)):
            find_the_files(os.path.join(path,item))
        else:
            if item.endswith('.xsd'):
                #os.path.join(path, item)
                list_xsd_files.append(os.path.join(path,item))
    return list_xsd_files

def get_list_of_files(path,ext):
    files = os.listdir(path)
    for item in files:
        if os.path.isdir(os.path.join(path, item)):
            get_list_of_files(os.path.join(path, item), ext)
        else:
            if item.endswith(ext):
                list_of_files.append(os.path.join(path, item))
    return sorted(list(set(list_of_files)))

def get_list_of_xml_files():
    loc = Path("./Schemas")
    paths = loc.glob('*.xml')
    loc1 = ".\schemas\\"
    files = [loc1 + path.name for path in paths]
    return files

def convert_xsd_to_xml_files(schema_files_path):
    list_of_xsd_files = get_list_of_files(schema_files_path,".xsd")
    for file in list_of_xsd_files:
        with open(file,'r') as f:
            data = f.read()
        if len(str(list_of_xsd_files.index(file))) < 2:
            new_file = open(f".\Schemas\schema{str(0)}{str(list_of_xsd_files.index(file))}.xml", 'a')
        else:
            new_file = open(f".\Schemas\schema{str(list_of_xsd_files.index(file))}.xml", 'a')
        new_file.write(data)
        new_file.close()

def removefiles(xml_files):
    """This function takes one argument path, and will return True after files deleted if any else False
    if path doesn't contain any files in it"""
    # new_list = get_list_of_files(".\Schemas",".xml")
    # if len(xml) != 0:
    for file in xml_files:
        os.remove(file)

def search_for_text(text):
    list_of_result = []
    xml_files = get_list_of_xml_files()
    for file in xml_files:
        with open(file, 'r') as f:
            data = f.read()

        if text in data:
            list_of_result.append("true")
            break
        else:
            list_of_result.append("false")

    return list_of_result

