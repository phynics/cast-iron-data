+++
id = "ref/spell/shock-shield"
kind = "spell"
title = "Shock Shield"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shock_shield", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["electricity", "force"]
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
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
School: abjuration
Level: 1: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: electricity, force
:::

**Sources:** Ultimate Combat pg 243

This spell creates an invisible shield similar to but not as strong as the
[shield](ref/spell/shield) spell. This shield hovers in front of you and negates
[magic missile](ref/spell/magic-missile) attacks directed at you. The disk provides a +2 shield
bonus to AC. This bonus applies against incorporeal touch attacks.

At any time, as a free action, you may dismiss your shield, at which point it deals 1d6 points of
electrical damage to all creatures within a 5-foot burst, including you. A Reflex saving throw
halves the damage.
