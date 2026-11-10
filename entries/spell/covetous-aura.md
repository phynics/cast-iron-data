+++
id = "ref/spell/covetous-aura"
kind = "spell"
title = "Covetous Aura"
aon = "SpellDisplay.aspx?ItemName=Covetous%20Aura"
source_ids = ["rise-of-the-runelords-anniversary-edition", "pathfinder-5-sins-of-the-saviors", "inner-sea-world-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "covetous_aura", path = "json/spells12.json" },
]
[[sources]]
publication = "rise-of-the-runelords-anniversary-edition"
page = "418"
[[sources]]
publication = "pathfinder-5-sins-of-the-saviors"
page = "58"
[[sources]]
publication = "inner-sea-world-guide"
page = "294"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 round"
components = "V, S"
range = "personal"
effects = [
  { label = "Area", value = "25-ft.-radius emanation centered on you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 5: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Area: 25-ft.-radius emanation centered on you
:::

Anytime a harmless (so noted by a spell's saving throw description) spell of 3rd level or lower is
cast within a covetous aura's area of effect, you may choose to immediately gain the benefit of that
spell as if it had also targeted you. The intended target still gains the effect of the spell. You
gain the benefits of this duplicated spell only if the caster is in range of the covetous aura. Each
time a covetous aura duplicates a spell effect, the remaining duration of the covetous aura is
reduced by a number of rounds equal to the spell level of the spell effect that is duplicated.
