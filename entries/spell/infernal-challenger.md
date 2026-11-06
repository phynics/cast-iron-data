+++
id = "ref/spell/infernal-challenger"
kind = "spell"
title = "Infernal Challenger"
source_ids = ["adventurers-guide", "path-of-the-hellknight"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "infernal_challenger", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Calling"]
descriptors = ["lawful"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 round"
components = "V, S, F/DF (an iron badge or medallion)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one called bearded devil and testing ground; see text" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Cleric, Oracle, Sorcerer, Summoner, Unchained Summoner, Warpriest, Wizard
Casting time: 1 round
Components: V, S, F/DF (an iron badge or medallion)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Effect: one called bearded devil and testing ground; see text
Subschool: Calling
Descriptors: lawful
:::

**Sources:** Adventurer's Guide pg 98, Path of the Hellknight pg 60

This spell summons a bearded devil, causing it to appear where you designate. The area within a
50-foot radius of where the devil appears is ringed with a smoldering, red glow. This area is the
testing ground. To successfully cast this spell, no creature other than the devil's challenger (see
below) can be within this area while the spell is being cast.

On the round it appears, the devil identifies itself (typically by name and with a brief recitation
of honors) and states it is prepared to do battle with a sole mortal champion. In the same round,
either you or a creature you designate while casting the spell must identify the devil's challenger.
For the duration of the spell, the devil does everything in its power to kill the challenger. You do
not control the devil or have any influence over how it conducts itself in battle, but the devil
cannot leave the testing ground. Unlike with summon monster and similar spells, you cannot dismiss
the devil. Rather, the conjured devil remains until any one of the following criteria is met: it is
reduced below 0 hit points or otherwise defeated, its challenger is slain, its challenger leaves the
testing ground, or it takes damage from any source other than its challenger. Upon any of these
occurrences, the devil vanishes.

Conjuring a devil is typically an evil act. If cast for any purpose besides the administering of a
[Hellknight](ref/rule/aff-lawknights) test, this spell has the evil descriptor.
