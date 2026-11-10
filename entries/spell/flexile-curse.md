+++
id = "ref/spell/flexile-curse"
kind = "spell"
title = "Flexile Curse"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flexile_curse", path = "json/spells4.json" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "21"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Bard, Inquisitor, Witch\
5: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
Descriptors: curse
:::

You curse your target with a withering aura that degrades its armor and shield (if any). This
reduces the [hardness](ref/umr/hardness), armor bonus, and enhancement bonus of any armor or shield
worn by the target by 1. For every hour the target wears a suit of armor or a shield, the hardness,
armor bonus, and enhancement bonus are reduced by an additional 1. If the armor or shield's hardness
is reduced to 0, anytime the target of the curse is struck while wearing that item, there is a 20%
chance that it gains the broken condition. If the enhancement bonus of magic suit of armor or shield
is reduced to 0, the armor or shield loses any other special abilities it had.

If the target removes the suit of armor or shield (even if it's broken or has been drained of all
enhancement bonuses), the armor or shield regains its [hardness](ref/umr/hardness), armor bonus, and
enhancement bonus at the rate of 1 per 2 hours. A suit of armor or shield broken by this curse that
regains its full hardness ceases to be broken. A magic suit of armor or shield that lost its special
abilities regains them when its enhancement bonus is fully restored.
