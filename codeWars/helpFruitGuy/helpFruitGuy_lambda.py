#!/usr/bin/env python3

bag = []
bag2 = ["rottenApple", "rottenBanana", "Catelope", "rottenPineapple", "Kiwi"]


def remove_rotten(bag_of_fruits):''''
  try:
    return map(lambda x: x.replace("rotten", "").lower(), bag_of_fruits)
  except Exception:
    return []

print(remove_rotten(bag))
