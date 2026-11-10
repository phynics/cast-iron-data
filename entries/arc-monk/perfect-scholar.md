+++
id = "ref/arc-monk/perfect-scholar"
kind = "archetype"
title = "Perfect Scholar"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Perfect%20Scholar"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "perfect_scholar", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "44"

[fields]
kind = "archetype"
replaces = ["Still mind", "Slow fall", "Tongue of the sun and moon"]
alters = ["Perfect self"]
replaces_features = ["still-mind", "slow-fall", "tongue-of-the-sun-and-moon"]
alters_features = ["perfect-self"]
+++

Perfect scholars, often worshipers of Irori, hone their minds and bodies through the accumulation of
knowledge. They study and annotate the holy texts of Irori and other philosophies as well as collect
lore on anatomy, medicine, philosophy, martial arts, and history, among other topics of erudition.

**Gained class skills:** ka, kd, ke, kg, kh, kl, kna, kno, kp, kr, ling

**Lost class skills:** intm, perf

**Lore (Ex)**

**Gained:** At 3rd Level

**Passive:** The perfect scholar gains a bonus equal to 1/2 his monk level on Knowledge checks and
can attempt Knowledge checks untrained.

**Replaces:** Still mind

**Learn from Failure (Ex)**

**Ability:** When the perfect scholar misses with an attack roll or fails a
[Research check](ref/rule/research), he gains an insight bonus on his next attack roll or Research
check against the same target attempted in the next 24 hours. The insight bonus is equal to
[half](ref/misc/fractions-and-rounding) his monk level - 1.

**Gained:** At 4th Level

**Replaces:** Slow fall

**Special:** An individual target cannot be affected by this ability more than once in a 24-hour
period.

**Eye of the Sun and Moon (Ex)**

**Ability:** A perfect scholar can read all languages and write all languages he has read or heard.

**Gained:** At 17th Level

**Replaces:** Tongue of the sun and moon

**Walk with the Master (Su)**

**Ability:** The perfect scholar has mastered his spiritual resonance, allowing him to travel as if
using [etherealness](ref/spell/etherealness), [plane shift](ref/spell/plane-shift), or
[shadow walk](ref/spell/shadow-walk) at his monk level by spending only 1 point from his _ki pool._
He cannot bring other creatures with him. He is treated as an [outsider](ref/type/outsider) rather
than his original type, although he can be brought back to life as if he were still of his former
type.

**Alters:** Perfect self

**Gained:** At 20th Level
