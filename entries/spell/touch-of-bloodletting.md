+++
id = "ref/spell/touch-of-bloodletting"
kind = "spell"
title = "Touch of Bloodletting"
source_ids = ["inner-sea-gods", "faiths-of-corruption"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "touch_of_bloodletting", path = "json/spells10.json" },
]
[[sources]]
publication = "inner-sea-gods"
page = "243"
[[sources]]
publication = "faiths-of-corruption"
page = "29"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Bloodrager, Cleric, Druid, Hunter, Oracle, Warpriest\
2: Antipaladin, Arcanist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: living creature touched
:::

This spell causes any existing wounds that the target possesses to bleed profusely. If the
creature's current total hit points are less than its maximum, this spell causes the creature to
take 1 point of bleed damage each round and become exhausted for the duration of the spell. A
successful DC 15 Heal check or any spell that cures hit point damage negates the effects of this
spell.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
