+++
id = "ref/spell/callback-greater"
kind = "spell"
title = "Greater Callback"
source_ids = ["ultimate-wilderness", "familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "callback_greater", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/callback" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a crushed grasshopper)"
range = "1 mile/level"
effects = [
  { label = "Target", value = "your familiar or spirit animal" },
]
duration = "1 hour/level or until expended"
saving_throw = "Fortitude negates"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Arcanist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a crushed grasshopper)
Range: 1 mile/level
Target: your familiar or spirit animal
Duration: 1 hour/level or until expended
Saving throw: Fortitude negates
Spell resistance: yes (harmless)
Subschool: Teleportation
:::

## Callback

**Sources:** Ultimate Wilderness pg 228, Familiar Folio pg 22

If the target takes hit point damage while within range of this spell, it immediately teleports to
your space (or adjacent to your space) after the damage is applied. If the target is killed, its
corpse teleports instead. Optionally, you can specify a number of points of damage for your familiar
to take before the spell takes effect, but you must do so when the spell is cast. Once the familiar
has teleported back to you, the spell ends.

### Greater Callback

**Sources:** Ultimate Wilderness pg 228

This spell functions as [callback](ref/spell/callback), except as noted above.
