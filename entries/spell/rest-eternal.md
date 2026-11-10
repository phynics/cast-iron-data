+++
id = "ref/spell/rest-eternal"
kind = "spell"
title = "Rest Eternal"
aon = "SpellDisplay.aspx?ItemName=Rest%20Eternal"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rest_eternal", path = "json/spells8.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "238"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 5 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 5 },
]
casting_time = "1 round"
components = "V, S, M/DF (ashes and a vial of holy or unholy water)"
range = "touch"
effects = [
  { label = "Target", value = "one dead creature touched" },
]
duration = "permanent"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Cleric, Oracle, Warpriest\
5: Druid, Hunter, Shaman, Witch
Casting time: 1 round
Components: V, S, M/DF (ashes and a vial of holy or unholy water)
Range: touch
Duration: permanent
Saving throw: none
Spell resistance: no
Target: one dead creature touched
Descriptors: curse
:::

You place a curse upon a dead creature that bars its spirit from returning. Anyone casting a spell
that would communicate with the dead creature, return it to life, or turn it into an undead creature
must succeed on a caster level check with a DC of 11 plus your caster level. Rest eternal cannot be
dispelled, but it can be negated with [remove curse](ref/spell/remove-curse) or
[break enchantment](ref/spell/break-enchantment).
