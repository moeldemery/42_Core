# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/20 01:11:08 by meldemir          #+#    #+#              #
#    Updated: 2026/01/20 01:11:09 by meldemir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

def  ft_harvest_total():
    d1 = input("Day 1 harvest: ")
    d2 = input("Day 2 harvest: ")
    d3 = input("Day 3 harvest: ")
    total = int(d1) + int(d2) + int(d3)
    print("Total harvest:", total)