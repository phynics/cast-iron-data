+++
id = "ref/spell/ferment"
kind = "spell"
title = "Ferment"
aon = "SpellDisplay.aspx?ItemName=Ferment"
source_ids = ["inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ferment", path = "json/spells4.json" },
]
[[sources]]
publication = "inner-sea-temples"
page = "23"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of ale, mead, or wine)"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Alchemist, Arcanist, Bard, Cleric, Druid, Hunter, Investigator, Oracle, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of ale, mead, or wine)
Range: touch
Duration: 10 minutes/level
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Target: object touched
:::

This spell temporarily imbues a potable liquid (including elixirs, extracts, potions, and poisons)
with an intoxicant. The caster must succeed at a caster level check in order to affect magic liquids
and poisons (DC = 10 + item level for magic liquids, DC equal to the poison's save DC for a poison);
otherwise, the spell fails. If the caster succeeds, the liquid also assumes a flavor according to
what the caster desires, but the effect on the imbiber is the same. An imbiber of a liquid affected
by ferment must succeed at a Fortitude saving throw at the spell's save DC or take a -2 penalty on
attack rolls, saves, ability checks, and skill checks for the remaining duration of the spell.
Additionally, the DC of any skill check to identify a magic liquid or poison under the effects of
this spell increases by 5.
