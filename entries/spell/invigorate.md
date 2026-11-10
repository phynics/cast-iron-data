+++
id = "ref/spell/invigorate"
kind = "spell"
title = "Invigorate"
aon = "SpellDisplay.aspx?ItemName=Invigorate"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invigorate", path = "json/spells14.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "230"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Bard", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
]
casting_time = "1 standard action"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Bard, Medium, Mesmerist, Psychic, Skald
Casting time: 1 standard action
Components: V
Range: touch
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Figment
:::

This spell banishes feelings of weariness. For the duration, the subject takes no penalties from the
fatigued or exhausted conditions. The effect of invigorate is merely an illusion, however, not a
substitute for actual rest or respite. When the spell ends, the subject takes 1d6 points of
nonlethal damage, along with the return of the original condition(s). A creature can be under the
effects of only one invigorate spell at a time; if it is cast a second time on that creature, the
first effect immediately ends.
