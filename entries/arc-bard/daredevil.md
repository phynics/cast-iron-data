+++
id = "ref/arc-bard/daredevil"
kind = "archetype"
title = "Daredevil"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Daredevil"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "daredevil", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-combat"
page = "32"

[fields]
kind = "archetype"
features = [
  { anchor = "agile" },
  { anchor = "bardic-performance" },
  { anchor = "derring-do" },
  { anchor = "canny-foe", level = 2 },
  { anchor = "dauntless", level = 2 },
  { anchor = "scoundrel-s-fortune", level = 5 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["agile"] },
  { replaces = "Inspire courage", feature = "bardic-performance", power = "inspire courage", by = ["derring-do"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["canny-foe"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["dauntless"] },
  { replaces = "Lore master", feature = "lore-master", by = ["scoundrel-s-fortune"] },
]
+++

As quick at wordplay as at swordplay, daredevils are dashing heroes, inspiring their allies to match
their clever repartee and acrobatic feats. Daredevils often lean toward comedy, dance, oratory, and
singing.

## Agile (Ex) {#agile}

A daredevil adds [half](ref/misc/fractions-and-rounding) her class level (minimum 1) on Acrobatics,
Bluff, Climb, and Escape Artist checks. This ability replaces bardic knowledge.

## Bardic Performance {#bardic-performance}

A daredevil gains the following type of bardic performance.

## Derring-do (Su) {#derring-do}

A daredevil can use her performance to bring out grace in the clumsiest allies. The daredevil and
any allies who see her receive a +1 morale bonus on Reflex saving throws and a +2 competence bonus
on Dexterity-based skill checks. Allies who move at least 10 feet during their turn gain a +1 dodge
bonus to their Armor Class until the start of their next turn. At 5th level, and every six bard
levels thereafter, the saving throw and Armor Class bonuses increase by +1, to a maximum of +4 at
17th level, and the skill check bonuses increase by +2, to a maximum of +8 at 17th level. This is a
mind-affecting ability that uses visual components. This ability replaces inspire courage.

## Canny Foe (Ex) {#canny-foe}

At 2nd level, a daredevil can choose one type of [combat maneuver](ref/rule/combat-maneuvers). She
gains a +2 bonus on her combat maneuver checks to attempt the chosen maneuver and to her CMD to
resist that maneuver. At 6th level, and every four levels thereafter, the daredevil gains a +2 bonus
for an additional type of combat maneuver. She may not choose the same maneuver twice. This ability
replaces versatile performance.

## Dauntless (Ex) {#dauntless}

At 2nd level, a daredevil gains a +1 morale bonus on saving throws against mind-affecting effects,
including all fear effects. This bonus increases by +1 for every four levels gained after 2nd level,
to a maximum of +5 at 18th level. This ability replaces well-versed.

## Scoundrel's Fortune (Ex) {#scoundrel-s-fortune}

At 5th level, once per day a daredevil can choose to roll two dice instead of one for any skill
check, keeping the best result. She can use this ability one additional time per day for every three
levels she possesses beyond 5th, to a maximum of six times per day at 20th level. This ability
replaces lore master.
