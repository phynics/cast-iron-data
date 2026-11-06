+++
id = "ref/spell/soothe-construct"
kind = "spell"
title = "Soothe Construct"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soothe_construct", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 round"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one construct" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Cleric, Occultist, Oracle, Warpriest\
5: Arcanist, Sorcerer, Wizard
Casting time: 1 round
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: one construct
:::

**Sources:** Ultimate Magic pg 239

You soothe the elemental spirit of a targeted construct, reducing its chance of going berserk by
1d4% per four caster levels (maximum 5d4%). If cast on a construct that has already gone berserk and
you are its master, you may immediately roll d% to end the construct's berserk state, it returns to
normal functioning, and its berserk chance returns to 0%.
