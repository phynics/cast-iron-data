+++
id = "ref/arc-inquisitor/exarch"
kind = "archetype"
title = "Exarch"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "exarch", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]

[fields]
kind = "none"
+++

**Sources:** Advanced Race Guide pg 13\
The gruff traditionalism of most dwarves finds its apex in those who adhere to a strict orthodoxy
rooted in ancient principles and practices and who are not amenable whatsoever to change or
innovation.

**Prerequisites:** Dwarf

**Spells**

**Alters:** Spellcasting

**Info:** Exarchs cannot cast spells with the chaotic descriptor.

**Inflexible Will (Ex)**

**Gained:** At 1st Level

**Passive:** An exarch gains a +2 bonus on saving throws against [confusion](ref/spell/confusion)
and [insanity](ref/spell/insanity) effects and effects with the chaotic descriptor.

**Replaces:** Monster lore

**Detect Chaos (Sp)**

**Ability:** At will, an exarch can use [detect chaos](ref/spell/detect-chaos).

**Replaces:** Detect alignment

**Fearsome Jurist (Su)**

**Gained:** At 5th Level

**Replaces:** Bane

**Swift:** An exarch can imbue one of her weapons with the [jurist](ref/magic-enh/jurist) or
[menacing](ref/magic-enh/menacing) weapon special ability, and may switch between these properties
as another swift action. When using either special ability, her weapon's critical threat range
doubles against chaotic creatures. This does not stack with [keen edge](ref/spell/keen-edge),
[Improved Critical](ref/feat/improved-critical), or similar effects. This ability otherwise
functions as _[bane](ref/spell/bane)._

**Aura of Repetition (Su)**

**Gained:** At 8th Level

**Replaces:** Second judgment

**Special:** If the exarch takes Artifice (Toil) as her domain, the save DC of her aura increases by
2 but its duration does not increase.

**Standard:** Once per day while using her judgment, an exarch can project an _aura of repetition,_
as the Toil subdomain power.

**Double Jeopardy (Su)**

**Gained:** At 12th Level

**Passive:** Whenever an exarch uses her _fearsome jurist_ ability, she may choose to affect two
weapons, with one gaining the _jurist_ weapon special ability and the other the _menacing_ special
ability as above. Both special abilities may be combined in a single weapon, whose critical threat
range doubles. This does not stack with _[keen edge](ref/spell/keen-edge),_ Improved Critical, or
similar effects.

**Replaces:** Greater bane

**Aura of Reversion (Su)**

**Ability:** While using her judgment, an exarch can project a 30-foot-radius
[emanation](ref/misc/emanation) for a number of rounds per day equal to her inquisitor level. Any
creature other than the exarch that is using a transmutation effect within this aura at the
beginning of its turn becomes [sickened](ref/misc/sickened), or sickened and
[nauseated](ref/misc/nauseated) if using a polymorph effect, including the
[change shape](ref/umr/change-shape) ability (Fortitude negates; DC 10 + 1/2 the exarch's level +
her Wisdom modifier). Continuous effects from permanent magical items do not cause this effect.
Within the aura, [dispel](ref/spell/dispel-magic) checks against transmutation effects gain a +4
bonus. This ability cannot be used simultaneously with _aura of repetition._

**Gained:** At 16th Level

**Replaces:** Third judgment
