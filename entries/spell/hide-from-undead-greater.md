+++
id = "ref/spell/hide-from-undead-greater"
kind = "spell"
title = "Greater Hide from Undead"
aon = "SpellDisplay.aspx?ItemName=Hide%20from%20Undead%2C%20Greater"
source_ids = ["core-rulebook", "people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hide_from_undead_greater", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/hide-from-undead" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "29"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Targets", value = "one touched creature/level" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless); see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Targets: one touched creature/level
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless); see text
Spell resistance: yes
:::

### Greater Hide from Undead

This spell functions as [hide from undead](ref/spell/hide-from-undead), except the spell does not
immediately end if a warded creature attempts to turn or command undead, channels positive energy,
touches an undead creature, or attacks any creature. Instead, when the warded creature takes one of
these actions, an intelligent undead creature can attempt another Will saving throw to negate the
effects of the spell.
