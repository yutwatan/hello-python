point_list = [75, 80, 91]
total = 0

for point in point_list:
    total += point

average = total / len(point_list)
print('合計点は{}、平均点は{}です。'.format(total, average))
