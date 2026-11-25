+++
id = "ref/arc-magus/staff-magus"
kind = "archetype"
title = "Staff Magus"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Staff%20Magus"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "staff_magus", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "ultimate-magic"
page = "49"

[fields]
kind = "archetype"
features = [
  { anchor = "quarterstaff-master", level = 1 },
  { anchor = "quarterstaff-defense", level = 7 },
  { anchor = "staff-weapon", level = 10 },
]
trades = [
  { replaces = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Medium armor", feature = "medium-armor", by = ["quarterstaff-defense"] },
  { replaces = "heavy armor", feature = "heavy-armor", by = ["quarterstaff-defense"] },
  { replaces = "Fighter training", feature = "fighter-training", by = ["staff-weapon"] },
]
+++

While most magi use a one-handed weapon as their melee implement of choice, one group of magi uses
the quarterstaff instead. These lightly armored magi use staves for both defense and inflicting
their spells upon enemies. Skilled in manipulating these weapons with one hand or two, they
eventually learn how to use arcane staves as well, and are just as formidable in combat as their
sword-swinging brethren.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A staff magus is proficient with simple weapons only. He can cast magus spells while wearing light
armor without incurring the normal arcane spell failure chance. Like any other arcane spellcaster, a
magus wearing medium armor or heavy armor or using a shield incurs a chance of arcane spell failure
if the spell in question has a somatic component. A multiclass magus still incurs the normal arcane
spell failure chance for arcane spells received from other classes. This replaces the normal magus
weapon and armor proficiency feature.

## Quarterstaff Master (Ex) {#quarterstaff-master}

At 1st level, the staff magus gains the [Quarterstaff Master](ref/feat/quarterstaff-master) feat
(see Chapter 3) as a bonus feat, even if he does not meet the normal prerequisites. He only gains
the benefit of this feat when wearing no armor or light armor.

## Quarterstaff Defense (Ex) {#quarterstaff-defense}

At 7th level, while wielding a quarterstaff, the staff magus gains a shield bonus to his Armor Class
equal to the enhancement bonus of the quarterstaff, including any enhancement bonus on that staff
from his arcane pool class feature. At 13th level, this bonus increases by +3. This ability replaces
the medium armor and heavy armor class abilities.

## Staff Weapon (Su) {#staff-weapon}

At 10th level, a staff magus treats any magical staff he is wielding as a magical quarterstaff with
an enhancement bonus to attack and damage equal to the staff's caster level divided by 4 (minimum
+1). The staff must have at least 1 charge for the magus to use this ability. A staff magus can
restore 1 charge to a staff by expending a number of points from his arcane pool equal to the level
of the highest-level spell cast in the staff, as long as at least one spell in the staff is on the
magus spell list. The magus cannot restore charges to more than one staff per day. This ability
replaces fighter training.

## Magus Arcana {#magus-arcana}

The following magus arcana complement the staff magus archetype:
[critical strike](ref/arcana/critical-strike), [dispelling strike](ref/arcana/dispelling-strike),
maneuver master, and [spell shield](ref/arcana/spell-shield).
