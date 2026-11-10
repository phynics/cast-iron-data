+++
id = "ref/spell/remove-radioactivity"
kind = "spell"
title = "Remove Radioactivity"
aon = "SpellDisplay.aspx?ItemName=Remove%20Radioactivity"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "remove_radioactivity", path = "json/spells8.json" },
]
[[sources]]
publication = "technology-guide"
page = "11"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Ranger", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature or object touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Bard, Cleric, Druid, Hunter, Inquisitor, Oracle, Paladin, Ranger, Skald, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Target: creature or object touched
Subschool: Healing
:::

You remove all ongoing radiation effects, both primary and secondary, on a single target if you
succeed at a caster level check (DC = the Fortitude DC associated with the radiation effect). In
addition, you immediately restore 1d4 points of Constitution drain and 1d4 points of Strength drain
caused by radiation-this spell cannot restore ability damage or drain caused by other sources. When
cast on an area, a single casting of remove radioactivity removes radiation from a 20-foot-radius
area around the point you touch. This spell has no power to negate naturally radioactive materials,
and as long as such materials remain in an area, the radiation that was removed may return.
