+++
id = "ref/hex/withering"
kind = "rule"
title = "Withering"
source_ids = ["potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "withering", path = "json/class_ability_hexes.json" },
]

[fields]
kind = "none"
+++

**Withering (Su)**

**Ability:** The target ages to the next [age category](ref/rule/age) (adult to middle-aged, and so
on). The witch gains a number of [temporary hit points](ref/rule/temporary-hit-points) equal to
1d10 + her witch level and a +2 enhancement bonus to either Strength, Dexterity, or Constitution for
a number of hours equal to her Intelligence modifier. These effects last for a number of hours equal
to the witch's level.

**Flavor:** The witch causes a creature within 30 feet to age rapidly, empowering the witch in the
process.

**Special:** A creature cannot be aged past venerable age by this hex, and it can attempt a
Fortitude save to negate the effect altogether. Once a creature has successfully saved against the
_withering_ hex, it cannot be affected by it again.
