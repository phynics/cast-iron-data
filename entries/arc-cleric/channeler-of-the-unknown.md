+++
id = "ref/arc-cleric/channeler-of-the-unknown"
kind = "archetype"
title = "Channeler of the Unknown"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Channeler%20of%20the%20Unknown"
source_ids = ["antiheros-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "channeler_of_the_unknown", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "antiheros-handbook"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "spells", level = 1 },
  { anchor = "unknown-aura", level = 1 },
  { anchor = "channel-entropy", level = 1 },
  { anchor = "power-of-the-unknown", level = 1 },
  { anchor = "spontaneous-casting", level = 1 },
]
trades = [
  { replaces = "Aura", feature = "aura", by = ["unknown-aura"] },
  { alters = "Weapon and armor proficiency", feature = "weapon-and-armor-proficiencies" },
  { alters = "Spells", feature = "spells", by = ["spells"] },
  { alters = "Channel energy", feature = "channel-energy", by = ["channel-entropy"] },
  { alters = "Domains", feature = "domains", by = ["power-of-the-unknown"] },
  { alters = "Spontaneous casting", feature = "spontaneous-casting", by = ["spontaneous-casting"] },
]
+++

While most clerics who fall out of favor with their deities simply lose their divine connection and
the powers it granted, a few continue to go through the motions of prayer and obedience, persisting
in the habits of faith even when their faith itself has faded. Among these, an even smaller number
find that while their original deity no longer answers their prayers, something else does: an
unknown entity or force of the universe channeling its power through a trained and practicing
vessel.

This is an ex-class archetype and can be taken by a character immediately upon becoming an
ex-cleric.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A channeler of the unknown loses proficiency with her deity's favored weapon. She instead gains
proficiency with one martial or exotic weapon, chosen when she first takes this archetype, which
thereafter effectively functions as her holy or unholy symbol for the purposes of class abilities
and spellcasting. The weapon chosen cannot be one associated with her former deity. Once she makes
this choice, she can't later change it.

This alters the cleric's weapon and armor proficiency.

## Spells {#spells}

A channeler of the unknown has one fewer spell slot per spell level in which she can prepare spells
than normal. She is no longer restricted by alignment descriptors, and she gains access to all
spells on the cleric spell list, even spells her alignment would normally prohibit.

This alters the cleric's spells.

## Unknown Aura (Su) {#unknown-aura}

A channeler of the unknown never radiates an alignment aura, as if under the effect of a permanent
_[undetectable alignment](ref/spell/undetectable-alignment)_ spell.

This replaces the cleric's aura.

## Channel Entropy (Su) {#channel-entropy}

A channeler of the unknown can channel entropy as a cleric channels negative or positive energy,
releasing a wave of twisting void that harms creatures in the area of effect. The amount of damage
dealt is equal to that an evil cleric of her level would deal by
[channeling negative energy](ref/ability/channel-energy), except it affects living, unliving, and
undead creatures alike. This functions in all other ways as a cleric's channel energy class feature,
including benefiting from feats that affect channel energy (such as
[Selective Channeling](ref/feat/selective-channeling)).

This alters channel energy.

## Power of the Unknown {#power-of-the-unknown}

A channeler of the unknown has lost the benefit of the domains granted by her deity, but the unknown
entity that answers her supplications instead grants her the benefits of one domain from the
following list: Darkness, [Destruction](ref/domain/destruction), [Luck](ref/domain/luck),
[Madness](ref/domain/madness), or [Void](ref/domain/void). Instead of a single domain spell slot,
the channeler of the unknown gains two domain spell slots per spell level she can cast. A channeler
of the unknown cannot select a subdomain in place of the domain available to her.

This alters the cleric's domains.

## Spontaneous Casting {#spontaneous-casting}

Instead of converting prepared spells into cure or inflict spells, a channeler of the unknown can
channel stored spell energy into her domain spells. She can lose a prepared spell, including a
domain spell, to spontaneously cast a domain spell of the same spell level or lower.

This alters spontaneous casting.
