+++
id = "ref/spell/contact-high"
kind = "spell"
title = "Contact High"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "contact_high", path = "json/spells12.json" },
]
[[sources]]
publication = "black-markets"
page = "19"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Investigator", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creatures touched (up to one per level)" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Bard, Investigator, Skald\
3: Cleric, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: living creatures touched (up to one per level)
:::

While under the effects of a drug, you can duplicate those effects in others. You can touch another
creature once per round (this requires a melee touch attack if the target is unwilling). When
touched, the target begins experiencing the effects of the same drug by which you are currently
affected (select one, if you are under the influence of more than one drug). The target doesn't take
any ability damage or risk addiction from the drug.

You cannot impart the effects of any potion, poison, elixir, or mutagen currently affecting you.
