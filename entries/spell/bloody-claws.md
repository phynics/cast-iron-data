+++
id = "ref/spell/bloody-claws"
kind = "spell"
title = "Bloody Claws"
aon = "SpellDisplay.aspx?ItemName=Bloody%20Claws"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bloody_claws", path = "json/spells2.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "206"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Hunter, Ranger\
4: Druid
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: living creature touched
:::

You give a creature the ability to deal bleed damage when making natural attacks so long as the
attack deals slashing or piercing damage. This bleed damage for each attack is equal to one-half
your caster level (limited to the creature's maximum damage with that attack), though bleed damage
does not stack. When two or more attacks deal bleed damage, take the worse effect.
