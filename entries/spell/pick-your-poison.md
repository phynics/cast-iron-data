+++
id = "ref/spell/pick-your-poison"
kind = "spell"
title = "Pick Your Poison"
source_ids = ["inner-sea-gods", "gods-and-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pick_your_poison", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Bard, Cleric, Inquisitor, Oracle, Skald, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 10 minutes/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Healing
Descriptors: mind-affecting
:::

**Sources:** Inner Sea Gods pg 238, Gods and Magic pg 11

This spell temporarily converts even the deadliest poison affecting a creature into an intoxicating
alcohol. If the subject is affected by a poison effect while under the effects of this spell,
instead of the poison's normal effect, she feels intoxicated as if she'd just had a very strong
drink and takes a -2 penalty on attacks, saves, and checks for the duration of the spell. When the
spell's duration expires, the penalty ends and the poison's normal effects apply. Pick your poison
does not affect any poison effects that occurred before the spell was cast.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
