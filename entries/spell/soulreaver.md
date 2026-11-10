+++
id = "ref/spell/soulreaver"
kind = "spell"
title = "Soulreaver"
aon = "SpellDisplay.aspx?ItemName=Soulreaver"
source_ids = ["mythic-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soulreaver", path = "json/spells9.json" },
]
[[sources]]
publication = "mythic-origins"
page = "15"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "living creatures in a 20-ft.-radius spread" },
]
duration = "instantaneous"
saving_throw = "Fortitude half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 8: Arcanist, Cleric, Oracle, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude half
Spell resistance: yes
Target: living creatures in a 20-ft.-radius spread
Descriptors: death
:::

Favored by the necromancer Geb as a tool to turn his enemies' armies against themselves, this potent
death spell deals 1d6 points of damage per caster level (maximum 20d6) to living creatures in the
area of effect.
