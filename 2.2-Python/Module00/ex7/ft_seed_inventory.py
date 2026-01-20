# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/20 01:12:31 by meldemir          #+#    #+#              #
#    Updated: 2026/01/20 01:12:32 by meldemir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

def ft_seed_inventory(seed_type: str, quantity: int, unit: str)-> None:
    if unit.lower() == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif unit.lower() == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    elif unit.lower() == "area":
        print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")