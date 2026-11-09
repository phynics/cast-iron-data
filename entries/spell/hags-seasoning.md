+++
id = "ref/spell/hags-seasoning"
kind = "spell"
title = "Hag's Seasoning"
aon = "SpellDisplay.aspx?ItemName=Hag%27s%20Seasoning"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hags_seasoning", path = "json/spells5.json" },
]
[[sources]]
publication = "blood-of-the-coven"
page = "21"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "S, M (a handful of spices)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Antipaladin, Bloodrager\
3: Druid, Hunter, Shaman, Witch
Casting time: 1 standard action
Components: S, M (a handful of spices)
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent (D)
Saving throw: none
Spell resistance: yes
Target: one creature
Descriptors: curse
:::

You render the affected creature supernaturally delicious, making it the preferred target for
animalistic monsters, as well as biting insects, stray animals, and vermin. A creature that makes a
successful bite attack against or otherwise ingests a portion of the victim (such as with drain
blood or swallow whole) gains a number of temporary hit points equal to half your caster level.
These temporary hit points last for 1 hour. A creature cannot gain temporary hit points from this
spell more than once per day, no matter how many times it bites your target or how many different
cursed targets it bites.
