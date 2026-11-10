+++
id = "ref/spell/divine-power"
kind = "spell"
title = "Divine Power"
aon = "SpellDisplay.aspx?ItemName=Divine%20Power"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "divine_power", path = "json/spells13.json" },
]
[[sources]]
publication = "core-rulebook"
page = "273"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Cleric, Inquisitor, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
:::

Calling upon the divine power of your patron, you imbue yourself with strength and skill in combat.
You gain a +1 luck bonus on attack rolls, weapon damage rolls, Strength checks, and Strength-based
skill checks for every three caster levels you have (maximum +6). You also gain 1 temporary hit
point per caster level. Whenever you make a full-attack action, you can make an additional attack at
your full base attack bonus, plus any appropriate modifiers. This additional attack is not
cumulative with similar effects, such as haste or weapons with the speed special ability.
