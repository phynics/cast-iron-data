+++
id = "ref/spell/nexs-secret-workshop"
kind = "spell"
title = "Nex's Secret Workshop"
source_ids = ["core-rulebook", "inner-sea-intrigue", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nexs_secret_workshop", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/nondetection" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Hunter", level = 4 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Ranger", level = 4 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (diamond dust worth 50 gp)"
range = "touch"
effects = [
  { label = "Target", value = "creature or object touched" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Medium\
3: Alchemist, Antipaladin, Arcanist, Inquisitor, Investigator, Mesmerist, Occultist, Psychic, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Wizard\
4: Hunter, Ranger
Casting time: 1 standard action
Components: V, S, M (diamond dust worth 50 gp)
Range: touch
Duration: 1 hour/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: creature or object touched
:::

## Nondetection

**Sources:** PRPG Core Rulebook pg 317

The warded creature or object becomes difficult to detect by divination spells such as
clairaudience/clairvoyance, locate object, and detect spells. Nondetection also prevents location by
such magic items as crystal balls. If a divination is attempted against the warded creature or item,
the caster of the divination must succeed on a caster level check (1d20 + caster level) against a DC
of 11 + the caster level of the spellcaster who cast nondetection. If you cast nondetection on
yourself or on an item currently in your possession, the DC is 15 + your caster level.

If cast on a creature, nondetection wards the creature's gear as well as the creature itself.

### Nex's Secret Workshop

**Sources:** Inner Sea Intrigue pg 60

Designed to protect a large number of items from rivals of the Arclords of Nex, this spell functions
as [nondetection](ref/spell/nondetection) except as noted above. You can exclude any creatures or
objects in the spell's range when casting this spell, if you wish.

### Communal Nondetection

**Sources:** Ultimate Combat pg 238

This spell functions like nondetection, except you divide the duration in 1-hour increments among
the creatures or objects touched.
