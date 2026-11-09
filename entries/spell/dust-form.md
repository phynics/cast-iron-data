+++
id = "ref/spell/dust-form"
kind = "spell"
title = "Dust Form"
aon = "SpellDisplay.aspx?ItemName=Dust%20Form"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dust_form", path = "json/spells13.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "228"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Investigator", level = 5 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of dust gathered from a gravestone or sacred shrine)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Alchemist, Investigator\
6: Cleric, Druid, Hunter, Oracle, Psychic, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, M (a pinch of dust gathered from a gravestone or sacred shrine)
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

Upon casting this spell, you keep your relative form, but you and your equipment become composed
entirely of dust. While in this dust form, you take no penalties for squeezing, and can move through
spaces as if you were a creature three size categories smaller without penalty. You are also
considered incorporeal, though any nonmagical attack you make deals half damage (50%). Magic attacks
are unaffected, and you can still use your magic items and other equipment as normal.

If the duration ends in a square that your normal space cannot occupy, you take 3d6 damage and are
shunted to the nearest open space that you can normally occupy.
