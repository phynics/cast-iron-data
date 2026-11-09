+++
id = "ref/spell/book-ward"
kind = "spell"
title = "Book Ward"
source_ids = ["seekers-of-secrets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "book_ward", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/protection-from-energy" },
]
[[sources]]
publication = "seekers-of-secrets"
page = "17"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a drop of clear oil)"
range = "touch"
effects = [
  { label = "Target", value = "one touched object of up to 10 pounds/level" },
]
duration = "1 day/level or until discharged (see text)"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Arcanist, Bard, Cleric, Oracle, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a drop of clear oil)
Range: touch
Duration: 1 day/level or until discharged (see text)
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: one touched object of up to 10 pounds/level
:::

As [protection from energy](ref/spell/protection-from-energy), except as noted above and that the
spell only protects against acid and fire damage. While the energy protection remains, the item is
also completely waterproof (this protection extends to other liquids as well, such as alcohol and
oil).
