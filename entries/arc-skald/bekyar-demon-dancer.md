+++
id = "ref/arc-skald/bekyar-demon-dancer"
kind = "archetype"
title = "Bekyar Demon Dancer"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Bekyar%20Demon%20Dancer"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bekyar_demon_dancer", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "advanced-class-origins"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "versatile-performance" },
  { anchor = "fiendish-maw", level = 3 },
  { anchor = "abyssal-wrath", level = 6 },
  { anchor = "demonic-conquest", level = 7 },
]
trades = [
  { replaces = "Rage power gained at 3rd level", feature = "rage-powers", levels = [3], by = ["fiendish-maw"] },
  { alters = "Versatile performance", feature = "versatile-performance", by = ["versatile-performance"] },
  { alters = "Rage powers gained at 6th and 9th levels", feature = "rage-powers", levels = [6, 9], by = ["abyssal-wrath"] },
]
+++

While the twisted power of the demon-worshiping Bekyar's skalds is great, it comes at a terrible
price.

## Skills {#skills}

A Bekyar demon dancer gains Perform (dance) as a class skill.

## Versatile Performance (Ex) {#versatile-performance}

A Bekyar demon dancer can choose Perform (dance) for the versatile performance class feature. Its
associated skills are Acrobatics and Fly. This ability alters versatile performance.

## Fiendish Maw (Su) {#fiendish-maw}

At 3rd level, whenever a Bekyar demon dancer inspires rage, all who accept his rage gain a bite
attack dealing 1d6 points of damage (for Medium allies; 1d4 points of damage if Small). This damage
increases to 1d8 (1d6 if Small) at 7th level, to 2d6 (1d8 if Small) at 12th level, and to 3d6 (2d6
if Small) at 17th level. These increases effectively treat the affected creatures as though their
sizes had increased by one size category, and so don't stack with any similar damage increases (such
as the increase from the _[strong jaw](ref/spell/strong-jaw)_ spell) other than those due to an
actual increase in size. If used as part of a full attack action, the bite attack is made at the
creature's full base attack bonus - 5. This ability replaces the rage power gained at 3rd level.

## Abyssal Wrath (Su) {#abyssal-wrath}

At 6th level, the Bekyar demon dancer gains the [fiend totem](ref/ragepower/fiend-totem) rage power,
even if he doesn't qualify for it. At 9th level, he gains the
[greater fiend totem](ref/ragepower/greater-fiend-totem) rage power, ignoring the prerequisites.
This ability alters the rage powers gained at 6th and 9th levels.

## Demonic Conquest (Su) {#demonic-conquest}

At 7th level, the Bekyar demon dancer's dances warp the minds of those who accept them even further.
Whenever anyone affected by his inspired rage makes an attack against a creature, the urge to
dominate this foe rises within the affected ally. The ally can attempt to resist this urge with a
Will save (DC = 10 + 1/2 the skald's class level + his Charisma modifier). If she fails the save or
chooses not to attempt one, the Strength and Constitution bonuses of the demon dancer's inspire rage
increase by 2, and she must continue to attack the same target each round. Once the target is
defeated, she must burn or cut the symbol of a demon the Bekyar demon dancer worships into the
target's flesh, which is a full-round action. The need to conquer and brand foes ends after this
action or after the demon dancer stops performing, whichever comes first.
