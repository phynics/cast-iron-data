+++
id = "ref/spell/bouncy-body"
kind = "spell"
title = "Bouncy Body"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bouncy_body", path = "json/spells2.json" },
]
[[sources]]
publication = "monster-codex"
page = "105"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Alchemist, Arcanist, Bloodrager, Investigator, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Target: creature touched
:::

The target's flesh becomes flexible and rubbery. It gains a +2 circumstance bonus on grapple combat
maneuver checks and Escape Artist checks, as well as to its CMD against combat maneuver checks to
grapple. Anytime the target would take falling damage, it treats falls as 20 feet shorter (minimum
0) for the purpose of determining damage. In addition, if the target falls against a hard surface,
it can attempt an Acrobatics check (DC = the distance fallen) to attempt to bounce upward; success
means the creature bounces upward half the distance fallen.
