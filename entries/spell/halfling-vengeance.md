+++
id = "ref/spell/halfling-vengeance"
kind = "spell"
title = "Halfling Vengeance"
aon = "SpellDisplay.aspx?ItemName=Halfling%20Vengeance"
source_ids = ["pathfinder-131-the-reapers-right-hand"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "halfling_vengeance", path = "json/spells5.json" },
]
[[sources]]
publication = "pathfinder-131-the-reapers-right-hand"
page = "72"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one Small or smaller creature touched" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Antipaladin\
2: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one Small or smaller creature touched
:::

You grant the touched target the ability to ascertain the weaknesses of foes. The target deals an
additional 1d6 points of precision damage on successful attacks with daggers or slings against foes
within 30 feet, as long as the attacked foe is denied its Dexterity bonus to Armor Class or is
flanked by the target. This additional damage increases by 1d6 for every 4 caster levels you have
beyond 3rd, to a maximum of 5d6 at 19th level. This bonus damage is precision damage and stacks with
other sources of precision damage, such as sneak attack. This bonus damage is not multiplied on a
critical hit.

Once per round on a successful attack that deals this precision damage, the target can choose to
forgo 2d6 points of precision damage (either granted by this spell or from other sources of
precision damage, such as sneak attack) to inflict one of the following conditions on the attacked
foe for 1 round:

- The attacked foe can't make attacks of opportunity against creatures smaller than it.
- The attacked foe is denied its Dexterity bonus to Armor Class against attacks made with daggers or
  slings.
- The attacked foe takes a -2 penalty on attacks against creatures smaller than it.
- The attacked foe can't take 5-foot steps.

A creature can benefit from only one halfling vengeance spell at a time.
