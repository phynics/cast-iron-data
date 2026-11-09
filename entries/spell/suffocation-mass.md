+++
id = "ref/spell/suffocation-mass"
kind = "spell"
title = "Mass Suffocation"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "suffocation_mass", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/suffocation" },
]
[[sources]]
publication = "advanced-players-guide"
page = "248"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Elementalist Wizard", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, M (a vial containing a bit of the caster’s breath)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature/2 levels (no two of which may be more than 30 feet apart)" },
]
duration = "1 round/level"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 9: Arcanist, Elementalist Wizard, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a vial containing a bit of the caster’s breath)
Range: close (25 ft. + 5 ft./2 levels)
Target: one living creature/2 levels (no two of which may be more than 30 feet apart)
Duration: 1 round/level
Saving throw: Fortitude partial
Spell resistance: yes
:::

### Mass Suffocation

This spell functions as [suffocation](ref/spell/suffocation) except as noted above. Note that the
duration of this spell is much longer, forcing those suffering from the effect to make far more
Fortitude saves to stave off eventual suffocation.
