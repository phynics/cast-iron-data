+++
id = "ref/spell/die-for-your-master"
kind = "spell"
title = "Die for Your Master"
source_ids = ["ultimate-wilderness", "animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "die_for_your_master", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/bleed-for-your-master" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 immediate action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "your animal companion, familiar, or fiendish servant" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Antipaladin\
3: Arcanist, Druid, Hunter, Ranger, Sorcerer, Witch, Wizard
Casting time: 1 immediate action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: your animal companion, familiar, or fiendish servant
Subschool: Compulsion
Descriptors: mind-affecting
:::

### Die for Your Master

This spell functions as [Bleed for Your Master](ref/spell/bleed-for-your-master), but it allows your
companion or familiar to intercept any attack that targets you, including those that do not require
attack rolls (e.g. [chain lightning](ref/spell/chain-lightning),
[hold monster](ref/spell/hold-monster), and [magic missile](ref/spell/magic-missile)). Your
companion or familiar cannot intercept effects that do not affect creatures of its type (e.g.
[dominate person](ref/spell/dominate-person)).
