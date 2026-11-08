+++
id = "ref/spell/secret-coffer"
kind = "spell"
title = "Secret Coffer"
source_ids = ["core-rulebook", "black-markets", "heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "secret_coffer", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/secret-chest" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, F (the chest and its replica)"
range = "see text"
effects = [
  { label = "Target", value = "one chest and up to 1 cu. ft. of goods/caster level" },
]
duration = "60 days or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Arcanist, Mesmerist, Occultist, Psychic, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 10 minutes
Components: V, S, F (the chest and its replica)
Range: see text
Duration: 60 days or until discharged
Saving throw: none
Spell resistance: no
Target: one chest and up to 1 cu. ft. of goods/caster level
Subschool: Summoning
:::

### Secret Coffer

**Sources:** Black Markets pg 31, Heroes of the Streets pg 31

This spell functions like [secret chest](ref/spell/secret-chest), except the coffer is only 1 foot
square and can contain only 1 cubic foot of goods, and the container can remain safely hidden on the
Ethereal Plane for only 14 days before it risks becoming lost. The spell automatically fails if a
living creature enters the coffer. The coffer used as a focus for secret coffer must cost at least
500 gp, and its replica costs 5 gp.
