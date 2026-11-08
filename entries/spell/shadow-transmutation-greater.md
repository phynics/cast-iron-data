+++
id = "ref/spell/shadow-transmutation-greater"
kind = "spell"
title = "Greater Shadow Transmutation"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_transmutation_greater", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/shadow-transmutation" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Shaman", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "see text"
effects = [
  { label = "Target", value = "see text" },
]
duration = "see text"
saving_throw = "Will disbelief (if interacted with), varies, see text"
spell_resistance = "yes, see text"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 9: Arcanist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: see text
Target: see text
Duration: see text
Saving throw: Will disbelief (if interacted with), varies, see text
Spell resistance: yes, see text
Subschool: Shadow
Descriptors: shadow
:::

### Greater Shadow Transmutation

**Sources:** Blood of Shadows pg 31

This spell functions like [shadow transmutation](ref/spell/shadow-transmutation), except it can
mimic greater polymorph instead of polymorph. The illusory attacks and special abilities of any
shape assumed using greater shadow transmutation deal three-fifths (60%) damage to nonbelievers, and
non-damaging effects are 60% likely to work against nonbelievers.
