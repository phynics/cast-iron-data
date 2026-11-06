+++
id = "ref/spell/mud-buddy"
kind = "spell"
title = "Mud Buddy"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mud_buddy", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (1 pint of water)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "5 cubic feet of earth or mud" },
]
duration = "1 hour/level (d) (see text)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Druid, Hunter, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (1 pint of water)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level (d) (see text)
Saving throw: none
Spell resistance: no
Target: 5 cubic feet of earth or mud
Subschool: Creation
:::

**Sources:** Monster Codex pg 105

You create a Small minion out of mud, and it obeys your commands. The mud buddy has AC 12, 10 hit
points, Strength 5, and a speed of 30 feet. It can perform any tasks an unseen servant can, plus any
similar tasks its Strength allows (it's able to lift up to 50 pounds), but instead of walking on
water, it gains a swim speed of 30 feet.

You can command a mud buddy to move up to 5 feet and trip an opponent (CMB = your caster level +
your spellcasting ability score modifier). After the trip attempt is resolved, the spell ends.

When the spell ends, the mud buddy reverts to a patch of wet earth.
