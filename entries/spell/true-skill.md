+++
id = "ref/spell/true-skill"
kind = "spell"
title = "True Skill"
aon = "SpellDisplay.aspx?ItemName=True%20Skill"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "true_skill", path = "json/spells10.json" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "63"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Alchemist, Arcanist, Bard, Investigator, Magus, Medium, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
:::

When faced with an important situation, you grant yourself a magical edge to ensure your success.
When casting this spell, select one skill for which you can attempt a skill check. The next time you
attempt a skill check using the selected skill (before the spell's duration ends), you gain an
insight bonus on the check equal to 1/2 your caster level (minimum 1).
