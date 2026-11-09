+++
id = "ref/spell/meticulous-match"
kind = "spell"
title = "Meticulous Match"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "meticulous_match", path = "json/spells14.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "220"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "10 minutes"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "two objects touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Bard, Hunter, Inquisitor, Occultist, Ranger, Skald\
4: Arcanist, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Target: two objects touched
:::

You compare two similar items and know if they are identical to one another or not. The spell can
indicate an identical match, a categorical match, or no match. For instance, blood samples are
identical if they are from the same creature. They are categorical if they are from the same
species. There is no match if they are from different species, or if one sample is merely stage
blood.

Alternatively, you can compare dissimilar items and know if they have a potential relationship. For
instance, you can compare a creature's tooth against a bite mark and know if that creature could
have caused the bite mark.

This spell is not infallible - an identical match can result from comparing items or creatures that
are duplicates of one another. For instance, a knife might have an identical match with a stab wound
if an identical knife was used to inflict the wound, and twins might have identical blood or
tissues.
