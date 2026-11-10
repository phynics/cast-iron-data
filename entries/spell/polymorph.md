+++
id = "ref/spell/polymorph"
kind = "spell"
title = "Polymorph"
aon = "SpellDisplay.aspx?ItemName=Polymorph"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "polymorph", path = "json/spells7.json" },
]
[[sources]]
publication = "core-rulebook"
page = "323"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Adept", level = 4 },
  { class = "Alchemist", level = 5 },
  { class = "Arcanist", level = 5 },
  { class = "Investigator", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of the creature whose form you choose)"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Adept\
5: Alchemist, Arcanist, Investigator, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you choose)
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: living creature touched
Subschool: Polymorph
:::

This spell transforms a willing creature into an animal, humanoid or elemental of your choosing; the
spell has no effect on unwilling creatures, nor can the creature being targeted by this spell
influence the new form assumed (apart from conveying its wishes, if any, to you verbally).

If you use this spell to cause the target to take on the form of an animal or magical beast, the
spell functions as [beast shape II](ref/spell/beast-shape-2). If the form is that of an elemental,
the spell functions as [elemental body I](ref/spell/elemental-body-1). If the form is that of a
humanoid, the spell functions as [alter self](ref/spell/alter-self). The subject may choose to
resume its normal form as a full-round action; doing so ends the spell for that subject.
