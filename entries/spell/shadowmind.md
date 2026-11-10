+++
id = "ref/spell/shadowmind"
kind = "spell"
title = "Shadowmind"
aon = "SpellDisplay.aspx?ItemName=Shadowmind"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadowmind", path = "json/spells15.json" },
]
[[sources]]
publication = "blood-of-shadows"
page = "16"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 2 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a small square of black silk)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "up to one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Antipaladin, Inquisitor, Witch\
3: Arcanist, Cleric, Druid, Hunter, Mesmerist, Occultist, Oracle, Psychic, Shaman, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (a small square of black silk)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Target: up to one creature/level, no two of which can be more than 30 ft. apart
Subschool: Phantasm
:::

You dim your targets' perceptions of light and shadow, convincing them the space they occupy is
dark. Each creature that fails its save perceives the world around it as one light level darker than
its true illumination level. The spell does not change the light level outside of the targets'
perception, and does not create magical darkness. However, the spell creates an illusion of darkness
rather than actual darkness, so low-light and [darkvision](ref/rule/darkvision) don't allow a target
to see in the conditions created by the spell. Even targets that see normally through magical
darkness suffer a loss of vision from this spell.
