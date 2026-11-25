+++
id = "ref/arc-brawler/mutagenic-mauler"
kind = "archetype"
title = "Mutagenic Mauler"
aon = "ArchetypeDisplay.aspx?FixedName=Brawler%20Mutagenic%20Mauler"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mutagenic_mauler", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]
[[sources]]
publication = "advanced-class-guide"
page = "86"

[fields]
kind = "archetype"
features = [
  { anchor = "mutagen", level = 1 },
  { anchor = "beastmorph", level = 4 },
]
trades = [
  { replaces = "Martial flexibility", feature = "martial-flexibility", by = ["mutagen"] },
  { replaces = "AC bonus", feature = "ac-bonus", by = ["beastmorph"] },
]
+++

Not content with perfecting her body with natural methods, a mutagenic mauler resorts to alchemy to
unlock the primal beast within.

## Mutagen (Su) {#mutagen}

At 1st level, a mutagenic mauler discovers how to create a mutagen that she can imbibe in order to
heighten her physical prowess, though at the cost of her personality. This functions as an
[alchemist's](ref/class/alchemist) mutagen and uses the brawler's class level as her alchemist level
for this ability (alchemist levels stack with brawler levels for determining the effect of this
ability). A mutagenic mauler counts as an alchemist for the purpose of imbibing a mutagen prepared
by someone else.

At 6th level, a mutagenic mauler gains a +2 bonus on damage rolls when she attacks in melee while in
her mutagenic form. This bonus increases to +3 at 11th level, and to +4 at 16th level. At 10th
level, a mutagenic mauler learns one of the following alchemist discoveries:
[feral mutagen](ref/discovery/feral-mutagen) or [infuse mutagen](ref/discovery/infuse-mutagen),
[preserve organs](ref/discovery/preserve-organs),
[spontaneous healing](ref/discovery/spontaneous-healing). At 12th level, the mutagenic mauler learns
the [greater mutagen](ref/discovery/greater-mutagen) discovery.

This ability replaces martial flexibility.

## Beastmorph (Su) {#beastmorph}

Starting at 4th level, a mutagenic mauler gains additional abilities when using her mutagen. At 4th
level, she gains [low-light vision](ref/rule/low-light-vision) and a +10 enhancement bonus to her
base speed. At 9th level, she gains [darkvision](ref/rule/darkvision) to a range of 30 feet and a
climb speed of 15 feet. At 13th level, the enhancement bonus to her base speed increases to +15 feet
and she gains the [scent](ref/umr/scent) ability within 30 feet. At 18th level, her climb speed
increases to 30 feet, and the enhancement bonus to her base speed increases to +20 feet. This
ability replaces AC bonus.
