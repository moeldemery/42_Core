# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/20 01:11:22 by meldemir          #+#    #+#              #
#    Updated: 2026/01/20 01:11:24 by meldemir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

def  ft_plant_age():
    age = input("Enter plant age in days: ")
    if (int(age) > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")