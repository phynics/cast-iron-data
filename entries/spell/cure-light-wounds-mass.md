+++
id = "ref/spell/cure-light-wounds-mass"
kind = "spell"
title = "Mass Cure Light Wounds"
aon = "SpellDisplay.aspx?ItemName=Cure%20Light%20Wounds%2C%20Mass"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cure_light_wounds_mass", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/cure-light-wounds" },
]
[[sources]]
publication = "core-rulebook"
page = "263"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Bard", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Inquisitor", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "Will half (harmless) or Will half; see text"
spell_resistance = "yes (harmless) or yes; see text"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Bard, Cleric, Inquisitor, Occultist, Oracle, Shaman, Skald, Warpriest\
6: Druid, Hunter, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will half (harmless) or Will half; see text
Spell resistance: yes (harmless) or yes; see text
Target: one creature/level, no two of which can be more than 30 ft. apart
Subschool: Healing
:::

You channel positive energy to cure 1d8 points of damage + 1 point per caster level (maximum +25) on
each selected creature. Like other cure spells, mass cure light wounds deals damage to undead in its
area rather than curing them. Each affected undead may attempt a Will save for half damage.
