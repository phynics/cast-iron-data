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
features = [
  { anchor = "monster-insight", level = 2 },
  { anchor = "signs-and-portents", level = 2 },
  { anchor = "predictive-strike", level = 5 },
]
trades = [
  { replaces = "Well-versed", feature = "well-versed", by = ["monster-insight"] },
  { replaces = "All types of versatile performance", feature = "versatile-performance", by = ["signs-and-portents"] },
  { replaces = "Spell kenning", feature = "spell-kenning", by = ["predictive-strike"] },
]
+++

Tales of Merivesta Olinchi are surprisingly common among the Bekyar of the Mwangi Expanse, who claim
she spent some time studying their traditions and history. Most historians find it more likely that
a Bekyar skald spent time in Nex, was exposed to the idea of divination as a tool of war from a copy
of [Cold Irony](ref/eq-spellbook/cold-irony), and fabricated tales of how that knowledge came to be
in his hands.

## Monster Insight (Ex) {#monster-insight}

At 2nd level, the augur applies his Charisma modifier in addition to his Intelligence modifier when
attempting Knowledge checks to identify the abilities and weaknesses of creatures. Monster insight
counts as the monster lore class feature for prerequisites. This ability replaces well-versed.

## Signs and Portents (Su) {#signs-and-portents}

At 2nd level, an augur can read signs and portents to attempt to ascertain how events in the near
future will play out. This allows the augur to cast _[augury](ref/spell/augury)_ as a
[spell-like ability](ref/umr/spell-like-abilities). At 7th level, he can instead use signs and
portents to cast _[divination](ref/spell/divination)_ as a
[spell-like ability](ref/umr/spell-like-abilities), and at 12th level, he can instead cast
_[commune](ref/spell/commune)_ as a [spell-like ability](ref/umr/spell-like-abilities). At 17th
level, he can use signs and portents twice per day. This ability replaces all types of versatile
performance.

## Predictive Strike (Su) {#predictive-strike}

At 5th level, the augur accurately divines the possible movements of his enemies in combat. Once per
day as a free action, he can declare one of his melee attacks to be a predictive strike. Against the
augur's attack, the target is [flat-footed](ref/rule/flat-footed) and gains no benefits from
[concealment](ref/rule/concealment) or [cover](ref/rule/cover). Attacks from other creatures are
treated normally. The target still benefits from total concealment and total cover normally. At 11th
level, the augur can use this ability a total of two attacks per day, and at 17th, three attacks per
day. This replaces spell kenning.
