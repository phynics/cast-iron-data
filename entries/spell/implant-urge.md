+++
id = "ref/spell/implant-urge"
kind = "spell"
title = "Implant Urge"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "implant_urge", path = "json/spells14.json" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "60"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 hour/level"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Arcanist, Bard, Medium, Mesmerist, Skald, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level
Saving throw: Will partial
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

You make the target unconsciously desire a goal you define when you cast this spell. The DC of any
Diplomacy check to ask the target to act in a way that it believes will lead it toward that goal
decreases by 5. The target takes a -2 penalty on saving throws against mind-affecting effects that
compel it to act in a way that it believes will lead it toward that goal. Spells that reveal the
target's goals or thoughts reveal the implanted urge as the target's most important goal and the
target does not register as thinking of anything else as long as it is presented with the focus of
its urge or a way to move toward its goal. Anyone studying the target's thoughts can notice the
implanted nature of this urge with a successful caster level check.
