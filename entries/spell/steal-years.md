+++
id = "ref/spell/steal-years"
kind = "spell"
title = "Steal Years"
aon = "SpellDisplay.aspx?ItemName=Steal%20Years"
source_ids = ["blood-of-the-night"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "steal_years", path = "json/spells9.json" },
]
[[sources]]
publication = "blood-of-the-night"
page = "30"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a handful of ash)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "24 hours"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Cleric, Druid, Hunter, Oracle, Red Mantis Assassin, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a handful of ash)
Range: touch
Duration: 24 hours
Saving throw: Fortitude negates
Spell resistance: yes
Target: creature touched
:::

You temporarily drain youth and vitality from the target and channel it into yourself. If the target
fails its Fortitude save, it physically ages 1d4 years per two caster levels (maximum 5d4), and you
decrease your age by the same number of years. If this changes the age category of you or the
target, only adjust physical ability scores. This effect cannot bring your age to lower than the
[minimum age of adulthood](ref/rule/age) for your race. This stolen youth does not actually change
your age or prolong your life; you will still die at your allotted time, no matter how youthful you
appear. Likewise, the spell does not add to the target's true age, and cannot make the target die of
old age.

When the spell ends, the sudden weight of aging makes you fatigued for 1d4 hours.
