+++
id = "ref/spell/gullibility"
kind = "spell"
title = "Gullibility"
aon = "SpellDisplay.aspx?ItemName=Gullibility"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gullibility", path = "json/spells5.json" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "14"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Antipaladin, Arcanist, Bard, Inquisitor, Mesmerist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Charm
Descriptors: mind-affecting
:::

You befuddle the target's mind, making it more willing to believe even the most outlandish tales.
The target takes a -10 penalty on Sense Motive checks for the spell's duration. In addition,
creatures that attempt to lie to or deceive the target gain a +10 bonus on their Bluff checks, as if
the target wanted to believe them and was drunk or impaired simultaneously. Furthermore, the
believability of any lie told to a creature under the effects of gullibility increases by one step;
an impossible lie seems far-fetched, a far-fetched lie seems unlikely, and an unlikely lie seems
believable.

A creature gains no benefits from glibness on Bluff checks to lie to or deceive a creature that is
under the effects of gullibility; in effect, gullibility renders a target so willing to believe what
others say that glibness cannot make their words any more believable.
