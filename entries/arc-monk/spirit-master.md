+++
id = "ref/arc-monk/spirit-master"
kind = "archetype"
title = "Spirit Master"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Spirit%20Master"
source_ids = ["undead-slayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spirit_master", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "undead-slayers-handbook"
page = "22"

[fields]
kind = "archetype"
replaces = ["Still mind", "Maneuver training", "Purity of body", "Wholeness of body", "Quivering palm", "Empty body", "Perfect self"]
+++

Spirit masters are monks who specialize in combating the undead, laying their corpses to rest, and
sending their souls to final judgment.

**Resilient Soul (Ex)**

**Gained:** At 3rd Level

**Passive:** A spirit master gains a +2 bonus on saving throws against necromancy spells and
effects.

**Replaces:** Still mind

**Spirit Combat (Su)**

**Ability:** A spirit master can charge his unarmed strike so it affects incorporeal creatures. The
spirit master's unarmed strike deals half damage to incorporeal creatures, or full damage if it's a
magic weapon (such as via an [amulet of mighty fists](ref/magic-wondrous/amulet-of-mighty-fists)).
This benefit lasts for a number of rounds equal to the spirit master's class level.

**Gained:** At 3rd Level

**Replaces:** Maneuver training

**Usage:** Wisdom3 modifier times/day

**Diamond Spirit (Ex)**

**Ability:** Once per day when attempting a Fortitude save to remove a temporary negative level, the
spirit master may choose to automatically succeed.

**Gained:** At 5th Level

**Passive:** A spirit master becomes fortified against the effects of
[energy drain](ref/rule/energy-drain-and-negative-levels). When the spirit master gains a negative
level, he does not take any penalties, his total hit points remain unchanged, and he is not
considered lower level for the purpose of level-dependent variables.

**Replaces:** Purity of body

**Special:** The spirit master still dies if his number of negative levels equals or exceeds his
number of Hit Dice.

**Spirit Burst (Su)**

**Free:** Whenever a spirit master destroys an undead creature with a melee attack, he may expend 2
points from his _ki pool_ to release an 15-foot-radius [burst](ref/misc/burst) of positive energy
centered on the destroyed creature. Undead creatures in the affected area each take a number of
points of damage equal the number of Hit Dice of the destroyed creature. Living creatures in the
area are healed by the same amount.

**Gained:** At 7th Level

**Replaces:** Wholeness of body

**Purifying Palm (Su)**

**Ability:** The spirit master can make a purifying palm attack once per day, and must announce his
intention before making a melee attack roll. If his attack deals damage, the target must attempt a
Will save (DC = 10 + 1/2 the spirit master's class level + the spirit master's Wisdom modifier). On
a failed save, the target cannot [channel energy](ref/ability/channel-energy), nor can it be healed
by positive or negative energy. This effect lasts for 1 round per class level. If the target is an
undead creature, it must succeed at its Will save or be instantly destroyed.

**Flavor:** The spirit master gains the ability to alter the balance of positive and negative energy
within an opponent's body.

**Gained:** At 15th Level

**Replaces:** Quivering palm

**Spirit Flow (Su)**

**Flavor:** A spirit master can dramatically alter the flow of his own ki.

**Immediate:** The spirit master can expend 3 ki points to alter his ki for a number of rounds equal
to his class level. During this time, he is healed by negative energy as if he were an undead
creature. The spirit master is still healed by positive energy as normal.

**Gained:** At 19th Level

**Replaces:** Empty body

**Spirit Mastery (Su)**

**Ability:** Once per week, the spirit master may bring a dead creature back to life. This ability
functions as [true resurrection](ref/spell/true-resurrection), except the spirit master may not
resurrect a creature that has been dead for longer than 1 day per class level.

**Gained:** At 20th Level

**Passive:** A spirit master gains DR 10/evil and becomes immune to
[ability drain and ability damage](ref/rule/ability-damage-drain).

**Replaces:** Perfect self
