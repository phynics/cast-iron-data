+++
id = "ref/spell/cast-out"
kind = "spell"
title = "Cast Out"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cast_out", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Inquisitor", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Psychic", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Medium\
3: Inquisitor\
4: Psychic
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: instantaneous
Saving throw: Will partial
Spell resistance: yes
Target: creature touched
:::

**Sources:** Advanced Player's Guide pg 210

With a melee touch attack you blast a single creature and disrupt any magic controlling it. The
target takes 2d8 points of damage + 1 point per caster level (maximum +15). In addition, you make a
dispel check against any magic jar effect (including a ghost's malevolence ability) or enchantment
(compulsion) spells on the target creature, starting with the highest level spells and proceeding to
lower level spells. Treat this as a targeted [dispel magic](ref/spell/dispel-magic) spell, except
cast out can dispel one such spell for every four caster levels you possess. A successful Will save
halves the damage and limits the dispelling to a single spell or effect.
