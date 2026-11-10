+++
id = "ref/spell/charm-person"
kind = "spell"
title = "Charm Person"
source_ids = ["core-rulebook", "the-first-world-realm-of-the-fey", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "charm_person", path = "json/spells2.json" },
]
[[sources]]
publication = "core-rulebook"
page = "254"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one humanoid creature" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Arcanist, Bard, Mesmerist, Occultist, Psychic, Shaman, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level
Saving throw: Will negates
Spell resistance: yes
Target: one humanoid creature
Subschool: Charm
Descriptors: mind-affecting
:::

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
