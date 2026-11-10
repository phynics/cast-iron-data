+++
id = "ref/arc-skald/augur"
kind = "archetype"
title = "Augur"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Augur"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "augur", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "arcane-anthology"
page = "25"

[fields]
kind = "archetype"
replaces = ["Well-versed", "All types of versatile performance", "Spell kenning"]
replaces_features = ["well-versed", "spell-kenning"]
+++

Tales of Merivesta Olinchi are surprisingly common among the Bekyar of the Mwangi Expanse, who claim
she spent some time studying their traditions and history. Most historians find it more likely that
a Bekyar skald spent time in Nex, was exposed to the idea of divination as a tool of war from a copy
of [Cold Irony](ref/eq-spellbook/cold-irony), and fabricated tales of how that knowledge came to be
in his hands.

**Monster Insight (Ex)**

**Ability:** The augur applies his Charisma modifier in addition to his Intelligence modifier when
attempting Knowledge checks to identify the abilities and weaknesses of creatures.

**Gained:** At 2nd Level

**Replaces:** Well-versed

**Special:** Monster insight counts as the _monster lore_ class feature for prerequisites.

**Signs and Portents (Su)**

**At 12th Level:** He can instead cast [commune](ref/spell/commune) as a
[spell-like ability](ref/umr/spell-like-abilities).

**At 17th Level:** He can use _signs and portents_ twice per day.

**At 2nd Level:** An augur can read signs and portents to attempt to ascertain how events in the
near future will play out. This allows the augur to cast [augury](ref/spell/augury) as a
[spell-like ability](ref/umr/spell-like-abilities) once a day.

**At 7th Level:** He can instead use _signs and portents_ to cast [divination](ref/spell/divination)
as a [spell-like ability](ref/umr/spell-like-abilities).

**Replaces:** All types of versatile performance

**Predictive Strike (Su)**

**Flavor:** The augur accurately divines the possible movements of his enemies in combat.

**Free:** Once per day, he can declare one of his melee attacks to be a _predictive strike._ Against
the augur's attack, the target is [flat-footed](ref/rule/flat-footed) and gains no benefits from
[concealment](ref/rule/concealment) or [cover](ref/rule/cover). Attacks from other creatures are
treated normally. The target still benefits from total concealment and total cover normally.

**At 11th Level:** The augur can use this ability on a total of two attacks per day.

**At 17th Level:** He can use this on three attacks per day.

**Gained:** At 5th Level

**Replaces:** Spell kenning
