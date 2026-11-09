+++
id = "ref/spell/brand-of-hobbling"
kind = "spell"
title = "Brand of Hobbling"
aon = "SpellDisplay.aspx?ItemName=Brand%20of%20Hobbling"
source_ids = ["adventurers-guide", "path-of-the-hellknight"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "brand_of_hobbling", path = "json/spells2.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "98"
[[sources]]
publication = "path-of-the-hellknight"
page = "60"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Inquisitor", level = 2 },
]
casting_time = "1 round"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 day/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Inquisitor
Casting time: 1 round
Components: V, S, DF
Range: touch
Duration: 1 day/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: creature touched
Descriptors: curse
:::

This spell etches a symbol of chains, a particular prison, or a lawful institution on the target,
dealing 1d6 points of damage. The mark can be placed on any exposed portion of the creature,
typically on the head or forearm. While the recipient is branded in this way, all of its movement
speeds are reduced by half (rounded down to the next 5-foot increment). A brand of hobbling can be
hidden by clothing or removed by scraping the brand away (the latter deals 1d6 points of damage,
though the brand returns if that damage is healed), but in either case the effects of a brand of
hobbling continue to function.
