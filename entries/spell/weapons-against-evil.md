+++
id = "ref/spell/weapons-against-evil"
kind = "spell"
title = "Weapons Against Evil"
aon = "SpellDisplay.aspx?ItemName=Weapons%20Against%20Evil"
source_ids = ["inner-sea-gods", "faiths-of-purity"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "weapons_against_evil", path = "json/spells11.json" },
]
[[sources]]
publication = "inner-sea-gods"
page = "245"
[[sources]]
publication = "faiths-of-purity"
page = "29"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one weapon/level, no two of which can be more than 20 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Cleric, Inquisitor, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Targets: one weapon/level, no two of which can be more than 20 ft. apart
:::

Each weapon this spell affects each shines with pale light that dimly illuminates a 5-foot square.
These weapons also ignore the DR of evil creatures that have DR 5 or lower, as long as the
[damage reduction](ref/rule/damage-reduction) is not DR/epic.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
