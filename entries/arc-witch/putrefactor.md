+++
id = "ref/arc-witch/putrefactor"
kind = "archetype"
title = "Putrefactor"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "putrefactor", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]

[fields]
kind = "none"
+++

**Sources:** Blood of the Coven pg 16\
Some witches find their patrons while in the throes of despair and grief, when all they desire is to
see the veneer of civilization peel back to reveal the filth and rot that underlies all things. The
arcane power they inherit is bleak and tainted, eating them from the inside out and transforming
them into living avatars of entropy.

**Infestation of Entropy**

**Alters:** Familiar, patron

**Choice:** A putrefactor must be of chaotic alignment and must choose one of the following patrons:
[Animals](ref/patron/animals), [Death](ref/patron/death), [Plague](ref/patron/plague), or
[Rot](ref/patron/rot).

**Info:** A putrefactor's body hosts various pests - insects, rats, or other scavengers - as part of
her connection with her patron. She treats the infestation as her familiar, and she communes with
the infestation to prepare spells. She still selects a familiar, which must be a
[house centipede](ref/monster/familiar-house-centipede), [rat](ref/monster/familiar-rat),
[scarlet spider](ref/carried/ultimate-magic/monsters/new-familiars/small-and-vermin-familiars/familiar/spider/scarlet),
or [toad](ref/monster/familiar-toad); the familiar crawls within her among the other vermin.

**Disgorge Familiar (Ex)**

**Info:** While within her, the familiar cannot be targeted for effects or take any action, but
effects affecting it persist, and their duration continues until the next time she disgorges it.

**Replaces:** 1st-level hex

**Standard:** A putrefactor can cough up her familiar, allowing it to act as a separate entity. She
can also devour it again as a standard action when the familiar is within reach.

**Verminous Blood (Ex)**

**Flavor:** The swarming creatures within a putrefactor begin to replace her bodily fluids.

**Gained:** At 2nd Level

**Passive:** Whenever she takes slashing or piercing damage from a melee attack, the creatures spill
out and bite the attacker, dealing 1d6 points of damage, which count as damage from a Diminutive
[swarm](ref/subtype/swarm). A creature can take damage from this ability only once per round.

**Replaces:** 2nd-level hex

At 12th level: This damage 2d6.

At 20th level: This damage 3d6.

**Putrefied Innards (Ex)**

**Flavor:** The infestation begins assuming various functions of the witch's organs.

**At 10th Level:** This increases to a 50% chance (as per
[moderate fortification](ref/magic-enh/fortification-moderate)).

**At 16th Level:** This increases to a 75% chance (as per
[heavy fortification](ref/magic-enh/fortification-heavy)).

**At 4th Level:** She gains a 25% chance to negate the extra damage from critical hits and sneak
attacks, as per the [light fortification](ref/magic-enh/fortification-light) magic armor ability.

**Replaces:** 4th-, 10th-, and 16th-level hexes

**Special:** Whenever the putrefactor negates additional damage from a melee attack in this way, the
attacker takes damage as if exposed to her _verminous blood,_ even if it has already been targeted
by this ability this round.

**Disgorge Swarm (Ex)**

**Gained:** At 6th Level

**Replaces:** 6th-level hex

**Special:** The witch can target creatures with her hexes as if she occupied both the swarm's space
and her own. When the duration ends, the swarm tries its best to return to her and crawl back into
her body, restoring hit points equal to its current hit points, up to her maximum hit points. If the
swarm dies or cannot return to her once the spell's duration ends, the witch does not regain any of
her spent hit points. Once she reabsorbs the swarm, she can't disgorge it again for 1 hour.

**Standard:** While her familiar is inside her, the putrefactor can disgorge all the crawling
creatures within her at once, retaining only her familiar. When she does, she loses 2 hit points per
class level and forms a spider swarm as per the spell [vomit swarm](ref/spell/vomit-swarm). The
swarm gains the Armor Class and saving throw bonuses of her familiar. The swarm deals her _verminous
blood_ damage instead of its normal damage; while the swarm lasts, the putrefactor loses access to
her _verminous blood_ ability.
