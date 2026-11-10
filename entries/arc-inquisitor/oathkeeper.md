+++
id = "ref/arc-inquisitor/oathkeeper"
kind = "archetype"
title = "Oathkeeper"
source_ids = ["merchants-manifest"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "oathkeeper", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "merchants-manifest"
page = "30"

[fields]
kind = "archetype"
replaces = ["Monster lore", "Track"]
alters = ["Alignment requirements"]
+++

Servants of gods who hold oaths to be sacrosanct, oathkeepers formally oversee the creation of
bargains and personally hunt down those who dare to violate them. Many of these inquisitors
previously oversaw religious vows in more formal settings, though more pursue more lucrative
contracts. Wronged merchants or cheated customers often seek out oathkeepers to bring justice when
local authorities fail.

**Alignment**

**Alters:** Alignment requirements

**Info:** An oathkeeper must be of a lawful alignment, and her alignment must be within one step of
her deity's.

**Gained class skills:** app

**Lost class skills:** kna

**Divine Witness (Su)**

**Action:** Ability

**Replaces:** Monster lore

Every oathkeeper inquisitor develops a unique personal symbol, which she can use to seal an
agreement between two or more willing parties. The agreement, whether it's a trade contract, a
truce, or a political marriage, must be as detailed as possible and then signed in the oathkeeper's
presence by every creature involved. Creatures must sign of their own free will - any magical or
physical coercion will cause the contract to crumble into ash when the oathkeeper attempts to place
her seal upon it. So long as no mystic or physical force is influencing any participating creature,
the oathkeeper can mystically seal the arrangement with her personal symbol, binding all signing
parties into upholding their ends of the bargain for the length of time spelled out in the
agreement.

Should any oathbound creature break the exact wording of the contract, the agreement is dissolved
and the offending creature is cursed, taking a penalty on all d20 rolls equal to the oathkeeper's
Wisdom modifier for a number of weeks equal to the oathkeeper's inquisitor level. Furthermore, the
inquisitor's symbol appears as a mystic symbol on the offending creature's throat and hands,
allowing the oathkeeper to know the creature's location at all times, as per the
[discern location](ref/spell/discern-location) spell.

If a creature is forced into breaking the agreement by magic or overwhelming physical force (for
example, breaking an agreement not to harm via a [compulsion](ref/spelldef/compulsion) spell or by
physically hurling an oathbound creature to deal damage to another), then the agreement dissipates
harmlessly. The oathkeeper's curse is a curse effect, but it can be removed only with a
[miracle](ref/spell/miracle) or [wish](ref/spell/wish) spell.

**Oathbreaker's Scourge (Su)**

**Ability:** If an oathkeeper is given physical evidence of a broken agreement and asked to hunt
down the contract's breaker by the offended party, the oathkeeper gains a +4 sacred or profane bonus
on Diplomacy and Survival skill checks to gather information about and track the target. The
inquisitor is also treated as being 3 levels higher for the purpose of one judgment she uses against
the deal breaker, so long as she keeps possession of the evidence.

**Gained:** At 2nd Level

**Replaces:** Track

**Special:** If the oathkeeper uses oathbreaker's scourge when attacking someone who is actually
innocent of fraud - due to forgery, hasty judgments, or other deceptions - she loses access to all
of her oathkeeper archetype abilities for 1 month or until she is the target of an
[atonement](ref/spell/atonement) spell.
