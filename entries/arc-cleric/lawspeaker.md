+++
id = "ref/arc-cleric/lawspeaker"
kind = "archetype"
title = "Lawspeaker"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Lawspeaker"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lawspeaker", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "blood-of-the-ancients"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "divine-judgment" },
  { anchor = "circumvent-obfuscation" },
]
trades = [
  { alters = "Domains", feature = "domains", by = ["divine-judgment"] },
]
+++

The Umani priest-judges presided over justice in ancient Yamasa, driven by a zeal for discovering
the truth. After the fall of Yamasa and the rise of hostile Koboto tribes in its place, the
surviving Umani spread their philosophy of certain and unwavering justice throughout the Inner Sea
region.

## Alignment {#alignment}

A lawspeaker must be lawful.

## Divine Judgment {#divine-judgment}

A lawspeaker must select the Law domain or any subdomain of Law offered by her deity. She does not
gain a second domain.

This alters domains.

## Circumvent Obfuscation (Sp) {#circumvent-obfuscation}

As a standard action, a lawspeaker can expend two uses of channel energy to expose truths and banish
falsehoods. The energy manifests as a [spell-like ability](ref/umr/spell-like-abilities), and this
action does not count as channeling for the purposes of abilities and feats. Unless listed
otherwise, the resulting abilities use the lawspeaker's cleric level as her caster level and have
the same range and required components as the corresponding spell. The spell-like abilities
available are cumulative and are listed below at the level at which the lawspeaker can first access
them.

Level 1: _Calm emotions._

Level 3: _Zone of truth_.

Level 5: _Invisibility purge_.

Level 7: _Discern lies_.

Level 9: _True seeing_ (self only).

Level 11: _Greater dispel magic_ (30-foot [burst](ref/misc/burst); targets only illusion spells,
polymorph effects, and spells granting a bonus on Bluff and Disguise checks).

Level 13: _Communal tongues_.

Level 15: _Discern location_.

Level 17: _Antimagic field_ (30-foot radius).
