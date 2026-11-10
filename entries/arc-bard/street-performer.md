+++
id = "ref/arc-bard/street-performer"
kind = "archetype"
title = "Street Performer"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Street%20Performer"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "street_performer", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "advanced-players-guide"
page = "85"

[fields]
kind = "archetype"
replaces = ["Inspire courage", "Inspire competence", "Inspire greatness", "Inspire heroics", "Countersong", "Bardic knowledge", "Lore master"]
replaces_features = ["bardic-knowledge", "lore-master"]
+++

Whether acrobat, troubadour, or thespian, the street performer mixes with the masses, singing for
his supper.

**Bardic Performance**

**Info:** A street performer gains the following types of bardic performance.

**Disappearing Act (Su)**

**At 1st Level:** A street performer can use performance to divert attention from an ally. All
creatures within 30 feet that fail a Will save (DC 10 + [half](ref/misc/fractions-and-rounding) the
bard's level + the bard's Cha modifier) treat one creature chosen by the bard as if it were
[invisible](ref/rule/invisible).

**At 11th Level:** The bard can render three allies invisible.

**At 17th Level:** The bard can now affect four allies.

**At 5th Level:** This performance now affects two allies.

**Replaces:** Inspire courage

**Special:** If the targets take any action that would cause them to become visible, they become
visible to everyone. The bard cannot use this ability on himself. This ability is a mind-affecting
effect that requires visual components.

**Harmless Performer (Su)**

**At 3rd Level:** A street performer can use performance to appear meek and unworthy of being
attacked. While using this performance, whenever an enemy targets the street performer, the enemy
must succeed at a Will save (DC 10 + 1/2 the bard's level + the bard's Cha bonus) or be unable to
attack the bard this round, as per [sanctuary](ref/spell/sanctuary). The enemy loses the attack that
targeted the bard, but may spend additional attacks targeting other creatures. If the opponent was
targeting the street performer with a spell, it must succeed at a
[concentration](ref/rule/concentration) check at the same DC or lose the spell. If this check
succeeds, it may target another creature with the spell instead.

**Replaces:** Inspire competence

**Special:** This mind-affecting ability requires audible or visual components.

**Madcap Prank (Su)**

**At 9th Level:** A street performer can use performance to discomfit a target within 30 feet,
causing its clothing to become tangled, its headgear to fall down over its eyes, or even causing it
to slip and fall or otherwise be made to appear a fool. The target must make a Reflex save (DC 10 +
1/2 the bard's level + the bard's Cha modifier) each round that it hears or sees the performance, or
it takes one of the following random effects each round: 1-[blinded](ref/misc/blinded),
2-[dazzled](ref/misc/dazzled), 3-[deafened](ref/misc/deafened), 4-[entangled](ref/rule/entangled),
5-fall [prone](ref/rule/prone), 6-[nauseated](ref/misc/nauseated). Each effect lasts 1 round.

**Replaces:** Inspire greatness

**Slip through the Crowd (Su)**

**At 15th Level:** A street performer's disappearing act enables affected creatures to move through
crowd squares and enemy-occupied squares without impediment. Affected creatures are treated as if
having [greater invisibility](ref/spell/invisibility-greater), but enemies gain a new saving throw
to notice them each time they are attacked.

**Replaces:** Inspire heroics

**Gladhanding**

**Ability:** A street performer earns double the normal amount of money from
[Perform](ref/skill/perform-any) checks.

**Replaces:** Countersong

**Standard:** He may use a Bluff check in place of a Diplomacy check to improve a creature's
attitude for 1 minute, after which its attitude becomes one step worse than originally.

**Streetwise**

**Passive:** A street performer gains a bonus equal to half his level on Bluff, Disguise, Knowledge
(local), and Sleight of Hand checks, Diplomacy or Intimidate checks made to influence crowds, and
Diplomacy checks to gather information (minimum +1).

**Replaces:** Bardic knowledge

**Quick Change (Ex)**

**Ability:** He can Take 20 on a Bluff or Disguise check once per day.

**At 11th Level:** He can Take 20 twice a day.

**At 17th Level:** He can Take 20 three times a day.

**Gained:** At 5th Level

**Replaces:** Lore master

**Standard:** A street performer can don a disguise by taking a -5 penalty on his check.

**Swift:** He can take 10 on Bluff and Disguise checks and use Bluff to create a diversion to hide.
