+++
id = "ref/arc-warpriest/jistkan-magistrate"
kind = "archetype"
title = "Jistkan Magistrate"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "jistkan_magistrate", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "blood-of-the-ancients"
page = "17"

[fields]
kind = "archetype"
alters = ["Blessings", "Spontaneous casting", "Bonus languages", "Channel"]
+++

Some warpriests study the ancient magic that the Jistkan magistrates used to bind elementals and
make pacts with genies. By tapping into the elementals' primal magic, these warpriests gain powers
that help them in combat.

**Prerequisites:** Must worship a deity who grants the [Air](ref/blessing/air),
[Earth](ref/blessing/earth), [Fire](ref/blessing/fire), or [Water](ref/blessing/water) blessing

**Gained class skills:** kp

**Lost class skills:** sur

**Elemental Binder (Su)**

**Alters:** Blessings

**Info:** A Jistkan magistrate must select the Air, Earth, Fire, or Water blessing. He does not gain
a second blessing.

**Spontaneous Summons**

**Ability:** In addition to losing prepared spells to cast &quot&cure&quot& or &quot&inflict&quot&
spells, he can also lose a prepared spell in order to cast any
[summon monster](ref/spell/summon-monster) spell of the same level or lower. He can use this ability
only to summon an [elemental](ref/family/elemental) whose subtype matches his blessing. He can
expend one use of his _fervor_ ability to decrease the spell's casting time to 1 **standard action**
and to increase the spell's duration to 1 minute per level.

**Alters:** Spontaneous casting

**Flavor:** A Jistkan magistrate is extremely flexible in channeling his stored spell energy.

**Bonus Languages**

**Alters:** Bonus languages

**Passive:** A Jistkan magistrate's bonus language options include Aquan, Auran, Ignan, and Terran
instead of Abyssal, Celestial, and Infernal. These choices are in addition to the bonus languages
available to the character because of his race.

**Channel Element (Su)**

**Action:** Ability

**Alters:** Channel

**Gained:** At 4th Level

A Jistkan magistrate gains [Elemental Channel](ref/feat/elemental-channel) as a bonus feat, choosing
the elemental subtype that matches his blessing. He doesn't gain the ability to harm undead with
channeled energy (if he channels positive energy) or heal undead (if he channels negative energy).
Instead, he can channel a blast of elemental matter and energy that buffets his targets. The Jistkan
artificer's blessing determines the damage type of this attack, as indicated by the table below. A
successful Reflex save halves the damage.

|Blessing|Damage type|
| --- | --- |
|Air|Electricity|
|Earth|Acid|
|Fire|Fire|
|Water|Cold|
