#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ����Ө
���ڣ�2020.4.8
"""

import random
import math



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    if name=="ʯͷ":
        player_choice_number=0
    elif name=="ʷ����":
        player_choice_number=1
    elif name=="ֽ":
        player_choice_number=2
    elif name=="����":
        player_choice_number=3
    elif name=="����":
        player_choice_number=4
    else:
        player_choice_number=5
    return player_choice_number
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    


def number_to_name(number):
    if number==0:
        comp_choice="ʯͷ"
    elif number==1:
        comp_choice="ʷ����"
    elif number==2:
        comp_choice="ֽ"
    elif number==3:
        comp_choice="����"
    else:
        comp_choice="����"
    return comp_choice
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��




def rpsls(player_choice):
    player_choice_number=name_to_number(player_choice)
    if player_choice_number==5:
        print()
    else:
        comp_number=random.randrange(0,4)
        comp_choice=number_to_name(comp_number)
        print("�����ѡ����ǣ�"+comp_choice)
        lose1=(comp_number+4)%5
        lose2=(comp_number+3)%5
        win1=(comp_number+6)%5
        win2=(comp_number+7)%5
        if comp_number==player_choice_number:
            print("���ͼ��������һ����")
        elif player_choice_number==lose1 or player_choice_number==lose1:
            print("�����Ӯ��")
        else:
            print("��Ӯ��")
        
            
            
        
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�




# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


