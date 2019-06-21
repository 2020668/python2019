
# 空库位
bc_list = ["2B056","2B023"]
defg_list = ["2C056","2C023"]


# sku基础数据
class SkuData():

  def __init__(self,sku,layer_num,layer,box_num,length,width,heigth,weigth):
        self.sku = sku
        self.layer_num = layer_num
        self.layer = layer
        self.box_num = box_num
        self.length = length
        self.width = width
        self.heigth = heigth
        self.weigth = weigth

# 维护基础数据
sku11059905 = SkuData("11059905",10,6,16,36,28,21,15.5)


# # 空库位
# class EmptyLocation():
#
#     def __init__(self,empty):
#
#         self.items_list = []
#         self.empty = empty
#         self.items_list.append(self.empty)
#
#         self.a_list = ["2A032","2A055"]
#         self.b_list = ["2B056","2B023"]
#
#
# empty_location = EmptyLocation("2K022")
# print(empty_location.items_list)


# 主程序
class Sku(object):

    def __init__(self,sku,total):
        self.sku = sku
        total = int(total)
        if self.sku == "11059905":

            total_heigth = total/sku11059905.box_num/sku11059905.layer_num*sku11059905.heigth
            if total_heigth <= 170:
                for i in bc_list:

                    print("货物高度%.2fcm,库位%s"% (total_heigth,i))
                    return

        else:
            print("您的输入有误")

input_sku = input("请输入SKU:")
input_total = input("请输入数量：")
Sku = Sku(input_sku,input_total)

