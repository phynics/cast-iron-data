+++
id = "ref/spell/hide-from-animals"
kind = "spell"
title = "Hide from Animals"
aon = "SpellDisplay.aspx?ItemName=Hide%20from%20Animals"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hide_from_animals", path = "json/spells5.json" },
]
[[sources]]
publication = "core-rulebook"
page = "296"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
]
casting_time = "1 standard action"
components = "S, DF"
range = "touch"
effects = [
  { label = "Targets", value = "one creature touched/level" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Druid, Hunter, Ranger, Shaman
Casting time: 1 standard action
Components: S, DF
Range: touch
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes
Targets: one creature touched/level
:::

Animals cannot sense the warded creatures. Even extraordinary or supernatural sensory capabilities,
such as [blindsense](ref/rule/blindsight-and-blindsense), blindsight, scent, and
[tremorsense](ref/umr/tremorsense), cannot detect or locate warded creatures. Animals simply act as
though the warded creatures are not there. If a warded character touches an animal or attacks any
creature, even with a spell, the spell ends for all recipients.
