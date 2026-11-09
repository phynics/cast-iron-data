+++
id = "ref/spell/handy-grapnel"
kind = "spell"
title = "Handy Grapnel"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "handy_grapnel", path = "json/spells5.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "215"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (an arrowhead)"
range = "touch"
effects = [
  { label = "Target", value = "one rope-like object, length up to 50 ft. + 5 ft./level" },
]
duration = "1 minute/level (D)"
saving_throw = "Fortitude negates (object)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Hunter, Inquisitor, Ranger, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (an arrowhead)
Range: touch
Duration: 1 minute/level (D)
Saving throw: Fortitude negates (object)
Spell resistance: no
Target: one rope-like object, length up to 50 ft. + 5 ft./level
:::

You cause the target rope to shrink and reshape itself into an arrow, bolt, or similar piece of
ammunition, which you can shoot at any Medium or larger object. With a successful attack roll
against an AC equal to 5 plus the [hardness](ref/umr/hardness) of the target object, the handy
grapnel strikes and embeds itself in that object with the strength of an iron grappling hook.

As a move action, you can command the rope to extend from the arrow. If you are within a distance
equal to the length of the rope and have a hand free, the end of the rope swings directly into your
hand. With another move action, you can command the handy grapnel to retract itself up to the
grappling hook, pulling up any creature or object supported by the rope at a speed of 50 feet per
round.

Once embedded, the rope can be used for climbing or any other purpose a rope could serve, and it can
bear up to 200 pounds per level of the caster at a time (maximum 1,000 pounds). If this weight limit
is exceeded, the handy grapnel comes loose and any creature or object supported by the rope falls.
