+++
id = "ref/spell/haste"
kind = "spell"
title = "Haste"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "haste", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a shaving of licorice root)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Medium, Summoner\
3: Alchemist, Arcanist, Bloodrager, Bard, Investigator, Magus, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Spiritualist, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (a shaving of licorice root)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Targets: one creature/level, no two of which can be more than 30 ft. apart
:::

**Sources:** PRPG Core Rulebook pg 293

The transmuted creatures move and act more quickly than normal. This extra speed has several
effects.

When making a full attack action, a hasted creature may make one extra attack with one natural or
manufactured weapon. The attack is made using the creature's full base attack bonus, plus any
modifiers appropriate to the situation. (This effect is not cumulative with similar effects, such as
that provided by a speed weapon, nor does it actually grant an extra action, so you can't use it to
cast a second spell or otherwise take an extra action in the round.)

A hasted creature gains a +1 bonus on attack rolls and a +1 dodge bonus to AC and Reflex saves. Any
condition that makes you lose your Dexterity bonus to Armor Class (if any) also makes you lose dodge
bonuses.

All of the hasted creature's modes of movement (including land movement, burrow, climb, fly, and
swim) increase by 30 feet, to a maximum of twice the subject's normal speed using that form of
movement. This increase counts as an enhancement bonus, and it affects the creature's jumping
distance as normal for increased speed. Multiple haste effects don't stack. Haste dispels and
counters [slow](ref/spell/slow).

### Mythic Haste

**Sources:** Mythic Adventures pg 97\
Affected creatures gain an additional move action each round. The movement speed increase changes to
50 feet, to a maximum of three times the creature's normal speed for that movement type.

_Augmented (3rd):_ If you expend two uses of mythic power, the movement speed increase changes to 70
feet, with no limit based on the creature's normal speed. If an affected creature moves at least 30
feet on its turn, it can travel across liquid as if the liquid were solid. If the liquid deals
damage on contact, the creature takes only half damage from moving across it.
