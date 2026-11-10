+++
id = "ref/spell/life-shield"
kind = "spell"
title = "Life Shield"
aon = "SpellDisplay.aspx?ItemName=Life%20Shield"
source_ids = ["undead-slayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "life_shield", path = "json/spells6.json" },
]
[[sources]]
publication = "undead-slayers-handbook"
page = "27"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 2 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Paladin\
3: Cleric, Druid, Hunter, Oracle, Warpriest
Casting time: 1 standard action
Components: S, DF
Range: personal
Duration: 1 minute/level or until discharged
Saving throw: none
Spell resistance: no
Target: you
Subschool: Healing
:::

You surround yourself with a positive energy field that damages undead opponents. Each time an
undead creature damages you with a melee attack, that creature takes an amount of positive energy
damage equal to half the damage it dealt to you. This damage is calculated after applying your
[damage reduction](ref/rule/damage-reduction), resistances, and other defenses. Once this spell has
dealt 5 points of damage per caster level (maximum 50), it is discharged.
