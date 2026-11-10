+++
id = "ref/spell/dispel-law"
kind = "spell"
title = "Dispel Law"
aon = "SpellDisplay.aspx?ItemName=Dispel%20Law"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dispel_law", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/dispel-evil" },
]
[[sources]]
publication = "core-rulebook"
page = "272"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["chaotic"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 5 },
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
Level: 4: Antipaladin\
5: Cleric, Inquisitor, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 round/level or until discharged, whichever comes first
Saving throw: see text
Spell resistance: see text
Target or Targets: you and a touched evil creature from another plane, or you and an enchantment or evil spell on a touched creature or object
Descriptors: chaotic
:::

This spell functions like [dispel evil](ref/spell/dispel-evil), except that you are surrounded by
flickering, yellow chaotic energy, and the spell affects lawful creatures and spells rather than
evil ones.
