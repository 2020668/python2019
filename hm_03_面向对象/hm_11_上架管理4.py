
# 空库位
bcdefgh_list = ["1B022","1B023","1B013","1B033","1B043","1B053","1B063","1B073","1B083"]
mnpq_list = ["1M053","1Q023"]


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
sku11039131 = SkuData("11039131",9,3,1,23.5,18,25,5.5)


# 主程序
class Sku(object):

    def __init__(self,sku,total):
        self.sku = sku
        if self.sku == "11059905":

            total_heigth = total/sku11059905.box_num/sku11059905.layer_num*sku11059905.heigth
            t_num = sku11059905.layer_num*sku11059905.layer*sku11059905.box_num
            t_height = sku11059905.layer*sku11059905.heigth

        if self.sku == "11039131":

            total_heigth = total/sku11039131.box_num/sku11039131.layer_num*sku11039131.heigth
            t_num = sku11039131.layer_num*sku11039131.layer*sku11039131.box_num
            t_height = sku11039131.layer*sku11039131.heigth

        if total_heigth > 80:

            for i in range(len(bcdefgh_list)-1,-1,-1):

                print("数量%d,请入库位%s"% (t_num,bcdefgh_list[i]))
                bcdefgh_list.pop(i)
                # print(bcdefgh_list)

                total_heigth -= t_height
                total -= t_num

                if total_heigth <= 80:
                    for r in range(len(mnpq_list)-1,-1,-1):

                        print("数量%d,请入库位%s" % (total, mnpq_list[r]))
                        mnpq_list.pop(r)

                        return

        else:

            for r in range(len(mnpq_list)-1,-1,-1):

                print("数量%d,请入库位%s"% (total,mnpq_list[r]))
                mnpq_list.pop(r)
                return


input_sku = input("请输入SKU:")
input_total = int(input("请输入数量："))
Sku = Sku(input_sku,input_total)
