+++
id = "ref/spell/heroes-feast"
kind = "spell"
title = "Heroes' Feast"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heroes_feast", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Warpriest", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "feast for one creature/level" },
]
duration = "1 hour plus 12 hours; see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Bard, Cleric, Inquisitor, Oracle, Skald, Warpriest
Casting time: 10 minutes
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour plus 12 hours; see text
Saving throw: none
Spell resistance: no
Effect: feast for one creature/level
Subschool: Creation
:::

**Sources:** PRPG Core Rulebook pg 295

You bring forth a great feast, including a magnificent table, chairs, service, and food and drink.
The feast takes 1 hour to consume, and the beneficial effects do not set in until this hour is over.
Every creature partaking of the feast is cured of all sickness and nausea, receives the benefits of
both [neutralize poison](ref/spell/neutralize-poison) and
[remove disease](ref/spell/remove-disease), and gains 1d8 temporary hit points + 1 point per two
caster levels (maximum +10) after imbibing the nectar-like beverage that is part of the feast. The
ambrosial food grants each creature that partakes a +1 morale bonus on attack rolls and Will saves
and a +4 morale bonus on saving throws against poison and fear effects for 12 hours.

If the feast is interrupted for any reason, the spell is ruined and all effects of the spell are
negated.
