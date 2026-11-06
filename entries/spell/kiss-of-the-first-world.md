+++
id = "ref/spell/kiss-of-the-first-world"
kind = "spell"
title = "Kiss of the First World"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kiss_of_the_first_world", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Bard", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Skald", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (diamond dust worth 100 gp)"
range = "touch"
effects = [
  { label = "Area", value = "living or undead creature touched" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Bard, Druid, Hunter, Skald
Casting time: 1 standard action
Components: V, S, M (diamond dust worth 100 gp)
Range: touch
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Area: living or undead creature touched
:::

**Sources:** Inner Sea Magic pg 58

This spell - a favorite of fey spellcasters - is traditionally bestowed with a kiss, though all
that's really required to gift someone with a kiss of the First World is a touch. This spell infuses
a living creature with a surge of positive energy from the First World, filling the target with the
raw energies of life. The exact effects of this spell vary, depending on the nature of the creature
touched. Constructs are immune to the effects of this spell.

_Living Creature:_ A living creature gains a 20-foot increase to his base land speed and a +2
insight bonus on all Charisma-based skill checks. In addition, the creature gains
[fast healing](ref/umr/fast-healing) 2. Fire, acid, and negative energy cause this fast healing to
stop functioning on the round following the attack.

_Undead Creature:_ An undead creature targeted by this spell is staggered for the duration of this
spell. It does not gain the benefits of any [channel resistance](ref/rule/channel-resistance) it
might normally enjoy, and the save DCs for any of its special attacks (but not
[spell-like abilities](ref/umr/spell-like-abilities) or spells) are reduced by 2.
