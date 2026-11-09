+++
id = "ref/spell/covetous-urge"
kind = "spell"
title = "Covetous Urge"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "covetous_urge", path = "json/spells12.json" },
]
[[sources]]
publication = "villain-codex"
page = "8"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["curse", "language-dependant"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a golden coin)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature with 7 HD or fewer" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Arcanist, Bard, Skald, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a golden coin)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one living creature with 7 HD or fewer
Subschool: Compulsion
Descriptors: curse, language-dependant
:::

You curse the target with insatiable greed, causing it to attempt to steal any item worth 100 gp or
more that it can see, each time it enters a new room or area. If it can see multiple items of value
in a single room or area, it attempts to steal the item it thinks is worth the most. This covetous
compulsion might cause the target to act recklessly where it normally would not (unless acting in
this manner would clearly cause it to die, suffer great harm, or get caught).

In combat, if the target sees a valuable item on an opponent, it must, for example, attempt to
disarm its foe to take a valuable weapon or use the steal combat maneuver to grab a precious item
kept on the opponent's belt. Once the target has either attempted to steal an item in combat or else
taken damage, this magical compulsion subsides until the threat of the current combat ends and the
target enters a new room or area. Affected targets in combat that have neither attempted to steal an
item nor taken damage (perhaps because the opponent with the most valuable item is far away) can
attempt a saving throw each round to ignore the spell's effect until the threat ends and the target
enters a new room.

[Break enchantment](ref/spell/break-enchantment), [limited wish](ref/spell/limited-wish),
[miracle](ref/spell/miracle), [remove curse](ref/spell/remove-curse), or [wish](ref/spell/wish) can
each end covetous urge before the duration expires. [Dispel magic](ref/spell/dispel-magic) does not
affect covetous urge.
