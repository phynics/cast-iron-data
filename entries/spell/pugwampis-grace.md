+++
id = "ref/spell/pugwampis-grace"
kind = "spell"
title = "Pugwampi's Grace"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pugwampis_grace", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a pugwampi's hair)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature (see below)" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Skald\
3: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a pugwampi's hair)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature (see below)
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Inner Sea Magic pg 59

Hated by adventurers throughout the Inner Sea region, the gremlins known as pugwampis infect those
around them with a malignant form of unluck - an effect that this spell emulates. If the target
fails its Will save, it becomes infused with the so-called "grace of the pugwampi." A creature
affected by this spell must roll two d20s whenever a situation calls for a d20 roll (such as an
attack roll, a skill check, or a saving throw) and must use the lower of the two results generated.
As with the aura shed by actual pugwampies, this spell has no effect on animals, gremlins, or
gnolls. The effects of this spell are negated as long as a target gains any sort of luck bonus to a
d20 roll (such as those granted by a luckstone or divine favor), but the spell's duration is not
impacted by these effects. If the luck bonus goes away before the pugwampi's grace effect ends, the
unluck returns and remains until the spell's normal duration runs out.
