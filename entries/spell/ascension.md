+++
id = "ref/spell/ascension"
kind = "spell"
title = "Ascension"
source_ids = ["mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ascension", path = "json/spells.json" },
]
[[sources]]
publication = "mythic-adventures"
page = "113"

[fields]
kind = "spell"
school = "universal"
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Cleric", level = 9 },
  { class = "Druid", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 hour"
components = "V, S, M (10,000 gp in rare herbs, gems, and other exotic materials), F (minor artifact)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one non-mythic creature/3 levels" },
]
duration = "2 hours/level; see text"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: universal
Level: 9: Arcanist, Cleric, Druid, Oracle, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 hour
Components: V, S, M (10,000 gp in rare herbs, gems, and other exotic materials), F (minor artifact)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 2 hours/level; see text
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one non-mythic creature/3 levels
:::

You imbue a number of creatures with mythic power, granting each of them 1st tier in a mythic path
of its choice. The creatures immediately gain the benefits of their chosen paths. Divide the
duration evenly among all targets.

The targets retain their mythic tier only while they're within 100 feet of the spell's focus
component. A target that goes outside this range loses its mythic tier, but instantly regains it if
it moves into range again. If the focus component is destroyed while the spell is in effect, the
spell immediately ends and all targets gain 1d4 permanent negative levels.
