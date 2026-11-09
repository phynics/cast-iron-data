+++
id = "ref/spell/unshakable-chill"
kind = "spell"
title = "Unshakable Chill"
aon = "SpellDisplay.aspx?ItemName=Unshakable%20Chill"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unshakable_chill", path = "json/spells11.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "246"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "10 minutes/level; see text"
saving_throw = "Fortitude negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Arcanist, Bloodrager, Druid, Hunter, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level; see text
Saving throw: Fortitude negates (see text)
Spell resistance: yes
Target: one creature
Descriptors: cold
:::

The target is filled with an unshakable chill for the duration of the spell, and suffers from the
effects of severe cold. Severe cold means if the initial saving throw fails, the target takes 1d6
points of nonlethal cold damage and must save every 10 minutes (using the DC of severe cold instead
of this spell's DC) or take additional damage.
