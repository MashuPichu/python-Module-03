# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42nice.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 19:52:09 by klucchin        #+#    #+#               #
#  Updated: 2026/02/22 18:34:45 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

print("=== Command Quest ===")

program_name = sys.argv[0]
total_args = len(sys.argv)

if total_args == 1:
    print("No arguments provided!")
    print(f"Program name: {program_name}")
    print(f"Total arguments: {total_args}")
else:
    print(f"Program name: {program_name}")
    print(f"Arguments received: {total_args - 1}")

    index = 1
    while index < total_args:
        print(f"Argument {index}: {sys.argv[index]}")
        index += 1

    print(f"Total arguments: {total_args}")
