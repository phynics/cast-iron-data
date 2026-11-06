+++
id = "ref/spell/stoneskin"
kind = "spell"
title = "Stoneskin"
source_ids = ["core-rulebook", "mythic-adventures", "potions-and-poisons", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stoneskin", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Adept", level = 4 },
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (granite and diamond dust worth 250 gp)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 min./level or until discharged"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Summoner\
4: Adept, Alchemist, Arcanist, Bloodrager, Inquisitor, Investigator, Magus, Occultist, Psychic, Sorcerer, Unchained Summoner, Wizard\
5: Druid, Hunter, Shaman
Casting time: 1 standard action
Components: V, S, M (granite and diamond dust worth 250 gp)
Range: touch
Duration: 10 min./level or until discharged
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

**Sources:** PRPG Core Rulebook pg 350

The warded creature gains resistance to blows, cuts, stabs, and slashes. The subject gains DR
10/adamantine. It ignores the first 10 points of damage each time it takes damage from a weapon,
though an adamantine weapon bypasses the reduction. Once the spell has prevented a total of 10
points of damage per caster level (maximum 150 points), it is discharged.

### Mythic Stoneskin

**Sources:** Mythic Adventures pg 109

The target gains a +4 bonus on saving throws against disease, poison, and stun effects. There is a
50% chance any critical hit or sneak attack against the target is treated as a normal hit, as if the
target were wearing medium fortification armor.

### Clay Skin

**Sources:** Potions and Poisons pg 17

The target's skin becomes as thick and tough as clay, granting the target DR 5/adamantine. Once the
spell has prevented a total of 5 points of damage per caster level (maximum 50 points), it is
discharged and the spell ends.

### Communal Stoneskin

**Sources:** Ultimate Combat pg 245

This spell functions like stoneskin, except you divide the duration in 10 minute intervals among the
creatures touched. Once the spell has prevented 10 points of damage per caster level (maximum 150
points) for a subject, the spell's effects end for that subject.
