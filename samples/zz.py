import datetime
import json
from decimal import Decimal

import flask as flask


class DataEncoder(json.JSONEncoder):
    def default(self, obj):

        if isinstance(obj, Decimal):
            return float(obj)

        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        return super(DataEncoder, self).default(obj)


{u'Operatorid': None, u'timestamp': '\x00\x00\x00\x00\x00\x1a\xa0\xfd', u'MemberPrice': None,
 u'BarCode': u' 753759197766', u'MainFlag': u'1', u'Barmode': u'0',
 u'UpdateDate': datetime.datetime(2017, 11, 15, 11, 34, 10, 400000), u'ProId': u'2000000235608',
 u'CreateDate': datetime.datetime(2017, 11, 15, 11, 34, 10, 400000), u'quantity': Decimal('1.000'),
 u'Spec': u'vivosport  \u667a\u80fd\u5fc3\u7387', u'NormalPrice': Decimal('1299.00')}

# json_1 = {u'SizeCode': u' ', u'BraSName': u'\u5e7f\u5dde\u5e97', u'DmCostFlag': u'0', u'VehicleNum': None,
#           u'EmpCount': None, u'Mprice_quotiety': Decimal('1.00'), u'Master': None, u'Flag2': None, u'Flag1': None}

#
# json_1 = {u'SizeCode': u' ', u'BraSName': u'\u5e7f\u5dde\u5e97', u'DmCostFlag': u'0', u'VehicleNum': None,
#           u'EmpCount': None, u'usedate': datetime.datetime(2015, 10, 10, 0, 0), u'Master': None, u'Flag2': None, u'Flag1': None,
#           u'Mprice_quotiety': Decimal('1.00')
#           }

# json_1 = {u'SizeCode': u' ', u'BraSName': u'\u5e7f\u5dde\u5e97', u'DmCostFlag': u'0', u'VehicleNum': None,
#           u'EmpCount': None, u'Mprice_quotiety': Decimal('1.00'), u'Master': None, u'Flag2': None, u'Flag1': None,
#           u'DistId': None, u'usedate': datetime.datetime(2015, 10, 10, 0, 0), u'BraId': u'01001'}

json_3 = {u'Operatorid': None, u'MemberPrice': None,
          u'BarCode': u' 753759197766', u'MainFlag': u'1', u'Barmode': u'0',
          u'UpdateDate': datetime.datetime(2017, 11, 15, 11, 34, 10, 400000), u'ProId': u'2000000235608',
          u'CreateDate': datetime.datetime(2017, 11, 15, 11, 34, 10, 400000), u'quantity': Decimal('1.000'),
          u'Spec': u'\u667a\u80fd\u5fc3\u7387', u'NormalPrice': Decimal('1299.00')}

# json_1 = {u'SizeCode': u' ', u'BraSName': u'\u5e7f\u5dde\u5e97', u'DmCostFlag': u'0', u'VehicleNum': None,
#           u'EmpCount': None, u'Mprice_quotiety': Decimal('1.00'), u'Master': None, u'Flag2': None, u'Flag1': None,
#           u'DistId': None, u'usedate': datetime.datetime(2015, 10, 10, 0, 0), u'BraId': u'01001',
#           u'Addr': u'\u6536\u8d27\u4eba\uff1a\u4e50\u4e4b\u4ed3\u5e93  \u7535\u8bdd\uff1a13392463952  \u6536\u8d27\u5730\u5740\uff1a\u5e7f\u5dde\u5e02\u5929\u6cb3\u8def590\u53f7\u6b66\u8b66\u5c0f\u533a16\u680bA\u5ea7301',
#           u'Status': u'0', u'Fax': None, u'showprofit': u'1', u'showreceiptamt': u'0', u'HqId': u'01',
#           u'serialno1': u'gEBoWg76hHrQI6x!QsIcQgEtOMcBit0axzmZb6Kvih4', u'PosNum': 6,
#           u'serialno': u'bEsFwx9nyHrQI6x!QsIcQgEtOMcBit0axzmZb6Kvih4',
#           u'CreateDate': datetime.datetime(2015, 10, 8, 17, 46, 19, 480000), u'BraType': u'0', u'showorderprice': u'0',
#           u'Square': Decimal('1500.00'), u'AlloPeroid': None, u'BraName': u'\u4e50\u4e4b\u5e7f\u5dde\u5e97',
#           u'Tel': u'020-22001356', u'IsOpen': u'1', u'Whid': None, u'ZipCode': u'510630', u'cstore': None,
#           u'AlloDiscount': None, u'AlloPriority': None, u'OpenDate': datetime.datetime(2015, 12, 1, 0, 0),
#           u'Sprice_quotiety': Decimal('1.00'), u'UpdateDate': datetime.datetime(2018, 8, 22, 9, 50, 49, 837000)}
#
# json_2 = {u'SizeCode': u' ', u'BraSName': u'\u5e7f\u5dde\u5e97', u'DmCostFlag': u'0', u'VehicleNum': None,
#           u'EmpCount': None, u'Mprice_quotiety': Decimal('1.00'), u'Master': None, u'Flag2': None, u'Flag1': None,
#           u'DistId': None, u'usedate': datetime.datetime(2015, 10, 10, 0, 0), u'BraId': u'01001',
#           u'Addr': u'\u6536\u8d27\u4eba\uff1a\u4e50\u4e4b\u4ed3\u5e93  \u7535\u8bdd\uff1a13392463952  \u6536\u8d27\u5730\u5740\uff1a\u5e7f\u5dde\u5e02\u5929\u6cb3\u8def590\u53f7\u6b66\u8b66\u5c0f\u533a16\u680bA\u5ea7301',
#           u'Status': u'0', u'Fax': None, u'showprofit': u'1', u'showreceiptamt': u'0', u'HqId': u'01',
#           u'serialno1': u'gEBoWg76hHrQI6x!QsIcQgEtOMcBit0axzmZb6Kvih4', u'PosNum': 6,
#           u'serialno': u'bEsFwx9nyHrQI6x!QsIcQgEtOMcBit0axzmZb6Kvih4',
#           u'CreateDate': datetime.datetime(2015, 10, 8, 17, 46, 19, 480000), u'BraType': u'0', u'showorderprice': u'0',
#           u'Square': Decimal('1500.00'), u'AlloPeroid': None, u'BraName': u'\u4e50\u4e4b\u5e7f\u5dde\u5e97',
#           u'Tel': u'020-22001356', u'IsOpen': u'1', u'Whid': None, u'ZipCode': u'510630', u'cstore': None,
#           u'AlloDiscount': None, u'AlloPriority': None, u'OpenDate': datetime.datetime(2015, 12, 1, 0, 0),
#           u'Sprice_quotiety': Decimal('1.00'), u'UpdateDate': datetime.datetime(2018, 8, 22, 9, 50, 49, 837000)}

rst = []
# rst.append(json_1)
# rst.append(json_2)
rst.append(json_3)

print '-' * 40
p = json.dumps(rst, cls=DataEncoder)
print p
