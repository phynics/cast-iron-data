+++
id = "ref/arc-medium/voice-of-the-void"
kind = "archetype"
title = "Voice of the Void"
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
replaces = ["Haunt channeler"]
alters = ["Spirit", "Spirit surge", "Taboo"]
replaces_features = ["haunt-channeler"]
alters_features = ["spirit", "spirit-surge", "taboo"]
+++

Some mediums delve deeply into the spirit world and make contact with entities that exist outside
the boundaries of the sane multiverse. Ageless and forever waiting, these beings offer immense
power, but the risks are also great.

**Emissary (Su)**

**Ability:** A voice of the void channels entities called emissaries, which emulate the six legends
but possess a different kind of inscrutable, alien power. They originate in a place that no mortal
mind can comprehend, and their power merely passes through the astral realm to reach the medium. For
each point of influence an emissary gains over a medium, the medium takes a -1 penalty on Will
saves, Wisdom checks, and Wisdom-based skill checks, in addition to the other penalties imposed by
the emissary's influence. If an emissary gains enough influence to take control of him, when the
medium awakens, in addition to performing the bidding of the alien entity, he retains faint memories
of horrible things in dark places and takes 2d4 points of
[Wisdom damage](ref/rule/ability-damage-drain).

**Alters:** Spirit

**Surge of the Void (Su)**

**Ability:** The voice of the void can use _spirit surge_ additional times per day without incurring
influence, but each time he does, he is [confused](ref/misc/confused) for 1 round. If this confusion
would cause him to babble, he can instead act normally, but his emissary gains 1 point of influence
over him. The voice of the void can't use this ability if he is immune to confusion, but he can
remove the confused condition when he is affected by it.

**Alters:** Spirit surge

**Special:** This temporary confusion clearly indicates the voice of the void isn't fully in
control, so if he uses this power on a Diplomacy check in a negotiation, for example, it might
prejudice the other party against him regardless of his check result.

**Blasphemy (Ex)**

**Ability:** Emissaries demand that a medium perform acts appealing to their alien whims. These work
just like _taboos_ for an ordinary medium, but in addition to the base _taboo,_ they require bizarre
and alien acts that distance the voice of the void from his own humanity. These blasphemies cause
the medium to take a -1 penalty on Charisma checks and Charisma-based skill checks whenever he
accepts a _taboo._ The increased devotion required to maintain a _[blasphemy](ref/spell/blasphemy)_
reaps a greater reward, however. If the voice of the void is under a
_[blasphemy](ref/spell/blasphemy),_ the die for his _spirit surge_ changes from 1d6 to 1d8.

**Alters:** Taboo

**At 10th Level:** The _[surge](ref/umr/surge)_ die becomes 1d10.

**At 20th Level:** The _[surge](ref/umr/surge)_ die becomes 1d12.

**Void Channeler (Su)**

**Ability:** The medium can unleash a [burst](ref/misc/burst) of energy that damages all other
creatures except aberrations within 30 feet of him. The burst deals 1d6 points of damage. Creatures
receive a Will save to halve the damage (DC = 10 + 1/2 the medium's level + the medium's Charisma
modifier). Creatures with fewer HD than half the medium's level who fail the Will save are also
confused for 1d4 rounds.

**Flavor:** The voice of the void can funnel energy from the emissaries' realm through himself.

**Gained:** At 3rd Level

**Replaces:** Haunt channeler

**Usage:** Charisma modifier times/day

At 5th level: The damage 2d6.

At 7th level: The damage 3d6.

At 9th level: The damage 4d6.

At 11th level: The damage 5d6.

At 13th level: The damage 6d6.

At 15th level: The damage 7d6.

At 17th level: The damage 8d6.

At 19th level: The damage 9d6.
