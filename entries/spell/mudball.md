+++
id = "ref/spell/mudball"
kind = "spell"
title = "Mudball"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mudball", path = "json/spells7.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "119"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["earth"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "single fist-sized blob of sticky mud" },
]
duration = "instantaneous"
saving_throw = "Reflex negates, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Arcanist, Bloodrager, Druid, Hunter, Magus, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Reflex negates, see text
Spell resistance: no
Effect: single fist-sized blob of sticky mud
Subschool: Creation
Descriptors: earth
:::

> _[Goblins](ref/race/goblin) have access to the following spell._

When you cast this spell, you conjure a single ball of sticky mud and launch it at an enemy's face
as a ranged touch attack. If the mudball hits, the target is blinded. Each round at the beginning of
its turn, a creature blinded by this spell can attempt a Reflex saving throw to shake off the mud,
ending the effect. The mudball can also be wiped off by the creature affected by it or by a creature
adjacent to the creature affected by it as a standard action.
