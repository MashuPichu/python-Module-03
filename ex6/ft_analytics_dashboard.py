# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42nice.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 22:24:11 by klucchin        #+#    #+#               #
#  Updated: 2026/02/25 15:58:49 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def list_example(player_list, score_list):
    
    print("=== List Comprehension Examples ===")

    print(f"Active players: {player_list}")

    score_list_value = [s for s in score_list if s > 2000]
    print(f"High scores (>2000): {score_list_value}")

    score_list_double = [s * 2 for s in score_list]
    print(f"Scores doubled: {score_list_double}")


def dict_example(dictionnary):
    
    print("=== Dict Comprehension Examples ===")


def set_example(set):

    print("=== Set Comprehension Examples")


def main():
    
    player_list = ["bob", "Charlie", "Tango", "Sierra"]
    score_list = [2500, 1200, 3000, 1999]

    list_example(player_list, score_list)


if __name__ == "__main__":
    main()
    
    