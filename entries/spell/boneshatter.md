+++
id = "ref/spell/boneshatter"
kind = "spell"
title = "Boneshatter"
aon = "SpellDisplay.aspx?ItemName=Boneshatter"
source_ids = ["pathfinder-84-pyramid-of-the-sky-pharaoh", "osirion-land-of-the-pharaohs"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "boneshatter", path = "json/spells2.json" },
]
[[sources]]
publication = "pathfinder-84-pyramid-of-the-sky-pharaoh"
page = "15"
[[sources]]
publication = "osirion-land-of-the-pharaohs"
page = "26"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a broken bone)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one corporeal creature or object" },
]
duration = "instantaneous and 1 minute/level (see text)"
saving_throw = "Fortitude partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Arcanist, Sorcerer, Wizard\
5: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, M (a broken bone)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous and 1 minute/level (see text)
Saving throw: Fortitude partial (see text)
Spell resistance: yes
Target: one corporeal creature or object
:::

The target's bones (or exoskeleton) splinter, dealing 1d6 points of damage per caster level (maximum
15d6) to the target, which is also exhausted for 1 minute per caster level from the pain and
exertion of the transformation.

If the target succeeds at its save, it takes half damage and is fatigued rather than exhausted.
Objects made of bone, chitin, or similar material take half again as much damage (+50%) from this
spell. This spell has no effect on a creature that has neither a skeleton nor a hard carapace.
