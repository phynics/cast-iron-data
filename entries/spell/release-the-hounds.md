+++
id = "ref/spell/release-the-hounds"
kind = "spell"
title = "Release the Hounds"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "release_the_hounds", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (shards of a canine's fang)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one pack of canines" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Arcanist, Bard, Druid, Hunter, Shaman, Skald, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (shards of a canine's fang)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one pack of canines
Subschool: Summoning
:::

**Sources:** Magic Tactics Toolbox pg 10

This spell summons a pack of canines that respond to the spellcaster's commands and act in perfect
unison, causing them to function like a swarm. The pack uses the statistics for a winter wolf,
except it loses its breath weapon, the cold subtype, and its cold special attack and gains the swarm
subtype, a swarm attack that deals 3d6 points of damage, and the distraction special attack (DC 17).
Whenever the pack damages an opponent with its swarm attack, it can immediately attempt a trip
combat maneuver check against that creature with its trip special attack. The pack does not gain any
[damage reduction](ref/rule/damage-reduction) or immunity to damage and can be attacked by effects
that target a specific number of creatures, though such attacks deal 1/4 the normal amount of damage
(25%) and effects that don't deal hit point damage are only 25% likely to work.
