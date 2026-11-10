+++
id = "ref/spell/arcane-reinforcement"
kind = "spell"
title = "Arcane Reinforcement"
aon = "SpellDisplay.aspx?ItemName=Arcane%20Reinforcement"
source_ids = ["faction-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_reinforcement", path = "json/spells.json" },
]
[[sources]]
publication = "faction-guide"
page = "60"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 round"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "concentration (up to 8 hours)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 round
Components: V, S
Range: personal
Duration: concentration (up to 8 hours)
Saving throw: none
Spell resistance: no
Target: you
:::

You cast this spell as you begin crafting an item using a Craft skill, and add your Spellcraft ranks
to Craft checks made to create that item. As part of concentrating on the spell, you must continue
chanting the verbal components, pausing at most for a few seconds at a time to speak, chew, and so
on. If the crafting takes more than 1 day to complete, you must cast the spell each day to gain its
benefit.

This spell originated among wizards of the Arcanamirium, though the
[Pathfinder Society](ref/rule/aff-scholars) also uses it.
