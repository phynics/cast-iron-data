+++
id = "ref/spell/foretell-failure"
kind = "spell"
title = "Foretell Failure"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "foretell_failure", path = "json/spells13.json" },
]
[[sources]]
publication = "arcane-anthology"
page = "24"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Occultist", level = 5 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 swift action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Bard, Oracle, Psychic, Skald, Witch\
5: Arcanist, Occultist, Sorcerer, Wizard
Casting time: 1 swift action
Components: V, S
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
:::

You cast this spell immediately before you would take an action that requires a d20 roll, such as a
skill check, attack roll, or ability check. The action must be something you can complete in a
single round. The spell magically informs you whether the action will succeed if you roll a 10 or
better on the d20 roll involved. If the action would be successful under those circumstances, you
must take the action. If the action would not be successful, you can take a different action.
