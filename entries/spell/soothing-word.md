+++
id = "ref/spell/soothing-word"
kind = "spell"
title = "Soothing Word"
source_ids = ["gamemastery-condition-cards"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soothing_word", path = "json/spells9.json" },
]
[[sources]]
publication = "gamemastery-condition-cards"
page = "0"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 creature" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Cleric, Druid, Hunter, Inquisitor, Oracle, Paladin, Ranger, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: 1 creature
Subschool: Healing
:::

The target of this spell causes several conditions that he suffers from to be lessened in severity
by one step. If he is nauseated, he is instead sickened. If he is stunned, he is instead dazed. If
he is exhausted, he is fatigued. If he is frightened, he is shaken. If he is paralyzed, he is
staggered. The duration of the effect is unchanged; the effect is simply reduced to the lesser
version. This spell has no effect on conditions not listed above.
