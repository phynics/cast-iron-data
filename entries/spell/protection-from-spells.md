+++
id = "ref/spell/protection-from-spells"
kind = "spell"
title = "Protection from Spells"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "protection_from_spells", path = "json/spells15.json" },
]
[[sources]]
publication = "core-rulebook"
page = "328"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Summoner", level = 6 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, M (diamond worth 500 gp), F (One 1,000 gp diamond per target. Each subject must carry the gem for the duration of the spell. If a subject loses the gem, the spell ceases to affect him.)"
range = "touch"
effects = [
  { label = "Targets", value = "up to one creature touched per four levels" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Summoner\
8: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (diamond worth 500 gp), F (One 1,000 gp diamond per target. Each subject must carry the gem for the duration of the spell. If a subject loses the gem, the spell ceases to affect him.)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Targets: up to one creature touched per four levels
:::

The subject gains a +8 resistance bonus on saving throws against spells and
[spell-like abilities](ref/umr/spell-like-abilities) (but not against supernatural and extraordinary
abilities).
