+++
id = "ref/spell/euphoric-tranquility"
kind = "spell"
title = "Euphoric Tranquility"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "euphoric_tranquility", path = "json/spells4.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "219"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 8 },
  { class = "Druid", level = 8 },
  { class = "Mesmerist", level = 6 },
  { class = "Oracle", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a poppy flower)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "none and Will partial (see below)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Bard, Mesmerist, Skald\
8: Arcanist, Cleric, Druid, Oracle, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a poppy flower)
Range: touch
Duration: 1 round/level
Saving throw: none and Will partial (see below)
Spell resistance: yes
Target: creature touched
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

A creature under the effect of this enchantment enters a state of euphoria. The target treats all
creatures as dear friends and abhors violence, but may rise up to protect itself if violence is
perpetrated against it. Until the end of the spell's duration, the creature's speed is halved, and
it cannot make attacks or cast spells. If the creature is attacked, it gets a Will saving throw. If
the saving throw succeeds, the creature can make act normally for 1 round. If the saving throw
fails, the creature moves half its speed away from the attacker as its next action.

Furthermore, if the creature is interacted with, or questioned while under the effects of this
spell, it is considered to have an attitude of Helpful (see the
[Diplomacy skill](ref/skill/diplomacy)), though any advice or answers it gives may be disjointed or
stream of consciousness due to its euphoric state.
