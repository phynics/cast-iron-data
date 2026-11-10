+++
id = "ref/spell/elemental-bombardment"
kind = "spell"
title = "Elemental Bombardment"
aon = "SpellDisplay.aspx?ItemName=Elemental%20Bombardment"
source_ids = ["mythic-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elemental_bombardment", path = "json/spells4.json" },
]
[[sources]]
publication = "mythic-origins"
page = "14"

[fields]
kind = "spell"
school = "conjuration [see text]"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Druid", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 round"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Effect", value = "one or more summoned elementals" },
]
duration = "1 round/2 levels (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration \[see text\]
Level: 7: Arcanist, Druid, Sorcerer, Wizard
Casting time: 1 round
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: 1 round/2 levels (D)
Saving throw: none
Spell resistance: no
Effect: one or more summoned elementals
Subschool: Summoning
:::

You summon elementals from their elemental planes and hurl them onto your enemies with great force.
You must have line of effect to a point at least 60 feet above your intended targets and within the
spell's range. You can summon one greater elemental, two Huge elementals, four Large elementals, or
eight Medium elementals. You aim the elementals at targets within 60 feet of each other, no more
than one elemental per target.

Each elemental can strike only a single target, regardless of its size. When an elemental strikes a
target, it makes a single slam attack at its full attack bonus with a +4 circumstance bonus. The
elemental deals damage according to the table below. The type and amount of damage dealt varies by
the size and type of elemental (see the table). Some elementals inflict an additional special
ability upon successfully hitting a target; these additional special abilities are detailed in the
elemental's full stat block and are denoted with an asterisk (\*). Whether or not it hits, the
elemental takes bludgeoning damage according to its size. A summoned elemental acts on the same turn
that it lands, starting prone in the nearest available space adjacent to its target.

You must select one type of elemental to summon when casting this spell (see the table). When you
use a summoning spell to summon a creature with an elemental subtype, it is a spell of that type.

|Elemental Size|Damage|
| --- | --- |
|Medium|6d6|
|Large|8d6|
|Huge or larger|12d6|
|Elemental Type|Damage Type|
|Air|Half slashing, half electricity|
|Earth|Bludgeoning and earth mastery\*|
|Fire|Fire and burn\*|
|Ice|Half bludgeoning, half cold|
|Lightning|Electricity and metal mastery\*|
|Magma|Half bludgeoning, half fire|
|Mud|Bludgeoning and entrap\*|
|Water|Bludgeoning and drench\*|
