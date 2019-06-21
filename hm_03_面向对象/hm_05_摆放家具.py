# 家具类
class HouseItems:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):

        return "[%s]占地%.2f平米" % (self.name, self.area)


# 房子类
class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return "户型是%s\n总面积%.2f平米[剩余面积%.2f平米]\n家具%s" % \
               (self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self, item):

        print("要添加%s" % item)
        if item.area > self.free_area:
            print("%s的家具太大了，家里放不下" % item.name)

            return
        self.item_list.append(item.name)
        self.free_area -= item.area


# 主程序
bed = HouseItems("席梦思",40)
chest = HouseItems("衣柜",2)
table = HouseItems("餐桌",10)
my_house = House("三室两厅",130)

my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)

print(my_house)



