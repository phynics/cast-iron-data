+++
id = "ref/spell/untold-wonder"
kind = "spell"
title = "Untold Wonder"
source_ids = ["heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "untold_wonder", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Mesmerist", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Paladin", level = 3 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Paladin\
4: Bard, Mesmerist, Skald\
5: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Heroes from the Fringe pg 19

You fill the target's mind with childlike wonder, allowing that creature to marvel at things that
would be debilitating to others. Penalties that the target would take as a result of an emotion
effect are instead treated as morale bonuses equal to half the penalty's value (for example, if the
target were affected by a [crushing despair](ref/spell/crushing-despair) spell, she would gain a +1
morale bonus on attack rolls, saving throws, ability checks, skill checks, and weapon damage rolls,
instead of the spell's normal effect). Furthermore, morale bonuses she gains from other sources are
increased by 1. Finally, the target gains a +2 bonus on saving throws to resist spells of the
pattern subschool, as her childlike wonder allows her to marvel at the beauty of such effects
without being overwhelmed by them.
