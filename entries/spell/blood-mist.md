+++
id = "ref/spell/blood-mist"
kind = "spell"
title = "Blood Mist"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blood_mist", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["poison"]
levels = [
  { class = "Druid", level = 8 },
  { class = "Shaman", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of dried red algae)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "60-ft. radius" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 8: Druid, Shaman
Casting time: 1 standard action
Components: V, S, M (a pinch of dried red algae)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level
Saving throw: Fortitude negates (see text)
Spell resistance: yes
Area: 60-ft. radius
Subschool: Creation
Descriptors: poison
:::

**Sources:** Ultimate Magic pg 209

This spell summons forth a misty cloud of rust-red toxic algae. Any creature within the mist is
coated by it, turning the creature the same reddish color. All targets within the mist gain
[concealment](ref/rule/concealment). Any creature within the mist must save or take 1d4 points of
Wisdom damage and become enraged, attacking any creatures it detects nearby (as the "attack nearest
creature" result of the confused condition). An enraged creature remains so as long as the spell is
in effect. A creature only needs to save once each time it is within the mist (though leaving and
returning requires another save).
