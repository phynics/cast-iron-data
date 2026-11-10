+++
id = "ref/spell/shadow-evocation-greater"
kind = "spell"
title = "Greater Shadow Evocation"
aon = "SpellDisplay.aspx?ItemName=Shadow%20Evocation%2C%20Greater"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_evocation_greater", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/shadow-evocation" },
]
[[sources]]
publication = "core-rulebook"
page = "340"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "see text"
effects = [
  { label = "Effect", value = "see text" },
]
duration = "see text"
saving_throw = "Will disbelief (if interacted with)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 8: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: see text
Effect: see text
Duration: see text
Saving throw: Will disbelief (if interacted with)
Spell resistance: yes
Subschool: Shadow
Descriptors: shadow
:::

### Greater Shadow Evocation

This spell functions like [shadow evocation](ref/spell/shadow-evocation), except that it enables you
to create partially real, illusory versions of sorcerer or wizard evocation spells of 7th level or
lower. If recognized as a greater shadow evocation, a damaging spell deals only three-fifths (60%)
damage.
