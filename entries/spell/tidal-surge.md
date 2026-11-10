+++
id = "ref/spell/tidal-surge"
kind = "spell"
title = "Tidal Surge"
aon = "SpellDisplay.aspx?ItemName=Tidal%20Surge"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tidal_surge", path = "json/spells10.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "237"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["water"]
levels = [
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Shaman", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "30 ft. or 60 ft.; see text"
effects = [
  { label = "Area", value = "cone-shaped burst or line; see text" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Druid, Hunter, Shaman
Casting time: 1 standard action
Components: V, S
Range: 30 ft. or 60 ft.; see text
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: no
Area: cone-shaped burst or line; see text
Subschool: Creation
Descriptors: water
:::

If you cast tidal surge on land, you create an onrushing surge of water 10 feet high in a 30-foot
cone that deals 1d6 points of bludgeoning damage for every 2 caster levels you have (maximum 10d6 at
20th level) and extinguishes all nonmagical fires in the area. Magical fire effects in the area of a
tidal surge are affected as if you had cast [dispel magic](ref/spell/dispel-magic). In addition to
taking damage, creatures that fail their Reflex saves are pushed 1d4×5 feet away from you, and
Medium or smaller creatures are also knocked prone.

If you cast this spell in or on a body of water at least 30 feet across, you can shape the spell
either as the cone described above or as a 60-foot line. In either shape, the water deals 1d10
points of bludgeoning damage for every 2 caster levels you have in addition to pushing away
creatures that fail their Reflex saves.
