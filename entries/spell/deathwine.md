+++
id = "ref/spell/deathwine"
kind = "spell"
title = "Deathwine"
source_ids = ["rise-of-the-runelords-anniversary-edition", "pathfinder-5-sins-of-the-saviors"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deathwine", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 minute"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "1 potion touched/level" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no (object)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Alchemist, Cleric, Investigator, Oracle, Warpriest\
3: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 minute
Components: V, S
Range: touch
Duration: 1 hour/level
Saving throw: none
Spell resistance: no (object)
Target: 1 potion touched/level
:::

**Sources:** Rise of the Runelords Anniversary Edition pg 418, Pathfinder \#5: Sins of the Saviors
pg 58

This spell allows you to turn a potion into a temporary pool of necromantic energy. Only a potion
created using a conjuration (healing) spell can be affected by this spell. An affected potion turns
dark red and reveals a necromantic aura if detect magic is cast on it while it remains under this
spell's effects.

When you drink a potion affected by this spell, you do not gain the potion's normal effect. Instead,
the first necromancy spell you cast within the next minute is cast at a higher caster level. The
bonus to caster level is equal to the spell level of the spell used to create the potion that
deathwine affects. For example, a 5th-level wizard who drinks deathwine made from a potion of cure
serious wounds would cast his next necromancy spell as an 8th-level caster, as cure serious wounds
is a 3rd-level spell.

In addition, any undead creature (or other creature healed by negative energy) that drinks a potion
affected by deathwine is healed of 1d8 points of damage. Any potion not imbibed before this spell's
duration expires is destroyed at the end of the deathwine's duration.
