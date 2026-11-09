+++
id = "ref/spell/instant-summons-greater"
kind = "spell"
title = "Greater Instant Summons"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "instant_summons_greater", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/instant-summons" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "217"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, M (sapphires worth 1,000 gp each)"
range = "see text"
effects = [
  { label = "Target", value = "up to one object per 3 caster levels, each weighing 10 lbs. or less whose longest dimension is 6 ft. or less" },
]
duration = "permanent until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 8: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (sapphires worth 1,000 gp each)
Range: see text
Target: up to one object per 3 caster levels, each weighing 10 lbs. or less whose longest dimension is 6 ft. or less
Duration: permanent until discharged
Saving throw: none
Spell resistance: no
Subschool: Summoning
:::

### Greater Instant Summons

This spell functions as [instant summons](ref/spell/instant-summons), except that you can target
multiple objects. You must use a separate sapphire worth 1,000 gp for each one. For each item you
target, you can touch a creature, granting that creature the ability to speak the special word for
that item (each item has its own special word) while crushing the matched gem to call the item to
hand. Only you or the touched creature can activate the gem or see the arcane mark upon it.
