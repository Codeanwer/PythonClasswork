#firstPythonwork内容：
#采用相关的字符串打印方法，打印下图的内容，整个字符串宽度为40。请独立完成该实验。输出结果如下：
#请输入表格宽度：40
#========================================
#Fruits                             Price
#----------------------------------------
# apple                                9.4
# pear                                 5.5
# tomato                               1.9
# mango                               10.5
# watermelon                           6.2
# Hami melon                           5.6
# ========================================
items_menu = {'apple': 9.4, 'pear': 5.5, 'tomato': 1.9, 'mango': 10.5, 'watermelon': 6.2, 'Hami melon': 5.6}
while True:
    forms_length = input("请输入表格宽度：")
    try:
        forms_length = int(forms_length)
        if forms_length > 0:
            break
        else:
            print("表格宽度必须是正整数，请重新输入。")
    except ValueError:
        print("表格宽度必须是正整数，请重新输入。")
print('=' * int(forms_length))
print("Fruits" + ' ' * (int(forms_length) - 11) + "Price")  # 可跟随用户要求的表格宽度进行自定义的适应性输出
print('-' * int(forms_length))
for key, value in items_menu.items():
    # 自适应输入表格宽度，-2的原因是小数点以及后一位数字占了两个字符的长度，减去即可符合格式
    print(key, ' ' * (int(forms_length) - len(str(key)) - len(str(value)) - 2), value)
print('=' * int(forms_length))
