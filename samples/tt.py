# -*- coding: utf-8 -*-
sql = """
      SELECT * FROM {0};
      """

sql=sql.format(123)
print sql
print("网站名：{name}, 地址 {url}".format(name="1111", url="www.runoob.com"))