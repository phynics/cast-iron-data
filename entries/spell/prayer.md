+++
id = "ref/spell/prayer"
kind = "spell"
title = "Prayer"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "prayer", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "40 ft."
effects = [
  { label = "Area", value = "all allies and foes within a 40-ft.-radius burst centered on you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Cleric, Inquisitor, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: 40 ft.
Duration: 1 round/level
Saving throw: none
Spell resistance: yes
Area: all allies and foes within a 40-ft.-radius burst centered on you
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 324

You bring special favor upon yourself and your allies while bringing disfavor to your enemies. You
and each of your allies gain a +1 luck bonus on attack rolls, weapon damage rolls, saves, and skill
checks, while each of your foes takes a -1 penalty on such rolls.

### Mythic Prayer

**Sources:** Mythic Adventures pg 104\
The spell's luck bonus increases to +2, and the penalty for enemies changes to -2. When you cast the
spell, your affected allies heal an amount of hit point damage equal to double your tier, and
affected enemies take an amount of damage equal to double your tier.
