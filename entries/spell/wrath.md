+++
id = "ref/spell/wrath"
kind = "spell"
title = "Wrath"
aon = "SpellDisplay.aspx?ItemName=Wrath"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wrath", path = "json/spells16.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "257"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Inquisitor", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a thorny vine)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Inquisitor
Casting time: 1 standard action
Components: V, S, M (a thorny vine)
Range: personal
Duration: 1 minute
Saving throw: none
Spell resistance: no
Target: you
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

You focus your anger against an enemy. Choose one enemy creature that you can see. You gain a +1
morale bonus on attack rolls and weapon damage rolls against that designated creature for every
three caster levels you have (at least +1, maximum +3). You also receive this bonus on caster level
checks made to overcome the creature's [spell resistance](ref/rule/spell-resistance), if any. At
12th level, you gain the benefits of the [Improved Critical](ref/feat/improved-critical) feat on
attack rolls made against the designated creature. This effect doesn't stack with any other effect
that expands the threat range of a weapon.
