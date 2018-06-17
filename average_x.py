sample_list = [2, 10, 3, 5]
avg_num = 0

for x in sample_list:
    avg_num = x + avg_num

print('sample_list is', sample_list)
print('Average of sample_list is', int(avg_num / len(sample_list)))

