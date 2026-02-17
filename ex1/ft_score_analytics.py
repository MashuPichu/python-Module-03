# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 20:04:31 by klucchin        #+#    #+#               #
#  Updated: 2026/02/13 21:04:36 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

print("=== Player Score Analytics ===")

score_list = []
i = 1

while i < len(sys.argv):
	try:
		score_list.append(int(sys.argv[i]))
	except ValueError:
		print(f"{sys.argv[i]} is not an int!")
	i += 1

total_players = len(score_list)

if total_players == 0:
	print("no score provided")
	quit()

total_score = sum(score_list)
average_score = total_score / total_players
max_score = max(score_list)
min_score = min(score_list)
range_score = max_score - min_score

print(f"Scores processed: {score_list}")
print(f"Total players: {total_players}")
print(f"Total score: {total_score}")
print(f"Average score: {average_score}")
print(f"High score: {max_score}")
print(f"Low score: {min_score}")
print(f"Score range: {range_score}")