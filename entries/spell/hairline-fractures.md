+++
id = "ref/spell/hairline-fractures"
kind = "spell"
title = "Hairline Fractures"
source_ids = ["inner-sea-gods", "faiths-of-purity"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hairline_fractures", path = "json/spells5.json" },
]
[[sources]]
publication = "inner-sea-gods"
page = "235"
[[sources]]
publication = "faiths-of-purity"
page = "28"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth"]
levels = [
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a broken twig)"
range = "touch"
effects = [
  { label = "Target", value = "5-foot-square section of stone or a creature with the earth subtype" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Cleric, Druid, Hunter, Oracle, Shaman, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, M (a broken twig)
Range: touch
Duration: 1 round/level
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Target: 5-foot-square section of stone or a creature with the earth subtype
Descriptors: earth
:::

With a single touch, you create temporary hairline fractures in a piece of stone or a creature with
the earth subtype. If you cast this spell on a section of stone, you reduce its
[hardness](ref/umr/hardness) to 5 and its hit points to 10/inch of thickness. If you cast this spell
on a creature with the earth subtype, that creature takes a -2 penalty to AC for the spell's
duration. Make whole reverses this spell's effect.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
