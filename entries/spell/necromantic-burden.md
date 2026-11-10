+++
id = "ref/spell/necromantic-burden"
kind = "spell"
title = "Necromantic Burden"
source_ids = ["undead-slayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "necromantic_burden", path = "json/spells7.json" },
]
[[sources]]
publication = "undead-slayers-handbook"
page = "27"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 round"
components = "V, S, M/DF (a handful of knucklebones)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one undead creature" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Cleric, Oracle, Warpriest\
3: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S, M/DF (a handful of knucklebones)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level
Saving throw: Will negates
Spell resistance: yes
Target: one undead creature
:::

You make an undead creature more difficult for necromancers and clerics to control via effects such
as Command Undead or control undead. If the target fails its Will save, the target's effective
number of Hit Dice is doubled for the purposes of determining whether it remains under the control
of another creature. Regardless of the target's actual Hit Dice, its effective HD cannot exceed
twice your caster level. (For example, a 12th-level cleric could cast this spell to cause an undead
creature with 15 HD to instead effectively have 24 HD for the purpose of controlling it.)

If the targeted undead is under the control of another creature and this spell causes the target's
effective Hit Dice to exceed the controller's maximum capability, the target creature is immediately
freed from control. Any creature capable of controlling undead may attempt to control the target,
provided the target's effective HD won't cause the would-be controller to exceed its HD limit. The
target's former controller can attempt to regain control over the target by relinquishing command
over other creatures until its HD limit is no longer exceeded (or the former controller can wait
until the spell's duration expires to attempt this at the target's normal HD).
