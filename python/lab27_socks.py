'''
Lab 27 - Socks
Marcel Schaeffer
10/19/17
'''

#import modules
import random
from collections import _count_elements

#random sock style function
def rand_sock(n):
    sock_style = ['ankle', 'crew', 'calf', 'thigh']
    sock_list = []
    i = 0
    while i < n:
        socks = random.choice(sock_style)
        sock_list.append(socks)
        i += 1
    #print(sock_list)
    sock_count = {}
    _count_elements(sock_count, sock_list)
    return(sock_count)

#random sock style and color function
def rand_sock_style_color(n):
    sock_style = ['ankle', 'crew', 'calf', 'thigh']
    sock_colors = ['black', 'white', 'blue']
    tuple_list = []
    i = 0
    while i < n:
        socks = random.choice(sock_style)
        colors = random.choice(sock_colors)
        sock_tuple = (socks, colors)
        tuple_list.append(sock_tuple)
        i += 1

    #print(tuple_list)
    style_color_count = {}
    _count_elements(style_color_count, tuple_list)
    for key in style_color_count:
        value = style_color_count[key]//2
        style_color_count[key] = value
    return(style_color_count)


#count pairs of socks function
def sock_pairs(dictionary):
    dict_pairs = {}
    for key in dictionary:
        dict_pairs[key] = dictionary[key] // 2
    return dict_pairs

#count loner socks function
def sock_loners(dictionary):
    dict_loners = {}
    for key in dictionary:
        loners = dictionary[key] % 2
        dict_loners[key] = loners
    return dict_loners

#generate 100 sock types
socks = rand_sock(100)
print(socks)

#find number of pairs
duplicates = sock_pairs(socks)
print(duplicates)

#find number of loners
loners = sock_loners(socks)
print(loners)

#generate 100 sock types and colors and show the amount of pairs
sock_color = rand_sock_style_color(100)
print(sock_color)