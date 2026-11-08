+++
id = "ref/spell/illusion-of-treachery"
kind = "spell"
title = "Illusion of Treachery"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "illusion_of_treachery", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "S, F (a tiny marionette)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level (D)"
saving_throw = "Will disbelief"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Antipaladin, Mesmerist\
4: Arcanist, Magus, Occultist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: S, F (a tiny marionette)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will disbelief
Spell resistance: yes
Target: one creature
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** Ultimate Intrigue pg 216

You create an illusion that takes the same space as a foe and mimics its movements perfectly.
Whenever you cast a spell or throw a weapon, the illusion ceases mimicking the target's actions just
long enough to make it look like the target cast the spell or threw the weapon simultaneously with
you, such that witnesses who can see both you and the target can't tell with certainty who truly
cast the spell or threw the weapon. Witnesses who can see only the target see it as the only
apparent source. The subject of this spell doesn't provoke attacks of opportunity from these
illusory actions. Each target of the attack or spell counts as interacting with the illusion and
thus receives a save to disbelieve.
