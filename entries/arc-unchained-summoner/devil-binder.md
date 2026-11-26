+++
id = "ref/arc-unchained-summoner/devil-binder"
kind = "archetype"
title = "Devil Binder"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20%28Unchained%29%20Devil%20Binder"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "devil_binder", path = "json/archetypes_summoner_UC.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/unchained-summoner" },
]
[[sources]]
publication = "adventurers-guide"
page = "94"

[fields]
kind = "archetype"
features = [
  { anchor = "infernal-binding", level = 1 },
  { anchor = "infernal-arcana", level = 1 },
  { anchor = "infernal-affinity", level = 2 },
  { anchor = "smite-chaos", level = 6 },
]
trades = [
  { replaces = "Summon monster I", feature = "summon-monster-i", by = ["infernal-arcana"] },
  { replaces = "Bond senses", feature = "bond-senses", by = ["infernal-affinity"] },
  { replaces = "shield ally", feature = "shield-ally", by = ["infernal-affinity"] },
  { replaces = "transposition", feature = "transposition", by = ["infernal-affinity"] },
  { replaces = "greater shield ally", feature = "greater-shield-ally", by = ["infernal-affinity"] },
  { replaces = "merge forms", feature = "merge-forms", by = ["infernal-affinity"] },
  { replaces = "twin eidolon", feature = "twin-eidolon", by = ["infernal-affinity"] },
  { replaces = "Maker's call", feature = "maker-s-call", by = ["smite-chaos"] },
  { replaces = "eidolon's devotion ability", by = ["smite-chaos"] },
  { alters = "Eidolon", feature = "eidolon", by = ["infernal-binding"] },
]
+++

While many assume [Hellknights](ref/rule/aff-lawknights) are worshipers or agents of devilkind—or,
at best, duped puppets of the infernal realm—most Hellknights see Hell and its native devils as a
challenge to be conquered. If one can dominate these beings of pure (albeit cruel) law, then the
power of that law is theirs by right. While the Test undertaken by those who seek to become full
Hellknights is one method by which this power is earned, the devil binder takes this philosophy a
step further, forcing a devil into service.

Unlike those of most summoners, a devil binder's eidolon does not willingly serve its master due to
a similar philosophical bent. While some devil binders (especially those who do serve Hell) seek
more amicable relationships with these infernal servants, others treat their eidolons as mere tools,
remorselessly ordering the devils into battle. The nature of the summoner's magical bond is
irrevocably altered by their style of invocation. A devil binder borrows extraplanar quintessence
from her eidolon, gaining strange abilities for herself and evolving her eidolon's magical powers.

## Alignment {#alignment}

The infernal bargains and rituals a devil binder pursues leave an indelible stain upon her soul. A
devil binder must be lawful [evil](ref/subtype/evil) or lawful neutral in alignment.

## Infernal Binding (Ex) {#infernal-binding}

A devil binder must select an eidolon of the [devil](ref/eidolon/devil) subtype. The devil binder's
eidolon never increases its maximum number of attacks, and its base attack bonus is equal to half
its Hit Dice. At 4th level and every 4 levels thereafter, the eidolon's Charisma score increases
by 2.

This alters the summoner's eidolon.

## Infernal Arcana (Sp) {#infernal-arcana}

At 1st level and every 2 levels thereafter, the devil binder's eidolon gains the following
[spell-like abilities](ref/umr/spell-like-abilities): _protection from chaos_ (1st), _scorching ray_
(3rd), _suggestion_ (5th), _charm monster_ (7th), _dominate person_ (9th),
_[planar binding](ref/spell/planar-binding)_ (devils only) (11th), _greater teleport_ (13th), _power
word stun_ (15th), _meteor swarm_ (17th). Each of these
[spell-like abilities](ref/umr/spell-like-abilities) is usable once per day, and the eidolon's
caster level is equal to the devil binder's summoner level. When the eidolon casts _planar binding_
this way, the devil binder is considered to be the spell's caster instead. At 19th level, the devil
binder's eidolon can use each of its infernal arcana
[spell-like abilities](ref/umr/spell-like-abilities) three times per day.

This replaces the summon monster I summoner class feature.

## Infernal Affinity (Ex, Su, or Sp) {#infernal-affinity}

A devil binder wrenches Hell's power from her eidolon. This grants the devil binder the bloodline
powers of the [infernal](ref/sorcbloodline/infernal) sorcerer bloodline (gained at the following
levels): corrupting touch (4th), infernal resistances (8th), hellfire (12th), on dark wings (16th),
and power of the Pit (20th). The devil binder treats her summoner level as her sorcerer level for
the purpose of determining their effects.

This replaces bond senses, shield ally, transposition, greater shield ally, merge forms, and twin
eidolon.

## Smite Chaos (Su) {#smite-chaos}

At 6th level, the summoner's eidolon gains the ability to smite chaos as a
[Hellknight](ref/pclass/hellknight) (see page 90) of its Hit Dice. This ability can be used once per
day and an additional time for every 4 levels beyond 6th.

This ability replaces maker's call and the eidolon's devotion ability.
