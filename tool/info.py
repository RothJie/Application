import xml.etree.ElementTree as ET
import re


class INFO:
    __info_path = "./files/app_info.xml"
    __xml_root = None
    __special_chr = {">": ";MT;", "<": ";LT;"}

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
    def __db_info_ele(cls):
        cls.__XML_root()
        return cls.__xml_root.find("wordsSourceDB")

    @classmethod
    def app_info(cls):
        title = cls.__app_info_ele().find("title").text
        width = cls.__app_info_ele().find("width").text
        height = cls.__app_info_ele().find("height").text
        return title, int(width), int(height)

    @classmethod
    def wordSorce(cls):
        user = cls.__db_info_ele().find("user").text
        host = cls.__db_info_ele().find("host").text
        password = cls.__db_info_ele().find("password").text
        port = cls.__db_info_ele().find("port").text
        db = cls.__db_info_ele().find("dbName").text
        return {"user": user, "host": host, "password": password, "port": int(port), "db": db}

    @classmethod
    def __sql(cls, nsm: str):
        cls.__XML_root()
        return cls.__xml_root.find("sql").find(nsm).text.strip()

    @classmethod
    def getSql(cls, nsm: str, **kwargs):
        __s = cls.__sql(nsm)
        for spc in cls.__special_chr:
            __s = __s.replace(cls.__special_chr[spc], spc)
        module_one = re.compile("\$\$(?P<feild>.*?)\$\$.*?", re.S)
        fields = module_one.findall(__s)
        for uni in fields:
            __s = __s.replace(f"$${uni}$$", "{}".format(kwargs[uni]))
        return __s
