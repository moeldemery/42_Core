# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/20 01:11:59 by meldemir          #+#    #+#              #
#    Updated: 2026/01/20 01:12:01 by meldemir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

def ft_count_harvest_iterative():
    h_days = int(input("Days until harvest: "))
    for i in range(h_days):
        print("Day",i+1)
    print("Harvest time!")