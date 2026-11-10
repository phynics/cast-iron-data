+++
id = "ref/spell/death-from-below"
kind = "spell"
title = "Death from Below"
aon = "SpellDisplay.aspx?ItemName=Death%20from%20Below"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "death_from_below", path = "json/spells3.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "39"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Bard", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Arcanist, Bloodrager, Sorcerer, Wizard\
3: Bard, Skald
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: creature touched
:::

> _[Gnomes](ref/race/gnome) have access to the following spell._

You grant the target a dodge bonus to its Armor Class against attacks from larger creatures. The
bonus is equal to +1 for every size category the attacker is larger than the target of the spell, to
a maximum of +1 per 3 caster levels. If the spell's target is a gnome, the maximum bonus is equal to
+1 per 2 caster levels.
