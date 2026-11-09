+++
id = "ref/rule/character-classes"
kind = "rule"
title = "Character Classes"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "character_classes", path = "json/rules_adv_gm02.json" },
]
[[sources]]
publication = "pathfinder-unchained"
page = "196"

[fields]
kind = "none"
+++

You might create a monster that should use the statistics for a character class, either because the
monster would normally be created by adding class levels to the monster or because you think the
monster's abilities are similar enough to those of a character class that it would be quicker to
start with the class. In this case, look ahead to the [class grafts](ref/rule/class-grafts) and use
the array required by the class you desire. Keep in mind that a monster with class levels typically
has a CR equal to its class level - 1, so if you want your monster to have particular
level-dependent class abilities, you'll want to use the statistics for a CR that's 1 lower than the
target class level.

As mentioned before, a monster that primarily relies on its racial or innate abilities with only a
small number of class levels might be built differently. You can create the monster using its
[creature type graft](ref/rule/creature-type-grafts), then refer to the related class graft for
ideas of which monster options to select.
