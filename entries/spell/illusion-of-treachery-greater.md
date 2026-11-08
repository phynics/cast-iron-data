+++
id = "ref/spell/illusion-of-treachery-greater"
kind = "spell"
title = "Greater Illusion of Treachery"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "illusion_of_treachery_greater", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/illusion-of-treachery" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "S, F (a tiny marionette)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "you and one creature" },
]
duration = "1 round/level (D)"
saving_throw = "Will disbelief"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Antipaladin, Mesmerist\
5: Occultist, Psychic\
6: Arcanist, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: S, F (a tiny marionette)
Range: close (25 ft. + 5 ft./2 levels)
Target: you and one creature
Duration: 1 round/level (D)
Saving throw: Will disbelief
Spell resistance: yes
Subschool: Glamer
Descriptors: glamer
:::

### Greater Illusion of Treachery

**Sources:** Ultimate Intrigue pg 217

This spell functions as [illusion of treachery](ref/spell/illusion-of-treachery) except that it also
conceals your own actions (as illusion of calm) and renders invisible all spell effects and ranged
attacks originating from you until they reach the attack's target (this doesn't cause the attack's
target to be unable to avoid the attack, as they still see the attack originating from the spell's
target).
