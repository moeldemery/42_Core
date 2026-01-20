# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/20 03:21:02 by meldemir          #+#    #+#              #
#    Updated: 2026/01/20 03:21:04 by meldemir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

def ft_garden_summary():
    g_name = input("Enter garden name: ")
    g_plant_no = int(input("Enter number of plants:"))
    print(f"Garden: {g_name}")
    print(f"Plants: {g_plant_no}")
    print("Status: Growing well!")
