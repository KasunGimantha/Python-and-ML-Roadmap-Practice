
def mean(lst):
    avg_list = sum(lst)/len(lst)
    return avg_list


def median(lst):

    sorted_lst = sorted(lst)

    median_lst = sorted_lst[int(len(lst)/2)]
    return median_lst


def mode(lst):
    new_dict = {}

    for item in lst:
        new_dict[item] = new_dict.get(item, 0)+1

    max_count = max(new_dict.values())

    modes = [key for key, value in new_dict.items() if value == max_count]

    return modes
