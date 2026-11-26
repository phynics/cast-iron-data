+++
id = "ref/arc-medium/voice-of-the-void"
kind = "archetype"
title = "Voice of the Void"
aon = "ArchetypeDisplay.aspx?FixedName=Medium%20Voice%20of%20the%20Void"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "voice_of_the_void", path = "json/archetypes_medium.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/medium" },
]
[[sources]]
publication = "villain-codex"
page = "212"

[fields]
kind = "archetype"
features = [
  { anchor = "emissary", level = 1 },
  { anchor = "surge-of-the-void", level = 1 },
  { anchor = "blasphemy" },
  { anchor = "void-channeler", level = 3 },
]
trades = [
  { replaces = "Haunt channeler", feature = "haunt-channeler", by = ["void-channeler"] },
  { alters = "Spirit", feature = "spirit", by = ["emissary"] },
  { alters = "Spirit surge", feature = "spirit-surge", by = ["surge-of-the-void"] },
  { alters = "Taboo", feature = "taboo", by = ["blasphemy"] },
]
+++

Some mediums delve deeply into the spirit world and make contact with entities that exist outside
the boundaries of the sane multiverse. Ageless and forever waiting, these beings offer immense
power, but the risks are also great.

## Emissary (Su) {#emissary}

A voice of the void channels entities called emissaries, which emulate the six legends but possess a
different kind of inscrutable, alien power. They originate in a place that no mortal mind can
comprehend, and their power merely passes through the astral realm to reach the medium. For each
point of influence an emissary gains over a medium, the medium takes a -1 penalty on Will saves,
Wisdom checks, and Wisdom-based skill checks, in addition to the other penalties imposed by the
emissary's influence. If an emissary gains enough influence to take control of him, when the medium
awakens, in addition to performing the bidding of the alien entity, he retains faint memories of
horrible things in dark places and takes 2d4 points of
[Wisdom damage](ref/rule/ability-damage-drain).

This ability alters spirit.

## Surge of the Void (Su) {#surge-of-the-void}

The voice of the void can use spirit [surge](ref/umr/surge) additional times per day without
incurring influence, but each time he does, he is [confused](ref/misc/confused) for 1 round. If this
confusion would cause him to babble, he can instead act normally, but his emissary gains 1 point of
influence over him. The voice of the void can't use this ability if he is immune to confusion, but
he can remove the confused condition when he is affected by it. This temporary confusion clearly
indicates the voice of the void isn't fully in control, so if he uses this power on a Diplomacy
check in a negotiation, for example, it might prejudice the other party against him regardless of
his check result.

This ability modifies spirit surge.

## Blasphemy (Ex) {#blasphemy}

Emissaries demand that a medium perform acts appealing to their alien whims. These work just like
taboos for an ordinary medium, but in addition to the base taboo, they require bizarre and alien
acts that distance the voice of the void from his own humanity. These blasphemies cause the medium
to take a -1 penalty on Charisma checks and Charisma-based skill checks whenever he accepts a taboo.
The increased devotion required to maintain a [blasphemy](ref/spell/blasphemy) reaps a greater
reward, however. If the voice of the void is under a [blasphemy](ref/spell/blasphemy), the die for
his spirit [surge](ref/umr/surge) changes from 1d6 to 1d8, increasing to 1d10 at 10th level and 1d12
at 20th level.

This ability alters taboo.

## Void Channeler (Su) {#void-channeler}

At 3rd level, the voice of the void can funnel energy from the emissaries' realm through himself. A
number of times per day equal to his Charisma modifier, the medium can unleash a
[burst](ref/misc/burst) of energy that damages all other creatures except aberrations within 30 feet
of him. The burst deals 1d6 points of damage + 1d6 additional points of damage for every 2 medium
levels the medium has beyond 3rd.

Creatures receive a Will save to halve the damage (DC = 10 + 1/2 the medium's level + the medium's
Charisma modifier). Creatures with fewer HD than half the medium's level who fail the Will save are
also confused for 1d4 rounds.

This ability replaces haunt channeler.
