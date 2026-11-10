+++
id = "ref/spell/scale-spikes-greater"
kind = "spell"
title = "Greater Scale Spikes"
aon = "SpellDisplay.aspx?ItemName=Scale%20Spikes%2C%20Greater"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scale_spikes_greater", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/scale-spikes" },
]
[[sources]]
publication = "monster-codex"
page = "141"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 4 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Investigator", level = 4 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a bit of thistle)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature/level that is a reptile, has the dragon type, or has the reptilian subtype, and also has a natural armor bonus of at least +1" },
]
duration = "1 hour/level"
saving_throw = "Fort negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Druid, Hunter, Ranger, Shaman, Sorcerer, Witch, Wizard\
4: Alchemist, Bloodrager, Investigator
Casting time: 1 standard action
Components: V, S, M/DF (a bit of thistle)
Range: close (25 ft. + 5 ft./2 levels)
Target: one living creature/level that is a reptile, has the dragon type, or has the reptilian subtype, and also has a natural armor bonus of at least +1
Duration: 1 hour/level
Saving throw: Fort negates (harmless)
Spell resistance: yes (harmless)
:::

### Greater Scale Spikes

This spell functions like [scale spikes](ref/spell/scale-spikes), except that the spikes growing out
of the scales have an enhancement bonus on attack and damage rolls equal to +1 for every 4 caster
levels (maximum +5). This bonus does not allow the spikes to bypass
[damage reduction](ref/rule/damage-reduction) aside from magic.
