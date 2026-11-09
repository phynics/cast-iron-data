+++
id = "ref/arc-cleric/iron-priest"
kind = "archetype"
title = "Iron Priest"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "iron_priest", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "technology-guide"
page = "12"

[fields]
kind = "archetype"
alters = ["Channel energy", "Casting"]
+++

Iron priests preach of the messengers from beyond the stars, envoys of the divine brought to
Golarion in a falling star. Iron priests can affect robots and other unliving constructs with
channeled energy, but lack power over the undead. Appropriate deities for an Iron Priest include
[Brigh](ref/faith/brigh), [Nethys](ref/faith/nethys), [Gorum](ref/faith/gorum), and
[Haagenti](ref/faith/haagenti). An iron priest has the following class features.

**Gained class skills:** dd, ke, kl, sur

**Lost class skills:** ka, kno, kp, sm

**Channel Energy (Su)**

**Ability:** When an iron priest _channels energy_ to heal or harm living creatures, she heals or
harms constructs with the clockwork or robot subtypes as well. Constructs without those subtypes are
also affected, but gain only half the normal amount of healing or take only half the normal amount
of damage, as appropriate. An iron priest cannot harm or heal undead with _channel energy._

**Alters:** Channel energy

**Spontaneous Casting**

**Ability:** An iron priest can spontaneously cast [make whole](ref/spell/make-whole) and
[greater make whole](ref/spell/make-whole-greater) in place of _cure/inflict moderate wounds_ and
_cure/inflict critical wounds,_ regardless of whether she channels positive or negative energy.

**Alters:** Casting
