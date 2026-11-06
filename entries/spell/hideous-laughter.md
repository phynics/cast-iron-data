+++
id = "ref/spell/hideous-laughter"
kind = "spell"
title = "Hideous Laughter"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hideous_laughter", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 1 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (tiny fruit tarts and a feather)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature; see text" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Bard, Mesmerist, Skald\
2: Arcanist, Medium, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (tiny fruit tarts and a feather)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature; see text
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 296

This spell afflicts the subject with uncontrollable laughter. It collapses into gales of manic
laughter, falling prone. The subject can take no actions while laughing, but is not considered
helpless. After the spell ends, it can act normally. On the creature's next turn, it may attempt a
new saving throw to end the effect. This is a full round action that does not provoke attacks of
opportunity. If this save is successful, the effect ends. If not, the creature continues laughing
for the entire duration.

A creature with an Intelligence score of 2 or lower is not affected. A creature whose type is
different from the caster's receives a +4 bonus on its saving throw, because humor doesn't
"translate" well.

### Mythic Hideous Laughter

**Sources:** Mythic Adventures pg 98\
A creature of a type different than your own doesn't gain a bonus on its saving throws against this
spell. The affected target laughs so hard it hurts, and takes 1d6 points of nonlethal damage each
round it spends laughing.

If the target fails its initial save, it must succeed at two follow-up saving throws (each a
full-round action that doesn't provoke attacks of opportunity) to end the spell. Succeeding at only
one save means the spell no longer deals damage, but the target is still unable to take actions.

_Augmented:_ If you expend two uses of mythic power, the target's laughter becomes contagious. When
the target's allies are within 30 feet and can hear the laugh, they must successfully save against
the spell or be sickened until the target stops laughing. The sickened effect ends if the ally moves
more than 30 feet from the target or is unable to hear the target's laughter for an entire round.
