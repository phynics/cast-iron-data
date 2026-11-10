+++
id = "ref/spell/ice-crystal-teleport"
kind = "spell"
title = "Ice Crystal Teleport"
aon = "SpellDisplay.aspx?ItemName=Ice%20Crystal%20Teleport"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ice_crystal_teleport", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/teleport" },
]
[[sources]]
publication = "ultimate-magic"
page = "224"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1d4 rounds and instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Summoner\
6: Arcanist, Sorcerer, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: long (400 ft. + 40 ft./level)
Duration: 1d4 rounds and instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Teleportation
Descriptors: cold
:::

This spell functions as [teleport](ref/spell/teleport), except you use it to teleport yourself or
one other creature to a safe location you specify (the target can bring along objects as long as
their weight doesn't exceed the target's heavy load). You can only send the target to a location
with which you are very familiar. The target is first trapped in ice ([hardness](ref/umr/hardness)
0, 3 hit points per inch of thickness, 1 inch thick per caster level) for 1d4 rounds, during which
time it is paralyzed, aware but unable to take any physical actions, and begins to fade away as the
teleportation aspect takes effect. At the end of the 1d4 rounds, the target teleports to the
specified location, and the ice's hit points drop to 0 and it quickly melts away. If the ice is
destroyed before the target teleports, the spell ends and the teleport doesn't occur.
