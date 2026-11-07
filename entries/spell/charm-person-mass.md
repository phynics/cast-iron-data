+++
id = "ref/spell/charm-person-mass"
kind = "spell"
title = "Mass Charm Person"
source_ids = ["core-rulebook", "the-first-world-realm-of-the-fey", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "charm_person_mass", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one or more humanoid creatures, no two of which can be more than 30 ft. apart" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Bard, Mesmerist, Occultist, Skald\
5: Arcanist, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one or more humanoid creatures, no two of which can be more than 30 ft. apart
Duration: 1 hour/level
Saving throw: Will negates
Spell resistance: yes
Subschool: Charm
Descriptors: mind-affecting
:::

## Charm Person

**Sources:** PRPG Core Rulebook pg 254

This charm makes a humanoid creature regard you as its trusted friend and ally (treat the target's
attitude as friendly). If the creature is currently being threatened or attacked by you or your
allies, however, it receives a +5 bonus on its saving throw.

The spell does not enable you to control the charmed person as if it were an automaton, but it
perceives your words and actions in the most favorable way. You can try to give the subject orders,
but you must win an opposed Charisma check to convince it to do anything it wouldn't ordinarily do.
(Retries are not allowed.) An affected creature never obeys suicidal or obviously harmful orders,
but it might be convinced that something very dangerous is worth doing. Any act by you or your
apparent allies that threatens the charmed person breaks the spell. You must speak the person's
language to communicate your commands, or else be good at pantomiming.

### Charm Fey

**Sources:** The First World, Realm of the Fey pg 12

This spell functions as charm person, except it affects a fey instead of a humanoid.

### Mass Charm Person

**Sources:** Ultimate Intrigue pg 206

This spell functions like charm person, except that mass charm person affects a number of humanoid
creatures whose combined Hit Dice don't exceed twice your level. If there are more potential targets
than you can affect, you choose them one at a time until you reach the limit of HD you can affect.
If you cast mass charm person on only one creature, you ignore the spell's HD limit.
