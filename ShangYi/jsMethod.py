
# -*- coding: utf-8 -*-
from spyne import ServiceBase, Unicode, rpc, String, Iterable, Mandatory

from Entity.Branch import Branch
from Entity.ProductBarCode import ProductBarCode
from Entity.SystemFunction import SystemFunction


class JsService(ServiceBase):

    @rpc(Unicode,_returns=String)
    def get_branch_result(self,braid):
        branch=Branch(braid)
        rst = branch.get_remote_table_result_all()
        return  rst

    @rpc(Unicode,Unicode,_returns=String)
    def get_product_by_barcode(self,branchcode,barcode):
        productbarcode=ProductBarCode(branchcode)
        rst=productbarcode.seek_branch_product_barcode(barcode)
        #barcode查询步到，使用prodid查询
        if len(rst)==2:
            rst=productbarcode.seek_branch_product_proid(barcode)
        return  rst

    @rpc(Unicode,Unicode, _returns=String)
    def get_product_by_proname(self, branchcode, proname):
        productbarcode = ProductBarCode(branchcode)
        rst = productbarcode.seek_branch_product_name(proname)
        return rst


    @rpc(Unicode,_returns=String)
    def get_functionmenu_all(self,branchcode):
        fun_menu = SystemFunction(branchcode)
        rst=fun_menu.get_section_function_json()
        return  rst

