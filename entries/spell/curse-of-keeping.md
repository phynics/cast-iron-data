+++
id = "ref/spell/curse-of-keeping"
kind = "spell"
title = "Curse of Keeping"
aon = "SpellDisplay.aspx?ItemName=Curse%20of%20Keeping"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_of_keeping", path = "json/spells3.json" },
]
[[sources]]
publication = "black-markets"
page = "30"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 day/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Antipaladin, Shaman, Witch
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 day/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: curse
:::

You curse the target with the inability to sell, barter, or give away any item it owns, other than
ordinary currency, for as long as the spell remains in effect. The target cannot sell, trade, drop,
or give away possessions. The target can purchase items using ordinary currency but can't then sell
the purchased items. The target can accept gifts from others but can't offer anything in exchange. A
curse of keeping can be ended by [break enchantment](ref/spell/break-enchantment),
[limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle),
[remove curse](ref/spell/remove-curse), or [wish](ref/spell/wish).
[Dispel magic](ref/spell/dispel-magic) does not affect a curse of keeping.
