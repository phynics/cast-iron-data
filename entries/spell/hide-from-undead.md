+++
id = "ref/spell/hide-from-undead"
kind = "spell"
title = "Hide from Undead"
source_ids = ["core-rulebook", "people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hide_from_undead", path = "json/spells5.json" },
]
[[sources]]
publication = "core-rulebook"
page = "296"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Warpriest", level = 1 },
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
Level: 1: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless); see text
Spell resistance: yes
Targets: one touched creature/level
:::

Undead cannot see, hear, or smell creatures warded by this spell. Even extraordinary or supernatural
sensory capabilities, such as [blindsense](ref/rule/blindsight-and-blindsense), blindsight, scent,
and [tremorsense](ref/umr/tremorsense), cannot detect or locate warded creatures. Nonintelligent
undead creatures (such as skeletons or zombies) are automatically affected and act as though the
warded creatures are not there. An intelligent undead creature gets a single Will saving throw. If
it fails, the subject can't see any of the warded creatures. If it has reason to believe unseen
opponents are present, however, it can attempt to find or strike them. If a warded creature attempts
to channel positive energy, turn or command undead, touches an undead creature, or attacks any
creature (even with a spell), the spell ends for all recipients.
