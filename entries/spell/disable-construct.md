+++
id = "ref/spell/disable-construct"
kind = "spell"
title = "Disable Construct"
aon = "SpellDisplay.aspx?ItemName=Disable%20Construct"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "disable_construct", path = "json/spells3.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "179"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "construct touched" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Arcanist, Investigator, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: no
Target: construct touched
:::

You can make a melee touch attack to send a pulse into the target, interfering with the magic that
endows it with life. If the construct fails its saving throw, it becomes helpless, but it receives a
new save each round at the end of its turn to shake off the effect. If the construct is normally
immune to magic, the pulse is less effective and the construct receives a +4 bonus on its saving
throw.
