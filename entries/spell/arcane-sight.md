+++
id = "ref/spell/arcane-sight"
kind = "spell"
title = "Arcane Sight"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_sight", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Alchemist, Arcanist, Inquisitor, Investigator, Magus, Occultist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** PRPG Core Rulebook pg 244

This spell makes your eyes glow blue and allows you to see magical auras within 120 feet of you. The
effect is similar to that of a detect magic spell, but arcane sight does not require concentration
and discerns aura location and power more quickly.

You know the location and power of all magical auras within your sight. An aura's power depends on a
spell's functioning level or an item's caster level, as noted in the description of the
[detect magic](ref/spell/detect-magic) spell. If the items or creatures bearing the auras are in
line of sight, you can make Spellcraft skill checks to determine the school of magic involved in
each. (Make one check per aura; DC 15 + spell level, or 15 + half caster level for a non-spell
effect.)

If you concentrate on a specific creature within 120 feet of you as a standard action, you can
determine whether it has any spellcasting or [spell-like abilities](ref/umr/spell-like-abilities),
whether these are arcane or divine (spell-like abilities register as arcane), and the strength of
the most powerful spell or spell-like ability the creature currently has available for use.

As with detect magic, you can use this spell to identify the properties of magic items, but not
artifacts.

Arcane sight can be made permanent with a [permanency](ref/spell/permanency) spell.
