+++
id = "ref/spell/rags-to-riches"
kind = "spell"
title = "Rags to Riches"
aon = "SpellDisplay.aspx?ItemName=Rags%20to%20Riches"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rags_to_riches", path = "json/spells8.json" },
]
[[sources]]
publication = "arcane-anthology"
page = "21"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 4 },
  { class = "Investigator", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a bit of burlap wrapped over a copper coin)"
range = "touch"
effects = [
  { label = "Target", value = "1 weapon, suit or armor, shield, tool, or skill kit touched/5 levels" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates (object)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Bard, Investigator, Medium, Occultist, Skald\
4: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a bit of burlap wrapped over a copper coin)
Range: touch
Duration: 10 minutes/level
Saving throw: Fortitude negates (object)
Spell resistance: no
Target: 1 weapon, suit or armor, shield, tool, or skill kit touched/5 levels
:::

The target object is enhanced to function as a masterwork item. In addition to any bonuses for the
masterwork quality, the object gains other bonuses. Skill kits and other equipment add an additional
+1 insight bonus for every 4 caster levels you possess to skill checks made with them that already
receive a bonus from the skill kit. Armor and weapons gain temporary hit points equal to your caster
level. If the object already has an enhancement bonus, this bonus increases by 1. If the object of
the spell has [hardness](ref/umr/hardness), that hardness increases by 5.
