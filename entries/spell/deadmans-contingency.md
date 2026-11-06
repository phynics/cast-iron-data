+++
id = "ref/spell/deadmans-contingency"
kind = "spell"
title = "Deadman's Contingency"
source_ids = ["core-rulebook", "mythic-adventures", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deadmans_contingency", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "at least 10 minutes; see text"
components = "V, S, M (quicksilver and an eyelash of a spell-using creature), F (ivory statuette of you worth 1,500 gp)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 day/level (d) or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Arcanist, Occultist, Psychic, Sorcerer, Wizard
Casting time: at least 10 minutes; see text
Components: V, S, M (quicksilver and an eyelash of a spell-using creature), F (ivory statuette of you worth 1,500 gp)
Range: personal
Duration: 1 day/level (d) or until discharged
Saving throw: none
Spell resistance: no
Target: you
:::

## Contingency

**Sources:** PRPG Core Rulebook pg 259

You can place another spell upon your person so that it comes into effect under some condition you
dictate when casting contingency. The contingency spell and the companion spell are cast at the same
time. The 10-minute casting time is the minimum total for both castings; if the companion spell has
a casting time longer than 10 minutes, use that instead. You must pay any costs associated with the
companion spell when you cast contingency.

The spell to be brought into effect by the contingency must be one that affects your person and be
of a spell level no higher than one-third your caster level (rounded down, maximum 6th level).

The conditions needed to bring the spell into effect must be clear, although they can be general. In
all cases, the contingency immediately brings into effect the companion spell, the latter being
"cast" instantaneously when the prescribed circumstances occur. If complicated or convoluted
conditions are prescribed, the whole spell combination (contingency and the companion magic) may
fail when triggered. The companion spell occurs based solely on the stated conditions, regardless of
whether you want it to.

You can use only one contingency spell at a time; if a second is cast, the first one (if still
active) is dispelled.

### Mythic Contingency

**Sources:** Mythic Adventures pg 89

You can cast this spell on yourself or another willing creature as if the spell had a range of
touch. A companion spell placed on another creature must be a spell from you, not from the creature,
and affects that creature when triggered. The target can have only one contingency spell upon it at
a time unless it also knows mythic contingency. The number of companion spells you can have on
yourself is equal to 1 + half your tier.

_Augmented (5th):_ If you expend two uses of mythic power, the casting time changes to 1 full round
plus the casting time of the companion spell, but the duration of mythic contingency decreases to 1
hour per level or until discharged.

### Deadman's Contingency

**Sources:** Ultimate Intrigue pg 210

This spell functions as contingency, except as noted above. This spell also only comes into effect
after your death and works only with certain spells. The companion spell triggers 1d6 rounds after
your death. All decisions made involving the companion spell must be made when deadman's contingency
is cast (including messages and recipients for spells like magic mouth or sending). If the spell
targets an object or appears in a certain location, it must target or be centered on your corpse.

The following spells can be companion spells for deadman's contingency:
[animate dead](ref/spell/animate-dead) (animating your corpse as an uncontrolled skeleton or
zombie), [disintegrate](ref/spell/disintegrate), [fireball](ref/spell/fireball),
[gentle repose](ref/spell/gentle-repose), [magic mouth](ref/spell/magic-mouth),
[major image](ref/spell/major-image) (with a duration of 3 rounds),
[permanent image](ref/spell/permanent-image), [sending](ref/spell/sending),
[stinking cloud](ref/spell/stinking-cloud), and [teleport object](ref/spell/teleport-object).
