#!/usr/bin/python3

def weight_average(my_list=[]):
    if (my_list):
        tuple_sum = 0
        weight_sum = 0
        for score, weight in my_list:
            tuple_sum += (score * weight)
            weight_sum += weight

        return (tuple_sum / weight_sum)
    else:
        return 0
