year_str = input('あなたの生まれ年を西暦4桁で入力してください： ')
year = int(year_str)
eto_tuple = ('子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥')

# 干支の順番（0〜11）を西暦から計算する
number_of_eto = (year + 8) % 12
print('あなたの干支は{}です。'.format(eto_tuple[number_of_eto]))
