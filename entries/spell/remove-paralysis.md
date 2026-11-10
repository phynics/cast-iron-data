+++
id = "ref/spell/remove-paralysis"
kind = "spell"
title = "Remove Paralysis"
aon = "SpellDisplay.aspx?ItemName=Remove%20Paralysis"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "remove_paralysis", path = "json/spells8.json" },
]
[[sources]]
publication = "core-rulebook"
page = "332"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "up to four creatures, no two of which can be more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Cleric, Inquisitor, Oracle, Paladin, Shaman, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Targets: up to four creatures, no two of which can be more than 30 ft. apart
Subschool: Healing
:::

You can free one or more creatures from the effects of temporary paralysis or related magic,
including spells and effects that cause a creature to gain the staggered condition. If the spell is
cast on one creature, the paralysis is negated. If cast on two creatures, each receives another save
with a +4 resistance bonus against the effect that afflicts it. If cast on three or four creatures,
each receives another save with a +2 resistance bonus.

The spell does not restore ability scores reduced by penalties, damage, or drain.
