def missing_number(num_list):
    return sum(range(num_list[0],num_list[-1]+1)) - sum(num_list)
