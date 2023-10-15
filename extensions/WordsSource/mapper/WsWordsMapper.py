from tool import INFO, DBtool
from ..entity import TWsWords


class WsWordsMapper(DBtool):
    tbl = "ws_words"

    @classmethod
    def insertRecord(cls, *args) -> bool:
        """TODO:对参数进行安全验证"""
        flag = False
        try:
            cls.openExcute(one="21fgds", laguage=INFO.getSql(nsm="ws_words_insert",
                                                             clumns="{},{},{}".format(*args),
                                                             tableName=cls.tbl))
            flag = True
        except Exception as e:
            print(e)
        return flag

    @classmethod
    def selectList(cls) -> list:
        """查询"""
        res = cls.openExcute(one_result="fdsaf",
                             laguage=INFO.getSql(nsm="select_for_words_page",
                                                 cols="id,word,mean",
                                                 tbl=cls.tbl, page="0",
                                                 num="20"))
        t_li = []
        for uni in res:
            t_li.append(TWsWords(uni[0], uni[1], uni[2]))
        return t_li
