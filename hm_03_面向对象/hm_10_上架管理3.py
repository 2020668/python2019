
# 空库位
bcdefgh_list = ["1B022","1B053","1B013","1B033"]
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
        total = int(total)
        if self.sku == "11059905":

            total_heigth = total/sku11059905.box_num/sku11059905.layer_num*sku11059905.heigth
            t_num = sku11059905.layer_num*sku11059905.layer*sku11059905.box_num
            t_height = sku11059905.layer*sku11059905.heigth

            if total_heigth > t_height:

                for i in bcdefgh_list:

                    print("数量%d,请入库位%s"% (t_num,i))
                    bcdefgh_list.remove(i)
                    total_heigth -= t_height
                    total -= t_num
                    if total_heigth <= 80:
                        for r in mnpq_list:

                            print("数量%d,请入库位%s"% (total,r))
                            mnpq_list.remove(r)
                            return

            else:
                for x in mnpq_list:
                    print("数量%d,请入库位%s" % (total, x))
                    mnpq_list.remove(x)
                    return


input_sku = input("请输入SKU:")
input_total = input("请输入数量：")
Sku = Sku(input_sku,input_total)
