# from collections import Counter
# lst = [1,3,3,4,5,5,5,5,2]

# cnt_lst = Counter(lst).most_common()
# print(cnt_lst[0])
# print(dict(cnt_lst))
# max_v = 0
# for k,v in dict(cnt_lst).items():
#     if v > max_v:
#         max_v = v

# for k,v in dict(cnt_lst).items():
#     if v == max_v:
#         print(k)


import pandas as pd

# Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Math': [85, 72, 90, 65],
    'English': [78, 89, 85, 75]
}

df = pd.DataFrame(data)

# print(df[(df['Math']>80) & (df['English']>80)]['Name'])

df['Average']= (df['Math']+df['English'])/2
print(df[(df['Average']>80)]['Name'])





