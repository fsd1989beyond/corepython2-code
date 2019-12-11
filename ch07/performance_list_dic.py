# -*- coding: utf-8 -*-
# @Time    : 2019/12/8 9:32
# @Author  : PangHu
import timeit
import time

products_list = [(143121312, 100), (432314553, 30), (32421912367, 150)]
products_dic = { 143121312: 100, 432314553: 30, 32421912367: 150,}

products = [ (143121312, 100), (432314553, 30), (32421912367, 150), (937153201, 30)]


def find_product_price(products, product_id):
    for id, price in products:
        if id == product_id:
            return price
    return None



def get_element_fromList():

    #print('The price of product 432314553 is {}'.format(find_product_price(products_list, 432314553)))
    find_product_price(products_list, 432314553)

def get_element_fromDic():
    # print('The price of product 432314553 is {}'.format(products_dic[432314553]))
    products_dic[432314553]


def compare_get_element_listVsDic():
    print(timeit.timeit(stmt=get_element_fromList, number=1000000))
    print(timeit.timeit(stmt=get_element_fromDic, number=1000000))

    # 0.323653926
    # 0.15484402100000005


# --------------------- 要找出这些商品有多少种不同的价格  ----------------------------------------------------------------


# list version
def find_unique_price_using_list(prod=products):
    unique_price_list = []
    for t, price in prod:  # A
        if price not in unique_price_list: #B
            unique_price_list.append(price)
    return len(unique_price_list)



# set version
def find_unique_price_using_set(prod=products):
    unique_price_set = set()
    for t, price in prod:
        unique_price_set.add(price)
    return len(unique_price_set)

def compare_count_element_listVsDic():
    print(timeit.timeit(stmt=find_unique_price_using_set, number=1000000))
    print(timeit.timeit(stmt=find_unique_price_using_list, number=1000000))


# --------------------- 生产环境中 100,000个元素的产品分别统计产品价格数量   ------------------------------------------------
def compare_ProductEnv_listVsDic():
    id = [x for x in range(0, 100000)]
    price = [x for x in range(200000, 300000)]
    products = list(zip(id, price))

    # 计算列表版本的时间
    start_using_list = time.perf_counter()
    find_unique_price_using_list(products)
    end_using_list = time.perf_counter()
    #print("time elapse using list: {}".format(end_using_list - start_using_list))
    print(timeit.timeit(stmt=find_unique_price_using_list(products), number=1))
    # 计算集合版本的时间
    start_using_set = time.perf_counter()
    find_unique_price_using_set(products)
    end_using_set = time.perf_counter()
    #print("time elapse using set: {}".format(end_using_set - start_using_set))
    print(timeit.timeit(stmt=find_unique_price_using_set(products), number=1))


if __name__ == '__main__':
    #compare_get_element_listVsDic()
    compare_count_element_listVsDic()
    # compare_ProductEnv_listVsDic()


