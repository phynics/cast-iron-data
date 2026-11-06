+++
id = "ref/spell/covetous-aura"
kind = "spell"
title = "Covetous Aura"
source_ids = ["rise-of-the-runelords-anniversary-edition", "pathfinder-5-sins-of-the-saviors", "inner-sea-world-guide", "mythic-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "covetous_aura", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 round"
components = "V, S"
range = "personal"
effects = [
  { label = "Area", value = "25-ft.-radius emanation centered on you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 5: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Area: 25-ft.-radius emanation centered on you
:::

**Sources:** Rise of the Runelords Anniversary Edition pg 418, Pathfinder \#5: Sins of the Saviors
pg 58, Inner Sea World Guide pg 294

Anytime a harmless (so noted by a spell's saving throw description) spell of 3rd level or lower is
cast within a covetous aura's area of effect, you may choose to immediately gain the benefit of that
spell as if it had also targeted you. The intended target still gains the effect of the spell. You
gain the benefits of this duplicated spell only if the caster is in range of the covetous aura. Each
time a covetous aura duplicates a spell effect, the remaining duration of the covetous aura is
reduced by a number of rounds equal to the spell level of the spell effect that is duplicated.

### Mythic Covetous Aura

**Sources:** Mythic Origins pg 12

The duration of the covetous aura increases to 1 minute per level or until discharged. You may gain
the benefits of spells of 5th level or lower cast within the aura's area of effect. You can gain the
effects of two separate spells, after which the mythic covetous aura ends.

_Augmented (6th):_ If you expend two uses of mythic power, the duration increases to 10 minutes per
level or until discharged. You may gain the benefits of spells of 7th level or lower cast within the
aura's area of effect. When you gain the benefit of a spell, the original spell is immediately
targeted with a [greater dispel magic](ref/spell/dispel-magic-greater) spell at your caster level.
If the dispel check succeeds, the spell ends for any of the original recipients in the area of your
covetous aura.
