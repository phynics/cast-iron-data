+++
id = "ref/spell/prediction-of-failure"
kind = "spell"
title = "Prediction of Failure"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "prediction_of_failure", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "divination"
descriptors = ["curse", "fear", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent or 1 round/level (see text)"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 6: Occultist\
8: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent or 1 round/level (see text)
Saving throw: Will partial
Spell resistance: yes
Target: one creature
Descriptors: curse, fear, mind-affecting
:::

**Sources:** Ultimate Magic pg 232

You wrack the target's body and mind with the anguish and suffering of every bitter failure it will
ever experience, rendering it permanently shaken and sickened. A successful Will save reduces the
duration to 1 round per level. If the target is a spellcaster, failing this saving throw means it
also gains a random [minor spellblight](ref/rule/minor-spellblights).
