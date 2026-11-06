+++
id = "ref/spell/protection-from-energy-communal"
kind = "spell"
title = "Communal Protection from Energy"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "protection_from_energy_communal", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 min./level or until discharged"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Hunter, Ranger\
3: Alchemist, Arcanist, Bloodrager, Cleric, Druid, Inquisitor, Investigator, Occultist, Oracle, Psychic, Shaman, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 10 min./level or until discharged
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

## Protection from Energy

**Sources:** PRPG Core Rulebook pg 327

Protection from energy grants temporary immunity to the type of energy you specify when you cast it
(acid, cold, electricity, fire, or sonic). When the spell absorbs 12 points per caster level of
energy damage (to a maximum of 120 points at 10th level), it is discharged.

Protection from energy overlaps (and does not stack with) [resist energy](ref/spell/resist-energy).
If a character is warded by protection from energy and resist energy, the protection spell absorbs
damage until its power is exhausted.

### Communal Protection from Energy

**Sources:** Ultimate Combat pg 240

This spell functions like protection from energy, except you divide the duration in 10-minute
intervals among the creatures touched. Once the spell absorbs 12 points of energy damage per caster
level (maximum 120 points) for a subject, the spell's effects end for that subject.
