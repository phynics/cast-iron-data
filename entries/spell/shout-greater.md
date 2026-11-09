+++
id = "ref/spell/shout-greater"
kind = "spell"
title = "Greater Shout"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shout_greater", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/shout" },
]
[[sources]]
publication = "core-rulebook"
page = "343"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Bard", level = 6 },
  { class = "Elementalist Wizard", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, F (a metal or ivory horn)"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial or Reflex negates (object); see text"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Bard, Skald\
8: Arcanist, Elementalist Wizard, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a metal or ivory horn)
Range: 60 ft.
Area: cone-shaped burst
Duration: instantaneous
Saving throw: Fortitude partial or Reflex negates (object); see text
Spell resistance: yes (object)
Descriptors: sonic
:::

### Greater Shout

This spell functions like [shout](ref/spell/shout), except that the cone deals 10d6 points of sonic
damage (or 1d6 points of sonic damage per caster level, maximum 20d6, against exposed brittle or
crystalline objects or crystalline creatures). It also causes creatures to be stunned for 1 round
and deafened for 4d6 rounds. A creature in the area of the cone can negate the stunning and halve
both the damage and the duration of the deafness with a successful Fortitude save. A creature
holding vulnerable objects can attempt a Reflex save to negate the damage to those objects.
