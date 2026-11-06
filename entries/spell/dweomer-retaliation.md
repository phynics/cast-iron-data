+++
id = "ref/spell/dweomer-retaliation"
kind = "spell"
title = "Dweomer Retaliation"
source_ids = ["cheliax-empire-of-devils"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dweomer_retaliation", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 immediate action"
components = "V"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "one creature you counterspelled since your last turn" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Arcanist, Sorcerer, Wizard
Casting time: 1 immediate action
Components: V
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: one creature you counterspelled since your last turn
:::

**Sources:** Cheliax, Empire of Devils pg 22

You may only cast this spell immediately after successfully counterspelling an opponent. Drawing
upon the residual energy of the countered spells, you gain a number of temporary hit points equal to
the level of the countered spell plus your Charisma or Intelligence modifier (for sorcerers and
wizards, respectively); your counterspelled opponent takes damage equal to this amount.

If the countered spell was at least 4th level, you and your opponent make opposed
[concentration](ref/rule/concentration) checks. If you beat your opponent by 10 or more, you retain
this spell (or its spell slot, if you are a sorcerer) as if you had not cast it.
