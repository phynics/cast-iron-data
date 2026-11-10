+++
id = "ref/spell/ironbloom-sprouts"
kind = "spell"
title = "Ironbloom Sprouts"
source_ids = ["pathfinder-62-curse-of-the-ladys-light", "inner-sea-gods"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ironbloom_sprouts", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/goodberry" },
]
[[sources]]
publication = "pathfinder-62-curse-of-the-ladys-light"
page = "75"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF, M (1 gp worth of powdered iron)"
range = "touch"
effects = [
  { label = "Targets", value = "2d4 fresh mushrooms touched" },
]
duration = "1 day/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Cleric, Druid, Hunter, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF, M (1 gp worth of powdered iron)
Range: touch
Duration: 1 day/level
Saving throw: none
Spell resistance: yes
Targets: 2d4 fresh mushrooms touched
:::

This spell functions like [goodberry](ref/spell/goodberry), except as noted above and that it
transforms 2d4 mushrooms into magical ironbloom mushrooms rather than transforming common berries
into magical berries. Alternatively, you may create twice as many mushrooms, but each only has the
nourishment ability of a goodberry and not the healing properties.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
