+++
id = "ref/spell/teleport-greater"
kind = "spell"
title = "Greater Teleport"
aon = "SpellDisplay.aspx?ItemName=Teleport%2C%20Greater"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "teleport_greater", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/teleport" },
]
[[sources]]
publication = "core-rulebook"
page = "359"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V"
range = "personal and touch"
effects = [
  { label = "Target", value = "you and touched objects or other touched willing creatures" },
]
duration = "instantaneous"
saving_throw = "none and Will negates (object)"
spell_resistance = "no and yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Summoner\
6: Unchained Summoner\
7: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: personal and touch
Target: you and touched objects or other touched willing creatures
Duration: instantaneous
Saving throw: none and Will negates (object)
Spell resistance: no and yes (object)
Subschool: Teleportation
:::

### Greater Teleport

This spell functions like [teleport](ref/spell/teleport), except that there is no range limit and
there is no chance you arrive off target. In addition, you need not have seen the destination, but
in that case you must have at least a reliable description of the place to which you are
teleporting. If you attempt to teleport with insufficient information (or with misleading
information), you disappear and simply reappear in your original location. Interplanar travel is not
possible.
