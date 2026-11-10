+++
id = "ref/spell/remove-sickness"
kind = "spell"
title = "Remove Sickness"
aon = "SpellDisplay.aspx?ItemName=Remove%20Sickness"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "remove_sickness", path = "json/spells8.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "234"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature" },
]
duration = "10 minutes/level; see text"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Cleric, Druid, Hunter, Mesmerist, Oracle, Spiritualist, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level; see text
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Targets: one creature
Subschool: Healing
:::

You quell feelings of illness and nausea in the target, giving it a +4 morale bonus on saving throws
against disease, nausea, and sickened effects. If the subject is already under the influence of one
of these effects when receiving the spell, that effect is suppressed for the duration of the spell.
