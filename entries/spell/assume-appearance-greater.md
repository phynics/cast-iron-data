+++
id = "ref/spell/assume-appearance-greater"
kind = "spell"
title = "Greater Assume Appearance"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "assume_appearance_greater", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/assume-appearance" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 minute"
components = "V, S, F (corpse or likeness of the deceased creature whose form you plan to assume)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 day/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Arcanist, Bard, Investigator, Medium, Mesmerist, Occultist, Psychic, Shaman, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 minute
Components: V, S, F (corpse or likeness of the deceased creature whose form you plan to assume)
Range: personal
Target: you
Duration: 1 day/level (D)
Saving throw: none
Spell resistance: no
Subschool: Polymorph
:::

## Assume Appearance

**Sources:** Horror Adventures pg 108

This spell functions similarly to alter self, except for the following differences. You assume the
exact form of a deceased Small or Medium creature of the humanoid type. Your voice changes to match
that of the form you assume. The creature whose form you assume must be dead and you must have
access to its fresh corpse (either dead less than 24 hours, or preserved via
[gentle repose](ref/spell/gentle-repose) or similar effect). Any attempt to copy the form of a
living creature causes the spell to fail. You do not have access to the assumed form's abilities,
memories, mannerisms, or speech patterns. The spell grants a +10 bonus on Disguise checks to appear
as the imitated creature.

If the assumed creature is returned to life while this spell is active, assume appearance
immediately ends.

### Greater Assume Appearance

**Sources:** Horror Adventures pg 109

This spell functions similar to [assume appearance](ref/spell/assume-appearance), except that you
can imitate a creature even if you have only a likeness (such as a sketch or painting) that is
fairly accurate. If there is an age difference between the likeness and the actual creature, you
take on the appearance of the creature near the end of its life. If you have heard the creature
whose form you plan to assume speak aloud, you can also copy its voice as vocal alteration
([speak with dead](ref/spell/speak-with-dead) can also be used to fulfill this requirement). The
spell doesn't grant insight into the dead creature's mannerisms

Additionally, if a likeness used as a focus for the spell is kept on your person or within 30 feet
at all times, the aura of greater ssume appearance is redirected to the likeness instead of to you,
similar to a reverse application of the misdirection spell.
