+++
id = "ref/spell/runic-overload"
kind = "spell"
title = "Runic Overload"
source_ids = ["giant-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "runic_overload", path = "json/spells8.json" },
]
[[sources]]
publication = "giant-hunters-handbook"
page = "26"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a small rune carved from stone)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature or object" },
]
duration = "instantaneous"
saving_throw = "see text"
spell_resistance = "see text"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Bloodrager\
4: Magus\
5: Arcanist, Sorcerer, Wizard\
6: Witch
Casting time: 1 standard action
Components: V, S, M (a small rune carved from stone)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: see text
Spell resistance: see text
Target: one creature or object
Descriptors: sonic
:::

This spell charges magical runes to an explosive degree. If cast on a creature with magical runes on
its body, such as a rune giant or a runescarred creature, it deals 1d6 points of sonic damage per
caster level (maximum 20d6) to the target and stuns the target for 1 round. When the spell is cast
in this way, it must overcome the target's [spell resistance](ref/rule/spell-resistance). A
successful Will save halves the damage and negates the stun effect.

The spell can also be cast on other magical runes, such as those from arcane mark or explosive
runes. In this case, the resulting explosion deals 1d8 points of sonic damage per 2 caster levels
(maximum 10d8) to all creatures within a 5-foot radius. Creatures in the area that succeed at a
Reflex save take half damage. This spell doesn't destroy runes; targeted runes continue to function
normally. Mundane runes, such as ones in writing or runic tattoos, cannot be affected by this spell.
