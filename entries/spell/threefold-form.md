+++
id = "ref/spell/threefold-form"
kind = "spell"
title = "Threefold Form"
source_ids = ["occult-adventures", "legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "threefold_form", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/bilocation" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "25"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one duplicate" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 8: Psychic\
9: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one duplicate
Subschool: Creation
:::

### Threefold Form

You pull forth idealized versions of yourself at various ages from your mind, splitting into three
copies of yourself. Threefold form functions as [bilocation](ref/spell/bilocation), except there are
three of you instead of two, and each of the three bodies is under the effect of threefold aspect
with a different idealized age. Other than the differences from threefold aspect, each body shares
all other effects with you, as normal for bilocation.
