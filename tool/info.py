import xml.etree.ElementTree as ET


class INFO:
    __info_path = "./files/app_info.xml"
    __xml_root = None

    @classmethod
    def __XML_root(cls):
        # 解析XML文件并返回ElementTree对象
        tree = ET.parse(cls.__info_path)
        # 得到文档元素对象
        cls.__xml_root = tree

    @classmethod
    def __app_info_ele(cls):
        cls.__XML_root()
        return cls.__xml_root.find("root_app_info")

    @classmethod
    def app_info(cls):
        title = cls.__app_info_ele().find("title").text
        width = cls.__app_info_ele().find("width").text
        height = cls.__app_info_ele().find("height").text
        return title, int(width), int(height)
