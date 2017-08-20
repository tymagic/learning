product_list = [('Iphone',5800),('Mac pro',9000)]
shopping_list = []


salary = input('input your salary:')

if salary.isdigit():
  salary = int(salary)
  while True:
      for index,i in enumerate(product_list):
              print(index, '商品:', i[0], '单价', i[1])
      user_choice = input('Please the product you want:')
      if user_choice.isdigit():
          user_choice = int(user_choice)
          if user_choice < len(product_list) and user_choice >=0:
            p_item = product_list[user_choice]
            if p_item[1] <= salary:
              shopping_list.append(p_item)
              salary -= p_item[1]
              print('added %s into shopping cart,your current balance is \033[31;1m%s\033[0m' % (p_item,salary))


            else:
              print('\033[41;myou don`t have so much mony by it,current balance is %s\033[0m' % salary)
          else:
              print('product code %s is not exits!' % user_choice)


      elif user_choice == 'q':
          print("-------------shopping----------------")
          for p  in shopping_list:
              print(p)
          print('Your current balance:',salary)
          exit()
      else:
          print('invalid option')