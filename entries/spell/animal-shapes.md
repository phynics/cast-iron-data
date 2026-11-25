+++
id = "ref/spell/animal-shapes"
kind = "spell"
title = "Animal Shapes"
aon = "SpellDisplay.aspx?ItemName=Animal%20Shapes"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animal_shapes", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/beast-shape-3" },
]
[[sources]]
publication = "core-rulebook"
page = "241"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["polymorph"]
levels = [
  { class = "Druid", level = 8 },
  { class = "Shaman", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "up to one willing creature per level, all within 30 ft. of each other" },
]
duration = "1 hour/level (D)"
saving_throw = "none, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 8: Druid, Shaman
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level (D)
Saving throw: none, see text
Spell resistance: yes
Targets: up to one willing creature per level, all within 30 ft. of each other
Subschool: polymorph
:::

### Animal Shapes

As [beast shape III](ref/spell/beast-shape-3), except you change the form of up to one willing
creature per caster level into an animal of your choice; the spell has no effect on unwilling
creatures. All creatures must take the same kind of animal form. Recipients remain in the animal
form until the spell expires or until you dismiss it for all recipients. In addition, an individual
subject may choose to resume its normal form as a full-round action; doing so ends the spell for
that subject alone.
