+++
id = "ref/spell/wither-limb"
kind = "spell"
title = "Wither Limb"
aon = "SpellDisplay.aspx?ItemName=Wither%20Limb"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wither_limb", path = "json/spells16.json" },
]
[[sources]]
publication = "horror-adventures"
page = "131"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Arcanist, Cleric, Inquisitor, Oracle, Shaman, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Target: living creature touched
:::

You cause one limb of the target to shrivel and weaken. The target takes 2d6 points of damage. The
points are permanently lost until the target's limb is restored by [heal](ref/spell/heal),
[limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle),
[regenerate](ref/spell/regenerate), or [wish](ref/spell/wish). Wither limb affects only living
creatures of the humanoid or monstrous humanoid type, or similar bipedal creatures at the GM's
discretion. You choose the limb affected. This spell's effects stack, until all a target's arms and
legs (or equivalent limbs) are withered.

_Arm:_ The target looses the use of one arm, which might affect what weapons and shields it can use.
The creature must immediately drop all objects held in the withered limb, though it can shift a
two-handed weapon it is holding in both hands to a remaining arm as an immediate action. Worn
objects' gauntlets, rings, and magic items in the [wrist slot](ref/rule/magic-items-on-the-body)
remain. This prevents the creature from using two-weapon fighting, claw attacks from that arm, and
so on. If multiple castings of this spell wither all of a creature's arms, it can't manipulate
objects or cast spells requiring somatic components.

_Leg:_ The creature's movement speeds are halved, except for flying or other speeds that don't
involve its legs. If multiple castings of this spell wither all of a creature's legs, it can only
crawl at a speed of 5 feet each round.

_Wing:_ The creature loses access to any fly speed that depends on its wings if even a single wing
is withered.
