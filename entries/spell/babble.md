+++
id = "ref/spell/babble"
kind = "spell"
title = "Babble"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "babble", path = "json/spells12.json" },
]
[[sources]]
publication = "occult-adventures"
page = "158"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature; see text" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Mesmerist, Skald\
3: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature; see text
Subschool: Compulsion
Descriptors: mind-affecting
:::

This spell causes the target to break into a fit of bizarre, uncontrollable babbling. The target
also becomes nauseated. If the target succeeds at its save, the effects end. If not, the creature
continues babbling and is nauseated for the entire duration.

Creatures within 30 feet of the subject that can hear the target's babbling must succeed at a Will
save or become fascinated for as long as the babbling persists. Once a creature's fascination ends,
it can't become fascinated by the same instance of babble again.

Creatures with an Intelligence score of 2 or lower aren't affected by this spell.
