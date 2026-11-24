+++
id = "ref/arc-bard/archaeologist"
kind = "archetype"
title = "Archaeologist"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Archaeologist"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "archaeologist", path = "json/archetypes_bard.json" },
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
  { anchor = "bardic-performance" },
  { anchor = "archaeologist-s-luck" },
  { anchor = "clever-explorer", level = 2 },
  { anchor = "uncanny-dodge", level = 2 },
  { anchor = "trap-sense", level = 3 },
  { anchor = "rogue-talents", level = 4 },
  { anchor = "evasion", level = 6 },
  { anchor = "advanced-talent", level = 12 },
]
trades = [
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["clever-explorer"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["uncanny-dodge"] },
]
+++

No stodgy researcher, this archaeologist meets his research head-on in the field. Archaeologists
sacrifice the bard's inspirational performance for a smattering of rogue talents. This archetype
also fits rogue-like characters that focus more on learning than on stabbing foes in the back.

## Bardic Performance {#bardic-performance}

Archaeologists do not gain the bardic performance ability or any of its performance types.

## Archaeologist's Luck (Ex) {#archaeologist-s-luck}

Fortune favors the archaeologist. As a swift action, an archaeologist can call on fortune's favor,
giving him a +1 luck bonus on attack rolls, saving throws, skill checks, and weapon damage rolls. He
can use this ability for a number of rounds per day equal to 4 + his Charisma modifier. Maintaining
this bonus is a free action, but it ends immediately if the archaeologist is killed, paralyzed,
stunned, knocked unconscious, or otherwise prevented from taking a free action to maintain it each
round. Archaeologist's luck is treated as bardic performance for the purposes of feats, abilities,
effects, and the like that affect bardic performance. Like bardic performance, it cannot be
maintained at the same time as other performance abilities. This bonus increases to +2 at 5th level,
+3 at 11th level, and +4 at 17th level.

## Clever Explorer (Ex) {#clever-explorer}

At 2nd level, an archaeologist gains a bonus equal to [half](ref/misc/fractions-and-rounding) his
class level on Disable Device and Perception checks. He can disable intricate and complex devices in
half the normal amount of time (minimum 1 round) and open a lock as a standard action. At 6th level,
an archaeologist can take 10 on Disable Device checks, even if distracted or endangered, and can
disarm magical traps. This ability replaces the versatile performance ability.

## Uncanny Dodge (Ex) {#uncanny-dodge}

At 2nd level, an archaeologist gains [uncanny dodge](ref/ability/uncanny-dodge), as the rogue class
feature of the same name. This ability replaces well-versed.

## Trap Sense (Ex) {#trap-sense}

At 3rd level, an archaeologist gains [trap sense](ref/ability/trap-sense) +1, as the rogue class
feature of the same name. This bonus improves by +1 for every three levels gained after 3rd, to a
maximum of +6 at 18th level.

## Rogue Talents {#rogue-talents}

At 4th level, an archaeologist gains a rogue talent. He gains an additional rogue talent for every
four levels of archaeologist gained after 4th level. Otherwise, this works as the rogue's rogue
talent ability.

## Evasion (Ex) {#evasion}

At 6th level, an archaeologist gains [evasion](ref/ability/evasion), as the rogue ability of the
same name.

## Advanced Talent {#advanced-talent}

At 12th level, and every four levels thereafter, an archaeologist can choose an advanced rogue
talent in place of a rogue talent.
