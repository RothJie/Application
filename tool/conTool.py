from tool import INFO
import pymysql


class DBtool:
    @classmethod
    def __creatCon(cls):
        con = pymysql.Connect(**INFO.wordSorce())
        return con

    @classmethod
    def haveDataRe(cls, sql: str):
        connect = cls.__creatCon()
        cur = connect.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        connect.close()
        return result

    @classmethod
    def notDataRe(cls, sql: str):
        connect = cls.__creatCon()
        cur = connect.cursor()
        cur.execute(sql)
        cur.close()
        connect.close()
