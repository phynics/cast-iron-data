+++
id = "ref/spell/callback"
kind = "spell"
title = "Callback"
source_ids = ["ultimate-wilderness", "familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "callback", path = "json/spells2.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "228"
[[sources]]
publication = "familiar-folio"
page = "22"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a crushed grasshopper)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "your familiar or spirit animal" },
]
duration = "10 minutes/level or until expended (see text)"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a crushed grasshopper)
Range: long (400 ft. + 40 ft./level)
Duration: 10 minutes/level or until expended (see text)
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: your familiar or spirit animal
Subschool: Teleportation
:::

If the target takes hit point damage while within range of this spell, it immediately teleports to
your space (or adjacent to your space) after the damage is applied. If the target is killed, its
corpse teleports instead. Optionally, you can specify a number of points of damage for your familiar
to take before the spell takes effect, but you must do so when the spell is cast. Once the familiar
has teleported back to you, the spell ends.
