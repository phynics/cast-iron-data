+++
id = "ref/spell/innocuous-shape"
kind = "spell"
title = "Innocuous Shape"
aon = "SpellDisplay.aspx?ItemName=Innocuous%20Shape"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "innocuous_shape", path = "json/spells14.json" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "25"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a handfull of dandelion seeds)"
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
Level: 4: Alchemist, Arcanist, Investigator, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a handfull of dandelion seeds)
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: living creature touched
Subschool: Polymorph
:::

This spell transforms a creature into a Medium or smaller animal or humanoid of no more than 1 Hit
Die. If you use this spell to cause the target to take on the form of an animal, the spell functions
as [beast shape II](ref/spell/beast-shape-2). If the form is that of a humanoid, the spell can
function as alter self, youthful appearance, or both, such that you can transform a creature into a
generic, youthful humanoid of any type.

Any creature that interacts with the target of this spell must succeed at a Will saving throw (using
the DC of the spell) or view the target in the most innocuous possible light. On a failed saving
throw, the creature views all of the target's actions as inoffensive and no cause for concern unless
the target becomes an obvious threat. The creature can otherwise act normally, and feels no
compunction to obey or ignore the target; it simply assumes none of the target's actions are
dangerous or malicious unless shown evidence that proves otherwise.
