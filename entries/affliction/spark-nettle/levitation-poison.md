+++
id = "ref/affliction/spark-nettle/levitation-poison"
kind = "affliction"
title = "Levitation poison"
source_ids = ["pathfinder-36-sound-of-a-thousand-screams"]
parent = "ref/monster/spark-nettle"
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spark_nettle|affliction:levitation-poison", path = "json/monsters22.json" },
]

[fields]
kind = "none"
+++

**Type:** Poison (Bite or contact-injury)

**Save:** Fortitude DC 16

**Frequency:** 1/round for 5 rounds

**Effect:** Dexterity damage 1 and [levitate](ref/spell/levitate) (victim rises 10 feet as per the
spell per failed save)

**Cure:** 2 consecutive saves. Skrik nettle poison can be cured by either
[neutralize poison](ref/spell/neutralize-poison) or [dispel magic](ref/spell/dispel-magic), as if it
were caster level 8th. The effect's CL equals the skrik nettle's Hit Dice.

The save DC is Constitution-based.
