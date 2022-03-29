import os

ROOT = os.path.dirname(__file__)
data_path = os.path.join(ROOT, 'some_data')

result = {0: 0, 10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0}
keys = [0, 10, 100, 1000, 10000, 100000, 1000000]
for root, dirs, files in os.walk(data_path):
    for _file in files:
        sz = os.stat(os.path.join(root, _file)).st_size
        if sz == 0:
            result[0] += 1
            continue
        for ind, key in enumerate(keys):
            if ind == len(keys) - 1:
                print(f"A very big file {_file}")
                break
            if key < sz <= keys[ind + 1]:
                result[keys[ind + 1]] += 1
                break
print(result)
