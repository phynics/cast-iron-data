+++
id = "ref/spell/remove-curse"
kind = "spell"
title = "Remove Curse"
aon = "SpellDisplay.aspx?ItemName=Remove%20Curse"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "remove_curse", path = "json/spells8.json" },
]
[[sources]]
publication = "core-rulebook"
page = "332"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Adept", level = 3 },
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature or object touched" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Adept, Alchemist, Bard, Cleric, Inquisitor, Investigator, Medium, Mesmerist, Oracle, Paladin, Shaman, Skald, Warpriest, Witch\
4: Arcanist, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature or object touched
:::

Remove curse can remove all curses on an object or a creature. If the target is a creature, you must
make a caster level check (1d20 + caster level) against the DC of each curse affecting the target.
Success means that the curse is removed. Remove curse does not remove the curse from a cursed
shield, weapon, or suit of armor, although a successful caster level check enables the creature
afflicted with any such cursed item to remove and get rid of it.

Remove curse counters and dispels [bestow curse](ref/spell/bestow-curse).
