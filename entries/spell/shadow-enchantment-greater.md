+++
id = "ref/spell/shadow-enchantment-greater"
kind = "spell"
title = "Greater Shadow Enchantment"
source_ids = ["occult-realms"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_enchantment_greater", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/shadow-enchantment" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "see text"
effects = [
  { label = "Effect", value = "see text" },
]
duration = "see text"
saving_throw = "Will disbelief, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 6: Arcanist, Bard, Mesmerist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: see text
Effect: see text
Duration: see text
Saving throw: Will disbelief, see text
Spell resistance: yes
Subschool: Shadow
Descriptors: shadow
:::

### Greater Shadow Enchantment

**Sources:** Occult Realms pg 17

This spell functions like [shadow enchantment](ref/spell/shadow-enchantment), except that it enables
you to create partially real, illusory versions of psychic, sorcerer, or wizard enchantment spells
of 5th level or lower. If the spell is recognized as a greater shadow enchantment, it's only
three-fifths (60%) as effective.
