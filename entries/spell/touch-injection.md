+++
id = "ref/spell/touch-injection"
kind = "spell"
title = "Touch Injection"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "touch_injection", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Investigator", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Investigator\
3: Arcanist, Psychic, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Ultimate Combat pg 247

You must hold an elixir, infused extract, poison, or potion in hand as you cast this spell. The held
substance drains from its container into a magical sac in your body. While the spell lasts, you can
deliver the substance with a mere touch. To do so to an opponent, you must make a successful melee
touch attack. If you hit, the substance takes effect immediately, despite any onset period, and that
opponent receives the normal saving throw (if any) against the substance. In the case of a personal
infused extract, the opponent receives both a Fortitude save and
[spell resistance](ref/rule/spell-resistance). If you miss, the substance remains in the magical sac
for you to use later.

This spell protects you from poison in the sac, but unless you have the poison use class feature,
you suffer a 5% chance of exposing yourself to the poison when you first cast the spell. If you roll
a natural 1 while attempting to inject the poison into an enemy, you are exposed to it.
