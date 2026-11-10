+++
id = "ref/arc-paladin/soul-sentinel"
kind = "archetype"
title = "Soul Sentinel"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Soul%20Sentinel"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soul_sentinel", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "horror-adventures"
page = "65"

[fields]
kind = "archetype"
replaces = ["6th-level mercy", "Aura of justice", "12th-level mercy"]
replaces_features = ["aura-of-justice"]
+++

In a world of horrors, some holy warriors fight to safeguard the minds and spirits of those exposed
to evil. Soul sentinels use the strength of their resolve to stem the tide of corruption and
insanity, as they believe that the greatest tragedy is a soul lost to evil when it was within their
power to save it.

**Reprieve (Su)**

**Flavor:** A soul sentinel relieves manic and tortured souls exposed to the harsh evil of the
world.

**At 6th Level:** When the soul sentinel uses her _lay on hands_ ability to heal a living creature,
she can remove [confusion](ref/misc/confused) effects in place of applying one of her other mercies.
If used on a creature suffering from a permanent confusion effect, this removes the effect for only
1 minute.

**Replaces:** 6th-level mercy

**Sacred Soul (Su)**

**Gained:** At 11th Level

**Passive:** A sacred soul is immune to hexes and curse spells or abilities. Each ally within 10
feet of her gains a +4 morale bonus on saving throws against hexes or curses.

**Replaces:** Aura of justice

**Special:** This ability functions only while the paladin is conscious, not if she is unconscious
or dead.

**Greater Reprieve (Su)**

**Flavor:** The soul sentinel suppresses the stain of corruption on the spirits of those she heals.

**At 12th Level:** At 12th level, whenever she uses her _lay on hands_ ability to heal a living
creature (other than herself) or damage an undead creature, in place of applying one of her other
mercies, she can suppress the stain from a [corrupted](ref/rule/corruption) creature's most recent
manifestation for 1 minute. Any gift from that manifestation is unaffected and remains available,
unless the manifestation has a special note requiring the gift and stain be taken together, in which
case greater reprieve also suppresses the gift.

**Replaces:** 12th-level mercy
