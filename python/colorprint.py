#/usr/bin/python
#-*- coding: utf-8 -*-


#   ��ʽ��\033[��ʾ��ʽ;ǰ��ɫ;����ɫm
#   ˵��:
#
#   ǰ��ɫ            ����ɫ            ��ɫ
#   ---------------------------------------
#     30                40              ��ɫ
#     31                41              ��ɫ
#     32                42              ��ɫ
#     33                43              �Sɫ
#     34                44              ��ɫ
#     35                45              �Ϻ�ɫ
#     36                46              ����ɫ
#     37                47              ��ɫ
#
#   ��ʾ��ʽ           ����
#   -------------------------
#      0           �ն�Ĭ������
#      1             ������ʾ
#      4            ʹ���»���
#      5              ��˸
#      7             ������ʾ
#      8              ���ɼ�
#
#   ���ӣ�
#   \033[1;31;40m    <!--1-������ʾ 31-ǰ��ɫ��ɫ  40-����ɫ��ɫ-->
#   \033[0m          <!--�����ն�Ĭ�����ã���ȡ����ɫ����-->]]]


STYLE = {
        'fore':
        {   # ǰ��ɫ
            'black'    : 30,   #  ��ɫ
            'red'      : 31,   #  ��ɫ
            'green'    : 32,   #  ��ɫ
            'yellow'   : 33,   #  ��ɫ
            'blue'     : 34,   #  ��ɫ
            'purple'   : 35,   #  �Ϻ�ɫ
            'cyan'     : 36,   #  ����ɫ
            'white'    : 37,   #  ��ɫ
        },

        'back' :
        {   # ����
            'black'     : 40,  #  ��ɫ
            'red'       : 41,  #  ��ɫ
            'green'     : 42,  #  ��ɫ
            'yellow'    : 43,  #  ��ɫ
            'blue'      : 44,  #  ��ɫ
            'purple'    : 45,  #  �Ϻ�ɫ
            'cyan'      : 46,  #  ����ɫ
            'white'     : 47,  #  ��ɫ
        },

        'mode' :
        {   # ��ʾģʽ
            'mormal'    : 0,   #  �ն�Ĭ������
            'bold'      : 1,   #  ������ʾ
            'underline' : 4,   #  ʹ���»���
            'blink'     : 5,   #  ��˸
            'invert'    : 7,   #  ������ʾ
            'hide'      : 8,   #  ���ɼ�
        },

        'default' :
        {
            'end' : 0,
        },
}


def UseStyle(string, mode = '', fore = '', back = ''):

    mode  = '%s' % STYLE['mode'][mode] if STYLE['mode'].has_key(mode) else ''

    fore  = '%s' % STYLE['fore'][fore] if STYLE['fore'].has_key(fore) else ''

    back  = '%s' % STYLE['back'][back] if STYLE['back'].has_key(back) else ''

    style = ';'.join([s for s in [mode, fore, back] if s])

    style = '\033[%sm' % style if style else ''

    end   = '\033[%sm' % STYLE['default']['end'] if style else ''

    return '%s%s%s' % (style, string, end)



def TestColor( ):

    print UseStyle('������ʾ')
    print ''

    print "������ʾģʽ"
    print UseStyle('����',   mode = 'bold'),
    print UseStyle('�»���', mode = 'underline'),
    print UseStyle('��˸',   mode = 'blink'),
    print UseStyle('����',   mode = 'invert'),
    print UseStyle('���ɼ�', mode = 'hide')
    print ''


    print "����ǰ��ɫ"
    print UseStyle('��ɫ',   fore = 'black'),
    print UseStyle('��ɫ',   fore = 'red'),
    print UseStyle('��ɫ',   fore = 'green'),
    print UseStyle('��ɫ',   fore = 'yellow'),
    print UseStyle('��ɫ',   fore = 'blue'),
    print UseStyle('�Ϻ�ɫ', fore = 'purple'),
    print UseStyle('����ɫ', fore = 'cyan'),
    print UseStyle('��ɫ',   fore = 'white')
    print ''


    print "���Ա���ɫ"
    print UseStyle('��ɫ',   back = 'black'),
    print UseStyle('��ɫ',   back = 'red'),
    print UseStyle('��ɫ',   back = 'green'),
    print UseStyle('��ɫ',   back = 'yellow'),
    print UseStyle('��ɫ',   back = 'blue'),
    print UseStyle('�Ϻ�ɫ', back = 'purple'),
    print UseStyle('����ɫ', back = 'cyan'),
    print UseStyle('��ɫ',   back = 'white')
    print ''
if __name__ == '__main__':

    TestColor( )