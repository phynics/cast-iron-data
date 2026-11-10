+++
id = "ref/spell/prosperous-room"
kind = "spell"
title = "Prosperous Room"
aon = "SpellDisplay.aspx?ItemName=Prosperous%20Room"
source_ids = ["quests-and-campaigns"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "prosperous_room", path = "json/spells15.json" },
]
[[sources]]
publication = "quests-and-campaigns"
page = "29"

[fields]
kind = "spell"
school = "enchantment"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 day"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "room you own; see text" },
]
duration = "1 day/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 1 day
Components: V, S
Range: touch
Duration: 1 day/level (D)
Saving throw: none
Spell resistance: yes
Target: room you own; see text
:::

The targeted room is enchanted to have magical appeal for customers, an increase in the workflow of
its employees, or the generation of additional materials to work with. While this spell is in
effect, the targeted room produces 1 more Goods, Labor, Influence, or Magic than it already does. If
the room produces multiple types of capital, it produces an additional capital of each type. If the
room generates gp, it generates 25% more. Only the capital that the room normally generates
increases-rooms that do not already generate Magic, for instance, do not generate Magic because of
this spell.

While this spell is in effect, neither you nor your allies can further interact with the affected
room or the spell's effects immediately end. You cannot spend downtime actions to run a business
with a room that is affected by this spell, though any employees or workers that operate within the
room may continue to do so normally.
