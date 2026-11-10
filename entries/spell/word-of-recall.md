+++
id = "ref/spell/word-of-recall"
kind = "spell"
title = "Word of Recall"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "word_of_recall", path = "json/spells16.json" },
]
[[sources]]
publication = "core-rulebook"
page = "371"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 8 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 7 },
  { class = "Warpriest", level = 6 },
]
casting_time = "1 standard action"
components = "V"
range = "unlimited"
effects = [
  { label = "Target", value = "you and touched objects or other willing creatures" },
]
duration = "instantaneous"
saving_throw = "none or Will negates (harmless, object)"
spell_resistance = "no or yes (harmless, object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Cleric, Oracle, Warpriest\
7: Psychic\
8: Druid
Casting time: 1 standard action
Components: V
Range: unlimited
Duration: instantaneous
Saving throw: none or Will negates (harmless, object)
Spell resistance: no or yes (harmless, object)
Target: you and touched objects or other willing creatures
Subschool: Teleportation
:::

Word of recall teleports you instantly back to your sanctuary when the word is uttered. You must
designate the sanctuary when you prepare the spell, and it must be a very familiar place. The actual
point of arrival is a designated area no larger than 10 feet by 10 feet. You can be transported any
distance within a plane but cannot travel between planes. You can transport, in addition to
yourself, any objects you carry, as long as their weight doesn't exceed your maximum load. You may
also bring one additional willing Medium or smaller creature (carrying gear or objects up to its
maximum load) or its equivalent per three caster levels. A Large creature counts as two Medium
creatures, a Huge creature counts as two Large creatures, and so forth. All creatures to be
transported must be in contact with one another, and at least one of those creatures must be in
contact with you. Exceeding this limit causes the spell to fail.

An unwilling creature can't be teleported by word of recall. Likewise, a creature's Will save (or
[spell resistance](ref/rule/spell-resistance)) prevents items in its possession from being
teleported. Unattended, nonmagical objects receive no saving throw.
