# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42nice.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 19:18:48 by klucchin        #+#    #+#               #
#  Updated: 2026/02/22 18:34:30 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

def inventory_report(inventory, total_items):

    for name, quantity in inventory.items():
        percentage = (quantity / total_items) * 100
        
        if quantity == 1:
           unit_word = "unit"
        else:
            unit_word = "units"
        
        print(f"{name}: {quantity} {unit_word} ({round(percentage, 1)}%)")


def main():

    print("=== Inventory System Analysis ===")

    inventory = dict()

    for arg in sys.argv[1:]:
        parts = arg.split(":")

        name = parts[0]
        quantity = int(parts[1])

        inventory.update({name: quantity})

    total_items = 0
    for value in inventory.values():
        total_items += value
    
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}\n")
    
    print("== Current Inventory ===")
    inventory_report(inventory, total_items)

    print("\n=== Inventory Statistics ===")



if __name__ == "__main__":
    main()
