+++
id = "ref/spell/artificers-curse"
kind = "spell"
title = "Artificer's Curse"
aon = "SpellDisplay.aspx?ItemName=Artificer%27s%20Curse"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "artificers_curse", path = "json/spells.json" },
]
[[sources]]
publication = "arcane-anthology"
page = "19"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 7 },
  { class = "Inquisitor", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a blank scroll or page from a spellbook)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 magical item" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (object)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Bard, Inquisitor, Occultist, Skald\
7: Arcanist, Cleric, Oracle, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a blank scroll or page from a spellbook)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Will negates (object)
Spell resistance: yes
Target: 1 magical item
:::

You temporarily suppress the most powerful qualities of a magical item. This item can be any object
you suspect bears a magical enchantment, but if the targeted item is not magical, your spell has no
effect. The spell reduces the object's caster level by an amount equal to your caster level, to a
minimum of 0. If the item grants a competence, deflection, enhancement, insight, luck, morale,
natural armor, profane, resistance, or sacred bonus, the bonus is reduced by 1 for every 4 caster
levels the item loses. If the item's caster level is reduced to 0, all its magic qualities are
suppressed (as if dispelled) for the duration of the spell. This spell has no effect on artifacts.
