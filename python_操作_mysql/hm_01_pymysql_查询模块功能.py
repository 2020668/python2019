from pymysql import connect


def main():
    # 创建connection连接
    conn = connect(
        host="192.168.43.188",
        port=3306,
        user="root",
        password="zuowei19881128",
        database="jing_dong",
        charset="utf8")

    # 获取cursor对象
    cs1 = conn.cursor()

    a = input("请输入想查询的信息：")
    if a == "商品信息":
        # 执行select语句，并返回受影响的行数：查询一条数据
        count = cs1.execute("select id,name from goods")

    if a == "型号价格":
        count = cs1.execute("select name,price from goods;")
        # 打印受影响的行数
        print("查询到%d条数据:" % count)

        for i in range(count):
            # 获取查询结果
            result = cs1.fetchone()
            # 打印查询结果
            print(result)

    # 关闭cursor对象
    # cs1.close()
    # conn.close()


if __name__ == '__main__':
    main()
