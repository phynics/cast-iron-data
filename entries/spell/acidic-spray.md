+++
id = "ref/spell/acidic-spray"
kind = "spell"
title = "Acidic Spray"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "acidic_spray", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["acid"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a vial of acid worth 10 gp)"
range = "60 ft."
effects = [
  { label = "Effect", value = "60-ft. line" },
]
duration = "instantaneous"
saving_throw = "Reflex partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Arcanist, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a vial of acid worth 10 gp)
Range: 60 ft.
Duration: instantaneous
Saving throw: Reflex partial (see text)
Spell resistance: yes
Effect: 60-ft. line
Subschool: Creation
Descriptors: acid
:::

**Sources:** Ultimate Magic pg 204

A spray of acid erupts from your outstretched hand, dealing 1d6 points of acid damage per caster
level (maximum 15d6) to each creature within its area (Reflex half). This acid continues to burn for
1 round, dealing 1d6 points of acid damage per two caster levels (maximum 7d6) to any creature that
failed its saving throw against the spell (a second Reflex save on the creature's turn negates this
additional damage).
