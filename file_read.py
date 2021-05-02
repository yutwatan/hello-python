open_file = open('data/point.txt')
raw_data = open_file.read()
open_file.close()
print(raw_data)

# with 文を使うと close() 不要（インデントの範囲がオープンした状態になる）
with open('data/point.txt') as open_file:
    raw_data = open_file.read()
print(raw_data)
