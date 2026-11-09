+++
id = "ref/spell/positive-pulse-greater"
kind = "spell"
title = "Greater Positive Pulse"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "positive_pulse_greater", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/positive-pulse" },
]
[[sources]]
publication = "planar-adventures"
page = "43"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "5-ft.-radius burst" },
]
duration = "instantaneous plus 1 round (see text)"
saving_throw = "Will negates or Will negates (harmless); see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Arcanist, Cleric, Inquisitor, Oracle, Paladin, Shaman, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Area: 5-ft.-radius burst
Duration: instantaneous plus 1 round (see text)
Saving throw: Will negates or Will negates (harmless); see text
Spell resistance: yes
:::

### Greater Positive Pulse

This spell functions like [positive pulse](ref/spell/positive-pulse), except that the damage dealt
increases to 3d6 plus your caster level, and the bonus on saving throws increases to +8.
