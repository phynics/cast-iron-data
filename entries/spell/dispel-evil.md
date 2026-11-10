+++
id = "ref/spell/dispel-evil"
kind = "spell"
title = "Dispel Evil"
aon = "SpellDisplay.aspx?ItemName=Dispel%20Evil"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dispel_evil", path = "json/spells13.json" },
]
[[sources]]
publication = "core-rulebook"
page = "271"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["good"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Paladin", level = 4 },
  { class = "Shaman", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target or Targets", value = "you and a touched evil creature from another plane, or you and an enchantment or evil spell on a touched creature or object" },
]
duration = "1 round/level or until discharged, whichever comes first"
saving_throw = "see text"
spell_resistance = "see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Paladin\
5: Cleric, Inquisitor, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 round/level or until discharged, whichever comes first
Saving throw: see text
Spell resistance: see text
Target or Targets: you and a touched evil creature from another plane, or you and an enchantment or evil spell on a touched creature or object
Descriptors: good
:::

Shimmering, white holy energy surrounds you. This energy has three effects.

First, you gain a +4 deflection bonus to AC against attacks by evil creatures.

Second, on making a successful melee touch attack against an evil creature from another plane, you
can choose to drive that creature back to its home plane. The creature can negate the effects with a
successful Will save ([spell resistance](ref/rule/spell-resistance) applies). This use discharges
and ends the spell.

Third, with a touch you can automatically dispel any one enchantment spell cast by an evil creature
or any one evil spell. Spells that can't be dispelled by [dispel magic](ref/spell/dispel-magic) also
can't be dispelled by dispel evil. Saving throws and [spell resistance](ref/rule/spell-resistance)
do not apply to this effect. This use discharges and ends the spell.
