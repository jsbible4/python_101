#

def zodiac_emoji(*years):
    dict_zod = {
        0: '🐒',
        1: '🐓',
        2: '🐕',
        3: '🐖',
        4: '🐀',
        5: '🐂',
        6: '🐅',
        7: '🐇',
        8: '🐉',
        9: '🐍',
        10: '🐎',
        11: '🐏'
    }
    return  [dict_zod[i % 12] for i in years] # 방법 1
    # for i in year:
    #     result_list.append(dict_zod[i % 12])   #방법 2

print(zodiac_emoji(1009, 2003, 2035, 4067))