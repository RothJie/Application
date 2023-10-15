from tool import conTool
from tool import INFO

print(INFO.getSql(nsm="select", clumns="*", tableName="ws_words"))

print(INFO.getSql(nsm="select_for_words", tbl="ws_words", cols="id, word, mean", page=2, num=10))
