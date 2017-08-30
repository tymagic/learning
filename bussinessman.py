#1。进入看到所有的商品情况
#2。输入商品和价格补充。
#4。修改商品价格

import os
import pickle

filename = '/Users/dengtianyuan/PycharmProjects/untitled1/product.pkl'




def add_goods():
    while True:

        add_choice = input('input Y/N to add goods in your shop\n')
        if add_choice.upper() == 'Y':
            #xfile.close()
            # 先判断有没有这个值，r打开，判断无则继续 close。w打开。
            xfile = open(filename, 'wb')
            product_price = []

            name_product = input('product name')
            price_product = input('product price')
            product_price.append((name_product,price_product))

            pickle.dump(product_price, xfile)
            xfile.close()
        elif add_choice.upper() == 'N':
            xfile.close()
            print('quit')
            exit()
        else:
            xfile.close()
            print('valid input')
            exit()

def add_goods_countinue():
    while True:

        add_choice = input('input Y/N to add goods in your shop\n')
        if add_choice.upper() == 'Y':
            ffile = open(filename, 'rb')
            product_price = pickle.load(ffile)
            ffile.close()
            #xfile.close()
            print(product_price)
            # 先判断有没有这个值，r打开，判断无则继续 close。w打开。
            xfile = open(filename, 'wb')


            name_product = input('product name')
            price_product = input('product price')
            product_price.append((name_product,price_product))

            pickle.dump(product_price, xfile)
            xfile.close()
        elif add_choice.upper() == 'N':
            xfile.close()
            print('quit')
            exit()
        else:
            xfile.close()
            print('valid input')
            exit()


def bussinessman():

    if not os.path.exists(filename):
        print('mkdir product')
        file = open(filename,'wb')
        file.close()
    else:
        try:

            xfile = open(filename,'rb')
            print(pickle.load(xfile))
        except EOFError:
            print('empty value')
            add_goods()
            exit()
        else:
            add_goods_countinue()


    # with open(filename,'rb  ') as xfile:
    #     try:
    #         return pickle.load(xfile)
    #     except EOFError:
    #         print('empty value')
    #         add_choice = input('Y/N to add goods in your shop')
    #         if upper(add_choice) = 'Y':Y



bussinessman()