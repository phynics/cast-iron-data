+++
id = "ref/spell/mindwipe"
kind = "spell"
title = "Mindwipe"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mindwipe", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous; see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Arcanist, Medium, Mesmerist, Occultist, Psychic, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous; see text
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Occult Adventures pg 178

You erase a portion of the target's mind and experiences, inflicting 2 temporary negative levels on
the target for 1 day per caster level. If the target is a spellcaster who must choose and prepare
spells in advance, each negative level imposed by mindwipe also causes the target to lose one
prepared spell from her highest level of spells known for each of her spellcasting classes for which
she must prepare spells. These lost spells are no longer considered known by the target until the
corresponding negative levels are removed.

If the target is a spontaneous spellcaster, each negative level inflicted by mindwipe causes her to
lose one spell slot of her highest level of spells for each spontaneous spellcasting class in which
she has levels and to lose knowledge of one random spell known of that level (or the next lowest
level if she has already lost knowledge of all spells known of that level, and so on). The target
cannot use the lost spell slots and spells known as long as the corresponding negative levels last.
When the target loses a spell known, the spell remains on her class list but she cannot prepare or
cast the spell.

If the negative levels from mindwipe cause the target's total number of negative levels to equal or
exceed her character level, instead of dying, she enters a catatonic state as long as the negative
levels from mindwipe continue to cause her total number of negative levels to equal or exceed her
character level.
