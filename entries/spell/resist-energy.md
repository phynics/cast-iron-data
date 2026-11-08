+++
id = "ref/spell/resist-energy"
kind = "spell"
title = "Resist Energy"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "resist_energy", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Adept", level = 2 },
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Hunter, Ranger\
2: Adept, Alchemist, Arcanist, Bloodrager, Cleric, Druid, Inquisitor, Investigator, Occultist, Oracle, Paladin, Psychic, Shaman, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 10 minutes/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

**Sources:** PRPG Core Rulebook pg 334

This abjuration grants a creature limited protection from damage of whichever one of five energy
types you select: acid, cold, electricity, fire, or sonic. The subject gains resist energy 10
against the energy type chosen, meaning that each time the creature is subjected to such damage
(whether from a natural or magical source), that damage is reduced by 10 points before being applied
to the creature's hit points. The value of the energy resistance granted increases to 20 points at
7th level and to a maximum of 30 points at 11th level. The spell protects the recipient's equipment
as well.

Resist energy absorbs only damage. The subject could still suffer unfortunate side effects.

Resist energy overlaps (and does not stack with)
[protection from energy](ref/spell/protection-from-energy). If a character is warded by protection
from energy and resist energy, the protection spell absorbs damage until its power is exhausted.
