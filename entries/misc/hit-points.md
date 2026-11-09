+++
id = "ref/misc/hit-points"
kind = "rule"
title = "Hit Points (hp)"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hit_points", path = "json/misc.json" },
]
[[sources]]
publication = "core-rulebook"
page = "12"

[fields]
kind = "none"
+++

Hit points are an abstraction signifying how robust and healthy a [creature](ref/misc/creature) is
at the current moment. To determine a creature's hit points, roll the dice indicated by its
[Hit Dice](ref/misc/hit-dice). A creature gains maximum hit points if its first Hit Die roll is for
a character class level. Creatures whose first Hit Die comes from an NPC class or from his race roll
their first Hit Die normally. Wounds subtract hit points, while healing (both natural and magical)
restores hit points. Some abilities and spells grant
[temporary hit points](ref/rule/temporary-hit-points) that disappear after a specific duration. When
a creature's hit points drop below 0, it becomes [unconscious](ref/misc/unconscious). When a
creature's hit points reach a negative total equal to its Constitution score, it dies.
