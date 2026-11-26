+++
id = "ref/arc-medium/uda-wendo"
kind = "archetype"
title = "Uda Wendo"
aon = "ArchetypeDisplay.aspx?FixedName=Medium%20Uda%20Wendo"
source_ids = ["haunted-heroes-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "uda_wendo", path = "json/archetypes_medium.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/medium" },
]
[[sources]]
publication = "haunted-heroes-handbook"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "wendo", level = 1 },
  { anchor = "wendo-s-secrets", level = 2 },
  { anchor = "wendo-tongue", level = 3 },
]
trades = [
  { replaces = "Shared seance", feature = "shared-seance", by = ["wendo-s-secrets"] },
  { replaces = "Haunt channeler", feature = "haunt-channeler", by = ["wendo-tongue"] },
  { replaces = "location channel", feature = "location-channel", by = ["wendo-tongue"] },
  { replaces = "connection channel", feature = "connection-channel", by = ["wendo-tongue"] },
  { alters = "Spirit", feature = "spirit", by = ["wendo"] },
  { alters = "Class skills" },
]
+++

Primarily found among the various tribes of the Mwangi Expanse, uda wendo are powerful mediums who
are sensitive to the presence and desires of the wendo, powerful and mysterious entities that walk
Golarion while shaping fate and guiding destiny. Rather than simply communing with the wendo like
some oracles do, an uda wendo invites the wendo to use his body as a vessel, gaining fantastic
powers even while struggling to maintain control of his body against the crushing might of the
wendo's presence.

## Class Skills {#class-skills}

An uda wendo adds Knowledge (geography) and Knowledge (nature) to his list of class skills, instead
of Perform.

This alters the medium's class skills.

## Wendo (Su) {#wendo}

Rather than channeling spirits, an uda [wendo](ref/faith/wendo) channels the wendo, otherworldly
entities that walk among mortals. This functions like channeling a spirit, except instead of
requiring a favored location to channel a wendo, an uda wendo must offer the wendo a sacrifice worth
at least 50 gp per Hit Die the uda wendo has. Alternatively, the uda wendo can instead accept 1
point of burn, as per the [kineticist](ref/class/kineticist) class ability (_Pathfinder RPG Occult
Adventures_ 11), instead of sacrificing material wealth. While channeling a wendo, the uda wendo
gains the 1st-level domain power of one [druid animal or terrain domain](ref/ability/druid-domains),
or the 1st-level domain power of one of the following cleric domains: [Air](ref/domain/air),
[Animal](ref/domain/animal), Community, Darkness, Death, [Destruction](ref/domain/destruction),
[Earth](ref/domain/earth), [Fire](ref/domain/fire), [Healing](ref/domain/healing), Knowledge,
[Protection](ref/domain/protection), Rune, Strength, [Sun](ref/domain/sun), Trickery,
[War](ref/domain/war), [Water](ref/domain/water), or [Weather](ref/domain/weather). The uda wendo
has an effective cleric or druid level equal to 1/2 his medium level (minimum 1st) for the purpose
of this ability. In addition, he adds all spells from his chosen domain that are of a spell level he
can cast (including modifications to the uda wendo's spellcasting from the archmage arcana or divine
surge lesser spirit powers) to his medium spell list and medium spells known as medium spells of
their domain spell level.

An uda wendo cannot invite allies to a seance to summon a wendo, and by channeling a wendo, the uda
wendo allows the entity to gain 2 points of influence over him. If any sentient creature that
doesn't practice juju witnesses the uda wendo's seance, both creatures become permanently cursed
with a -2 penalty on all d20 rolls and checks (as per _[bestow curse](ref/spell/bestow-curse)_) and
the attempt fails.

This ability alters spirit.

## Wendo's Secrets (Ex) {#wendo-s-secrets}

At 2nd level, an uda wendo learns most of his information through tales and secrets whispered to him
by the wendo. He adds his Charisma bonus (if any) to all Knowledge checks that he attempts in
addition to his Intelligence modifier.

This ability replaces shared seance.

## Wendo Tongue (Su) {#wendo-tongue}

At 3rd level, an uda wendo can invoke the wendo to commune with nearby spirits for a number of
minutes per day equal to his level. These minutes don't need to be used consecutively, but they must
be spent in 1-minute increments. The uda wendo can use this ability to speak with corpses (as per
_[speak with dead](ref/spell/speak-with-dead)_) at 3rd level, with animals and plants (as per
_[speak with animals](ref/spell/speak-with-animals)_ or
_[speak with plants](ref/spell/speak-with-plants)_) at 5th level, and with humanoids (as per
_[tongues](ref/spell/tongues)_) at 7th level.

This ability replaces haunt channeler, location channel, and connection channel.
