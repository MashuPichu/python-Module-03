# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 17:53:08 by klucchin        #+#    #+#               #
#  Updated: 2026/02/18 19:18:54 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def rare_achievements(all_achievements, alice, bob, charlie):
    rare = set()
    for achievement in all_achievements:
        count = 0

        if achievement in alice:
            count += 1
        if achievement in bob:
            count += 1
        if achievement in charlie:
            count += 1

        if count == 1:
            rare.add(achievement)

    return rare


def main():
    print("=== Achievement Tracker System ===\n")

    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {"level_10", "treasure_hunter",
               "boss_slayer", "speed_demon", "perfectionist"}

    print(f"Player alice achievement: {alice}")
    print(f"Player bob achievement: {bob}")
    print(f"Player charlie achievement: {charlie}\n")

    union1 = alice.union(bob)
    union2 = bob.union(charlie)
    union = union1.union(union2)

    print("=== Achievement Analytics ===\n")
    print(f"All unique achievements: {union}")
    print(f"Total unique achievements: {len(union)}\n")

    common = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common}")

    rare = rare_achievements(union, alice, bob, charlie)
    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob - charlie}")
    print(f"Bob unique: {bob - alice - charlie}")


if __name__ == "__main__":
    main()
