+++
id = "ref/spell/knell-of-the-depths"
kind = "spell"
title = "Knell of the Depths"
aon = "SpellDisplay.aspx?ItemName=Knell%20of%20the%20Depths"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "knell_of_the_depths", path = "json/spells6.json" },
]
[[sources]]
publication = "blood-of-the-coven"
page = "21"

[fields]
kind = "spell"
school = "conjuration"
descriptors = ["curse", "water"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Magus", level = 2 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 round"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Magus, Witch\
3: Arcanist, Druid, Hunter, Shaman, Sorcerer, Summoner, Wizard
Casting time: 1 round
Components: V, S
Range: touch
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: curse, water
:::

You invest a target with cursed elemental energy, causing nearby bodies of water to roil when the
target draw nears and tendrils of water to drag it deeper under the waves. The target takes a -10
penalty on Swim checks and automatically sinks 15 feet per round when in any body of liquid. The
creature does not sink if standing upon a solid surface capable of supporting its weight, even if it
is submerged.
