# # sku基础数据
# class SkuData():
#
#
#     def __init__(self,sku,layer_num,layer,box_num,length,width,heigth,weigth):
#         self.sku = sku
#         self.layer_num = layer_num
#         self.layer = layer
#         self.box_num = box_num
#         self.length = length
#         self.width = width
#         self.heigth = heigth
#         self.weigth = weigth
#
#
# sku11059905 = SkuData("11059905",10,6,16,36,28,21,15.5)
#
#
# # 空库位
# class EmptyLocation():
#
#     def __init__(self,empty):
#
#         self.items_list = []
#         self.empty = empty
#         self.items_list.append(self.empty)
#
#
# empty_location = EmptyLocation("2K022")
# print(empty_location.items_list)
#
#
# # 主程序
# class Sku(SkuData):
#
#     def __init__(self,sku,total):
#         # self.sku = sku
#         total_heigth = total/sku.box_num/sku.layer_num*sku.heigth
#         print(total_heigth)
#
#
# Sku = Sku("sku11059905",960)

bcdefgh_list = ["1B022","1B023","1B013","1B033","1B043","1B053","1B063","1B073","1B083"]

print(bcdefgh_list)
for i in range(len(bcdefgh_list)-1,-1,-1):
    print(bcdefgh_list[i])

    bcdefgh_list.pop(i)

print(bcdefgh_list)


