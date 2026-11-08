+++
id = "ref/spell/suns-disdain"
kind = "spell"
title = "Sun's Disdain"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "suns_disdain", path = "json/spells16.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a piece of glass)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Bloodrager, Cleric, Inquisitor, Oracle, Shaman, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a piece of glass)
Range: touch
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
Descriptors: curse
:::

**Sources:** Adventurer's Guide pg 17

You alter a creature so the touch of the sun is hostile to it. The cursed creature gains light
blindness and is blinded for 1 round if exposed to bright light, such as sunlight or the
[daylight](ref/spell/daylight) spell. The cursed creature is dazzled as long as it remains in areas
of bright light, and it is treated as being particularly susceptible to sunlight for the purposes of
resolving spells like [searing light](ref/spell/searing-light), [sunbeam](ref/spell/sunbeam), and
[sunburst](ref/spell/sunburst).
