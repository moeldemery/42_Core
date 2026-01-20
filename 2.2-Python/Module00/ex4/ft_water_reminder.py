# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/20 01:11:38 by meldemir          #+#    #+#              #
#    Updated: 2026/01/20 01:11:39 by meldemir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

def  ft_water_reminder():
    w_days = int(input("Days since last watering: "))
    if (w_days > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")