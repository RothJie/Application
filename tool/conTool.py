from tool import INFO
import pymysql


class DBtool:
    @classmethod
    def __creatCon(cls):
        con = pymysql.Connect(**INFO.wordSorce())
        return con

    @classmethod
    def __haveDataRe(cls, sql: str) -> tuple:
        connect = cls.__creatCon()
        cur = connect.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        connect.close()
        return result

    @classmethod
    def __notDataRe(cls, sql: str) -> None:
        connect = cls.__creatCon()
        cur = connect.cursor()
        cur.execute(sql)
        cur.close()
        connect.close()

    @classmethod
    def __excuteManyRe(cls, sql_li: list) -> list:
        connect = cls.__creatCon()
        cur = connect.cursor()
        result = []
        for sql in sql_li:
            cur.execute(sql)
            result.append(cur.fetchall())
        cur.close()
        connect.close()
        return result

    @classmethod
    def __excuteMany(cls, sql_li: list) -> None:
        connect = cls.__creatCon()
        cur = connect.cursor()
        for sql in sql_li:
            cur.execute(sql)
        cur.close()
        connect.close()

    @classmethod
    def openExcute(cls, **kwargs) -> tuple or list or None:
        res = None
        if "one_result" in kwargs:
            res = cls.__haveDataRe(kwargs["laguage"])
        if "one" in kwargs:
            cls.__notDataRe(kwargs["laguage"])
        if "many_result" in kwargs:
            res = cls.__excuteManyRe(kwargs["laguage"])
        if "many" in kwargs:
            cls.__excuteMany(kwargs["laguage"])
        return res
