+++
id = "ref/spell/guardian-armor"
kind = "spell"
title = "Guardian Armor"
aon = "SpellDisplay.aspx?ItemName=Guardian%20Armor"
source_ids = ["armor-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "guardian_armor", path = "json/spells5.json" },
]
[[sources]]
publication = "armor-masters-handbook"
page = "23"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 immediate action"
components = "V, S, F (armor worn)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one willing creature; see below" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Antipaladin, Arcanist, Bloodrager, Cleric, Inquisitor, Magus, Occultist, Oracle, Paladin, Sorcerer, Warpriest, Wizard
Casting time: 1 immediate action
Components: V, S, F (armor worn)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: one willing creature; see below
Subschool: Teleportation
:::

This spell teleports the suit of armor you are wearing off of your body and onto an ally within
range; the target must be the same size and general shape as you. This armor appears on the target's
body fully formed and properly donned, granting the creature the immediate benefit of its
protection. If the target of guardian armor was already wearing armor, the armor wearing it is
removed from the target's body and falls undamaged into an adjacent square.
