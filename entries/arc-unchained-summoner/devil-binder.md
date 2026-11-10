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
replaces = ["Summon monster I", "Bond senses", "shield ally", "transposition", "greater shield ally", "merge forms", "twin eidolon", "Maker's call", "eidolon's devotion ability"]
alters = ["Eidolon"]
replaces_features = ["summon-monster-i", "bond-senses", "shield-ally", "transposition", "greater-shield-ally", "merge-forms", "twin-eidolon", "maker-s-call"]
alters_features = ["eidolon"]
+++

While many assume [Hellknights](ref/rule/aff-lawknights) are worshipers or agents of devilkind - or,
at best, duped puppets of the infernal realm - most Hellknights see Hell and its native devils as a
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

**Alignment**

**Info:** The infernal bargains and rituals a devil binder pursues leave an indelible stain upon her
soul. A devil binder must be lawful evil or lawful neutral in alignment.

**Infernal Binding (Ex)**

**Alters:** Eidolon

**Info:** A devil binder must select an eidolon of the [devil](ref/eidolon/devil) subtype. The devil
binder's eidolon never increases its maximum number of attacks, and its base attack bonus is equal
to half its Hit Dice.

**Repeat:** The eidolon's Charisma score increases by 2., 4, 4

**Infernal Arcana (Sp)**

**At 19th Level:** The devil binder's eidolon can use each of its _infernal arcana_
[spell-like abilities](ref/umr/spell-like-abilities) three times per day.

**Info:** The devil binder's eidolon gains the following
[spell-like abilities](ref/umr/spell-like-abilities) at the listed summoner level.

**Replaces:** Summon monster I

**Spells:** Protection from chaos

**Spells:** Planar binding\|(devils only)

**Spells:** Greater teleport

**Spells:** Power word stun

**Spells:** Meteor swarm

**Spells:** Scorching ray

**Spells:** Suggestion

**Spells:** Charm monster

**Spells:** Dominate person

**Special:** Each of these [spell-like abilities](ref/umr/spell-like-abilities) is usable once per
day, and the eidolon's caster level is equal to the devil binder's summoner level. When the eidolon
casts _[planar binding](ref/spell/planar-binding)_ this way, the devil binder is considered to be
the spell's caster instead.

**Infernal Affinity (Ex, Su, or Sp)**

**At 12th Level:** Hellfire

**At 16th Level:** On dark wings

**At 20th Level:** Power of the Pit

**At 4th Level:** Corrupting touch

**At 8th Level:** Infernal resistances

**Info:** A devil binder wrenches Hell's power from her eidolon. This grants the devil binder the
bloodline powers of the [infernal](ref/sorcbloodline/infernal) sorcerer bloodline (gained at the
following levels).

**Replaces:** Bond senses, shield ally, transposition, greater shield ally, merge forms, twin
eidolon

**Special:** The devil binder treats her summoner level as her sorcerer level for the purpose of
determining their effects.

**Smite Chaos (Su)**

**Ability:** The summoner's eidolon gains the ability to _smite chaos_ as a
[Hellknight](ref/pclass/hellknight) of its Hit Dice

**Replaces:** Maker's call, eidolon's _devotion_ ability

**Usage:** 1 time/day + 1 per 4 summoner levels beyond 6th

**Smite Chaos (Su)**

**Ability:** This ability functions as the paladin's _smite evil_ class feature but against
chaotic-aligned creatures. This ability is twice as effective against outsiders with the chaotic
subtype, chaotic-aligned aberrations, and fey.

**Flavor:** Text from the hellknight class ability.

**Smite Evil (Su)**

**Action:** Swift Action

**Flavor:** Relevant text from the paladin class ability.

You can call out to the powers of good to aid you in your struggle against evil, choosing one target
within sight to smite. If you target a creature that is not evil, the smite is wasted with no
effect.

If this target is evil, you add your Charisma bonus (if any) on your attack rolls and add your
paladin level to all damage rolls made against the target of your smite. If the target of _smite
evil_ is an [outsider](ref/type/outsider) with the [evil](ref/subtype/evil) subtype, an evil-aligned
[dragon](ref/type/dragon), an [undead](ref/type/undead) creature, or a creature with levels in
[antipaladin](ref/class/antipaladin), the bonus to damage on the first successful attack increases
to 2 points of damage per paladin level. Regardless of the target, _smite evil_ attacks
automatically bypass any DR the creature might possess.

In addition, while _smite evil_ is in effect, you gain a deflection bonus equal to your Charisma
modifier (if any) to your AC against attacks made by the target of the smite.

The _smite evil_ effect remains until the target of the smite is dead or the next time you rest and
regain your uses of this ability.
