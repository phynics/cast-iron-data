+++
id = "ref/spell/lend-path"
kind = "spell"
title = "Lend Path"
aon = "SpellDisplay.aspx?ItemName=Lend%20Path"
source_ids = ["mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lend_path", path = "json/spells6.json" },
]
[[sources]]
publication = "mythic-adventures"
page = "114"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Magus", level = 4 },
  { class = "Medium", level = 2 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Medium\
4: Bard, Magus, Skald, Summoner, Unchained Summoner\
5: Arcanist, Cleric, Druid, Hunter, Oracle, Psychic, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

You temporarily transfer one of your mythic path abilities to another creature, which can use it as
if it were part of the creature's own path. If the target is unable to expend mythic power, it can't
activate any part of the ability that requires expending uses of mythic power, but the ability
otherwise functions as if the creature were 1st tier.

While your path ability is transferred in this way, you can't use it yourself (even if it's an
automatic ability or one that doesn't require expending uses of mythic power).
