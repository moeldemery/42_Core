# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/20 01:12:10 by meldemir          #+#    #+#              #
#    Updated: 2026/01/20 01:12:12 by meldemir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

def ft_print_day(x, y):
    if x < y:
        print("Day",x + 1)
        ft_print_day(x + 1, y)

def ft_count_harvest_recursive():
    h_days = int(input("Days until harvest: "))
    ft_print_day(0 ,h_days)
    print("Harvest time!")