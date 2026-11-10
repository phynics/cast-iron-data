+++
id = "ref/arc-cavalier/esquire"
kind = "archetype"
title = "Esquire"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Esquire"
source_ids = ["cohorts-and-companions"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "esquire", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "cohorts-and-companions"
page = "30"

[fields]
kind = "archetype"
replaces = ["Mount", "Cavalier's charge", "Expert trainer", "Mighty charge", "Supreme charge"]
alters = ["Banner"]
+++

The esquire is a roving knight who acquires the services of a faithful follower - an
aide-de-camp-who serves as the esquire's assistant, spear carrier, and guard.

**Aide-de-Camp (Ex)**

**Action:** Ability

**Gained:** At 3rd Level

**Replaces:** Mount

An esquire acquires the services of a loyal aide-de-camp. This NPC functions similarly to a cohort
(as the [Leadership](ref/feat/leadership) feat), though the aide-de-camp must advance in a class
that grants proficiency with all martial weapons and cannot multiclass until the esquire reaches 7th
level (though the aide-de-camp can select an archetype). If the aide-de-camp is a cavalier, he must
follow the same order as the esquire.

The aide-de-camp gains [Swift Aid](ref/feat/swift-aid) as a bonus feat, and provides a +2 (rather
than +1) bonus when using this feat to aid the esquire. As a **move action,** the aide-de-camp can
retrieve a stored item or an item on the ground and hand it to the esquire. The esquire does not
have to take an action to receive the item, though he must be conscious and have a free hand. This
action does not provoke attacks of opportunity for the aide-de-camp or esquire.

If the aide-de-camp dies performing an act that directly supports the edicts of the esquire's order
(GM's discretion), the esquire does not take a penalty to his Leadership score. If an aide-de-camp
dies, or is released from the esquire's service, the esquire may gain a new aide-de-camp by scouting
for potential candidates in a city or large town. This requires 1 day per 5 levels of the
aide-de-camp to be recruited.

**Teamwork (Ex)**

**Gained:** At 3rd Level

**Passive:** As long as an esquire and his aide-de-camp are adjacent, the aide-de-camp is treated as
having any teamwork feats the esquire has. They also share any teamwork feats that function when two
or more allies threaten the same target, as long as they both threaten the same target.

**Replaces:** Cavalier's charge

**Shared Challenge (Ex)**

**Ability:** Whenever an esquire challenges an opponent when his aide-de-camp is within 30 feet, he
may grant his aide-de-camp bonuses equal to one-half of the bonuses he gains from _challenge,_
including bonuses derived from the cavalier's order. If the aide-de-camp is also a cavalier and
challenges the same target, these bonuses do not stack. Like the esquire, his aide-decamp takes a -2
penalty to Armor Class against attacks from creatures other than the challenged opponent.

**Gained:** At 4th Level

**Replaces:** Expert trainer

**Banner (Ex)**

**Alters:** Banner

**Passive:** An aide-de-camp can carry an esquire's banner for him and still grant allies within
range the banner's bonuses. While doing so the aide-de-camp gains double the normal morale bonuses
provided by the banner.

**Avenge Me (Ex)**

**Gained:** At 11th Level

**Passive:** Whenever the esquire is killed, dying, stunned, dazed, or otherwise unable to take
actions, his aide-de-camp gains the full benefits of the esquire's _challenge_ and _order_ abilities
against all creatures that attacked the esquire in the previous round. If the aide-de-camp is also a
cavalier and challenges the same target, these bonuses do not stack. These benefits last until the
esquire regains the ability to take actions, or until the aide-de-camp or the triggering opponents
are killed.

**Replaces:** Mighty charge

**Special:** If his aide-de-camp is killed, dying, or otherwise unable to take actions the esquire
may declare one creature of his choice that attacked the aide-de-camp in the past round as his
_quarry;_ this functions identically to the [ranger](ref/class/ranger) class ability. These bonuses
last until the aide-de-camp recovers or until the cavalier or the triggering opponents are killed.

**Fight As One (Ex)**

**Gained:** At 20th Level

**Passive:** The _shared challenge_ ability increases in power, granting the aide-de-camp full
benefit of the esquire's _challenge._ In addition, if the esquire and aide-de-camp both confirm a
critical hit against the same target within the same round, the target must make a Fortitude save
(DC 10 + [half](ref/misc/fractions-and-rounding) the esquire's cavalier level + the esquire's
Charisma bonus) or be [staggered](ref/misc/staggered) for 1d4 rounds.

**Replaces:** Supreme charge
