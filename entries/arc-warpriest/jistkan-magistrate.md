+++
id = "ref/arc-warpriest/jistkan-magistrate"
kind = "archetype"
title = "Jistkan Magistrate"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Jistkan%20Magistrate"
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
features = [
  { anchor = "elemental-binder" },
  { anchor = "spontaneous-summons" },
  { anchor = "bonus-languages" },
  { anchor = "channel-element", level = 4 },
]
trades = [
  { alters = "Blessings", feature = "blessings", by = ["elemental-binder"] },
  { alters = "Spontaneous casting", feature = "spontaneous-casting", by = ["spontaneous-summons"] },
  { alters = "Bonus languages", feature = "bonus-languages", by = ["bonus-languages"] },
  { alters = "Channel", feature = "channel-energy", by = ["channel-element"] },
  { alters = "Class skills" },
]
+++

Some warpriests study the ancient magic that the Jistkan magistrates used to bind elementals and
make pacts with genies. By tapping into the elementals' primal magic, these warpriests gain powers
that help them in combat.

## Class Skills {#class-skills}

A Jistkan magistrate gains Knowledge (planes) as a class skill. Survival is not a class skill for a
Jistkan magistrate.

This alters the warpriest's class skills.

## Elemental Binder (Su) {#elemental-binder}

A Jistkan magistrate must worship a deity who grants the Air, Earth, Fire, or Water blessing, and he
must select one of these blessings. He does not gain a second blessing.

This alters the warpriest's blessings.

## Spontaneous Summons {#spontaneous-summons}

A Jistkan magistrate is extremely flexible in channeling his stored spell energy. In addition to
losing prepared spells to cast "cure" or "inflict" spells, he can also lose a prepared spell in
order to cast any _[summon monster](ref/spell/summon-monster)_ spell of the same level or lower. He
can use this ability only to summon an [elemental](ref/family/elemental) whose subtype matches his
blessing. He can expend one use of his fervor ability to decrease the spell's casting time to 1
standard action and to increase the spell's duration to 1 minute per level.

This alters spontaneous casting.

## Bonus Languages {#bonus-languages}

A Jistkan magistrate's bonus language options include Aquan, Auran, Ignan, and Terran instead of
Abyssal, Celestial, and Infernal. These choices are in addition to the bonus languages available to
the character because of his race.

This alters the warpriest's bonus languages.

## Channel Element (Su) {#channel-element}

At 4th level, a Jistkan magistrate gains [Elemental Channel](ref/feat/elemental-channel) as a bonus
feat, choosing the elemental subtype that matches his blessing. He doesn't gain the ability to harm
undead with channeled energy (if he channels positive energy) or heal undead (if he channels
negative energy). Instead, he can channel a blast of elemental matter and energy that buffets his
targets. The Jistkan magistrate's blessing determines the damage type of this attack, as indicated
by the table below. A successful Reflex save halves the damage.

This alters channel.

**Channel Element Damage**

|Blessing|Damage type|
| --- | --- |
|Air|Electricity|
|Earth|Acid|
|Fire|Fire|
|Water|Cold|
