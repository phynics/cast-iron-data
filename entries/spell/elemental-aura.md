+++
id = "ref/spell/elemental-aura"
kind = "spell"
title = "Elemental Aura"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elemental_aura", path = "json/spells4.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "218"

[fields]
kind = "spell"
school = "evocation [acid, cold, electricity, or fire]"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "Reflex half, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation \[acid, cold, electricity, or fire\]
Level: 3: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level (D)
Saving throw: Reflex half, see text
Spell resistance: yes
Target: you
:::

This spell forms an aura of energy around you, damaging all those that come near you. Choose an
energy type: acid, cold, electricity, or fire. Creatures adjacent to you when this spell is cast and
at the start of your turn take 2d6 points of energy damage of the selected type. This aura has an
additional effect, depending upon the type of energy chosen.

_Acid:_ Creatures affected by your aura take 1 point of ongoing acid damage per round for 1 round
per three caster levels, and are sickened for the duration of the ongoing acid damage.

_Cold:_ Creatures affected by your aura are fatigued. A creature that is already fatigued suffers no
additional effect.

_Electricity:_ Creatures affected by your aura are staggered for 1 round.

_Fire:_ Creatures affected by your aura catch on fire.

Creatures adjacent to you are allowed a Reflex save to halve the damage and negate the additional
effect. The aura's additional effects do not stack if a creature takes damage from your aura
multiple times. You may only have one elemental aura in effect at one time. When you cast this spell
to deal acid, cold, electricity, or fire damage, it is a spell of that type.
