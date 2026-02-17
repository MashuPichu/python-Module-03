# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 21:06:28 by klucchin        #+#    #+#               #
#  Updated: 2026/02/17 19:24:14 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math

pos = ("10", "20", "5")
target_pos = ("0", "0", "0")
distance = math.sqrt(
    (target_pos[0]-pos[0])**2 +
    (target_pos[1]-pos[1])**2 + (target_pos[2]-pos[2])**2
)

print(f"Parsing coordinates: "{pos[0]}, {pos[1]}, {pos[2]}"")