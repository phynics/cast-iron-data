+++
id = "ref/spell/command"
kind = "spell"
title = "Command"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "command", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Adept", level = 1 },
  { class = "Antipaladin", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Adept, Antipaladin, Cleric, Inquisitor, Medium, Mesmerist, Occultist, Oracle, Psychic, Warpriest, Witch
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: language-dependant, mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 256

You give the subject a single command, which it obeys to the best of its ability at its earliest
opportunity. You may select from the following options.

_Approach:_ On its turn, the subject moves toward you as quickly and directly as possible for 1
round. The creature may do nothing but move during its turn, and it provokes attacks of opportunity
for this movement as normal.

_Drop:_ On its turn, the subject drops whatever it is holding. It can't pick up any dropped item
until its next turn.

_Fall:_ On its turn, the subject falls to the ground and remains prone for 1 round. It may act
normally while prone but takes any appropriate penalties.

_Flee:_ On its turn, the subject moves away from you as quickly as possible for 1 round. It may do
nothing but move during its turn, and it provokes attacks of opportunity for this movement as
normal.

_Halt:_ The subject stands in place for 1 round. It may not take any actions but is not considered
helpless.

If the subject can't carry out your command on its next turn, the spell automatically fails.

### Mythic Command

**Sources:** Mythic Adventures pg 88

You can target up to one creature per level, each of which must receive the same command. Creatures
that succeed at their saving throws are staggered for 1 round (this is a mind-affecting effect).
