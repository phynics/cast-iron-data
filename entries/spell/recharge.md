+++
id = "ref/spell/recharge"
kind = "spell"
title = "Recharge"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "recharge", path = "json/spells8.json" },
]
[[sources]]
publication = "technology-guide"
page = "11"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 round"
components = "V, S, M (500 gp of diamond dust)"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Bard, Skald\
3: Arcanist, Cleric, Magus, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 round
Components: V, S, M (500 gp of diamond dust)
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Target: object touched
:::

You restore up to 1 charge per level to a battery or half that number of charges to a technological
item capable of being charged by a battery. If you recharge a battery, there is a 20% chance that
the battery is destroyed by the attempt. If you restore more charges than the item can hold, the
item must succeed at a Fortitude saving throw or take 1d6 points of electricity damage for each
excess charge. This spell provides no knowledge of how many charges an item can safely hold, but you
can choose to bestow fewer charges than the maximum allowed to reduce the risk; you must declare how
many charges you are restoring before casting this spell.
