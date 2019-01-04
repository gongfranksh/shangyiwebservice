# -*- coding: utf-8 -*-
from Entity.jsEntity import JsEntity


class ProductBarCode(JsEntity):

    def __init__(self, branchcode):
        JsEntity.__init__(self, "Product_barcode", branchcode)

    def seek_product_by_barcode(self, barcode):
        sql = "select ProId, BarCode, Barmode, quantity, NormalPrice, MemberPrice, MainFlag, CreateDate, UpdateDate, Spec, Operatorid from product_barcode where barcode='{0}' "
        sql = sql.format(barcode)
        rst = self.get_remote_result_by_sql(sql)
        return rst

    def get_product_barcode_all(self):
        sql = """
            SELECT  top 100 ProId, BarCode, Barmode, quantity, NormalPrice, MemberPrice, MainFlag, CreateDate, UpdateDate, Spec, Operatorid, 
             CONVERT (int,timestamp) AS stamp
            FROM dbo.product_barcode
            """
        rst = self.get_remote_result_by_sql(sql)
        return rst
