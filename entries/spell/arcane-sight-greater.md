+++
id = "ref/spell/arcane-sight-greater"
kind = "spell"
title = "Greater Arcane Sight"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_sight_greater", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/arcane-sight" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
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
Level: 7: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Target: you
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
:::

## Arcane Sight

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

### Greater Arcane Sight

**Sources:** PRPG Core Rulebook pg 244

This spell functions like [arcane sight](ref/spell/arcane-sight), except that you automatically know
which spells or magical effects are active upon any individual or object you see.

Unlike arcane sight, this spell cannot be made permanent with a permanency spell.
