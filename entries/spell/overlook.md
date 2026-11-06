+++
id = "ref/spell/overlook"
kind = "spell"
title = "Overlook"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "overlook", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 3 },
  { class = "Skald", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Skald
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Inner Sea Races pg 221

> _The following spell is available to the indicated race or ethnicity:
> [Halfling](ref/race/halfling)_

You enhance your natural ability to seem small and unimportant, causing those around you to overlook
you. You gain a +20 bonus on Stealth checks, which doesn't stack with bonuses from effects that
actually make you sneakier, such as [invisibility](ref/spell/invisibility) or
[respectful quiet](ref/spell/respectful-quiet); you do not need cover or concealment to hide; and
you can hide while you are being observed. If a creature fails to notice you because of this spell,
that creature can still remember seeing a halfling pass by, but attach no importance to the memory.
You do not gain these benefits against creatures that are immune to compulsions or mind-affecting
effects, and [spell resistance](ref/rule/spell-resistance) applies. If you take an actively
aggressive or extremely conspicuous action, creatures automatically notice you, and you gain no
further benefits against those creatures for the remainder of the spell's duration.
