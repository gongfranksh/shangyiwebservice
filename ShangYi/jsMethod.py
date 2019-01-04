from spyne import ServiceBase, Unicode, rpc, String, Iterable

from Entity.Branch import Branch
from Entity.ProductBarCode import ProductBarCode


class JsService(ServiceBase):
    @rpc(Unicode,_returns=String)
    def get_branch_result(self,braid):
        branch=Branch(braid)
        rst = branch.get_remote_table_result_all()
        return  rst

    @rpc(Unicode,_returns=String)
    def get_productbarcode_by_barcode_result(self,barcode):
        productbarcode=ProductBarCode(barcode)
        rst=productbarcode.seek_product_by_barcode(barcode)
        return  rst

    @rpc(Unicode,_returns=String)
    def get_productbarcode_all(self,barcode):
        productbarcode=ProductBarCode(barcode)
        rst=productbarcode.get_product_barcode_all();
        return  rst
