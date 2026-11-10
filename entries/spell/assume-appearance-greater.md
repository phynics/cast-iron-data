+++
id = "ref/spell/assume-appearance-greater"
kind = "spell"
title = "Greater Assume Appearance"
aon = "SpellDisplay.aspx?ItemName=Assume%20Appearance%2C%20Greater"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "assume_appearance_greater", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/assume-appearance" },
]
[[sources]]
publication = "horror-adventures"
page = "109"

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

### Greater Assume Appearance

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
