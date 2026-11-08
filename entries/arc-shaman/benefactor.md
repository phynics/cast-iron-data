+++
id = "ref/arc-shaman/benefactor"
kind = "archetype"
title = "Benefactor"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "benefactor", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]

[fields]
kind = "archetype"
alters = ["Spellcasting", "Hexes"]
+++

**Sources:** Healer's Handbook pg 26\
Though most shamans dole out banes and boons equally, a benefactor seeks to improve the lives of
others by primarily offering powerful supportive abilities and magic to her allies and others she
deems worthy.

**Benefactor Ethos**

**Alters:** Spellcasting

**Info:** Benefactors cannot cast shaman spells with the curse descriptor; for the benefactor's
purpose, they are considered not on the shaman spell list. A benefactor can't use spell completion
or spell trigger magic items that use shaman spells with the curse descriptor unless she succeeds at
a Use Magic Device check.

**Benefactor Hexes**

**Ability:** A benefactor adds the following hexes to the list of shaman hexes she can choose from
whenever she gains a new _hex_ or a _wandering hex._

**Alters:** Hexes

**Special:** A benefactor cannot gain a _hex_ that is a curse effect or that has the word
&quot&curse&quot& in its name as a _hex_ or a _wandering hex._

**Boon Reservoir (Su)**

**Ability:** Once per day, a benefactor can perform a 10-minute ritual with one of her allies, plus
one additional ally for every 3 shaman levels she has. All creatures that participate in the ritual
(including the benefactor) gain a boon reservoir with a number of points equal to 1/2 the
benefactor's shaman level (minimum 1) for 24 hours.

**Immediate:** A creature can spend 1 point from its boon reservoir to gain a +2 insight bonus on
all saving throws it attempts until the start of its next turn.

**Special:** Boon reservoir points that are not spent within 24 hours are wasted.

**Expanded Boon (Su)**

**Choice:** When a benefactor gains this hex, she chooses one of the following: ability checks,
attack rolls, or skill checks. Instead of gaining an insight bonus on saving throws, any creature
with a boon reservoir granted by the benefactor can spend 1 point as an **immediate action** to gain
a +2 insight bonus on rolls or checks of the chosen kind until the start of its next turn.

**Prereq:** _Boon reservoir_ hex

**Special:** This hex can be chosen multiple times. Each time, it applies to a different roll or
check.

**Suppress Curse (Sp)**

**Special:** The benefactor uses her shaman level as her caster level for the purpose of this hex.

**Standard:** A benefactor can attempt to suppress one curse effect that is affecting a creature or
object with a touch. This functions as per [remove curse](ref/spell/remove-curse), except the
curse's effects are suppressed for 1 hour, even if it is a cursed shield, weapon, or suit of armor.
This allows a creature afflicted with any such cursed item to remove or get rid of it.
