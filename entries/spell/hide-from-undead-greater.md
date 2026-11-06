+++
id = "ref/spell/hide-from-undead-greater"
kind = "spell"
title = "Greater Hide from Undead"
source_ids = ["core-rulebook", "people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hide_from_undead_greater", path = "json/spells5.json" },
]

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

## Hide from Undead

**Sources:** PRPG Core Rulebook pg 296

Undead cannot see, hear, or smell creatures warded by this spell. Even extraordinary or supernatural
sensory capabilities, such as [blindsense](ref/rule/blindsight-and-blindsense), blindsight, scent,
and [tremorsense](ref/umr/tremorsense), cannot detect or locate warded creatures. Nonintelligent
undead creatures (such as skeletons or zombies) are automatically affected and act as though the
warded creatures are not there. An intelligent undead creature gets a single Will saving throw. If
it fails, the subject can't see any of the warded creatures. If it has reason to believe unseen
opponents are present, however, it can attempt to find or strike them. If a warded creature attempts
to channel positive energy, turn or command undead, touches an undead creature, or attacks any
creature (even with a spell), the spell ends for all recipients.

### Greater Hide from Undead

**Sources:** People of the Wastes pg 29

This spell functions as hide from undead, except the spell does not immediately end if a warded
creature attempts to turn or command undead, channels positive energy, touches an undead creature,
or attacks any creature. Instead, when the warded creature takes one of these actions, an
intelligent undead creature can attempt another Will saving throw to negate the effects of the
spell.
