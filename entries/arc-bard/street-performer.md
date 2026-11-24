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
features = [
  { anchor = "bardic-performance" },
  { anchor = "disappearing-act" },
  { anchor = "harmless-performer", level = 3 },
  { anchor = "madcap-prank", level = 9 },
  { anchor = "slip-through-the-crowd", level = 15 },
  { anchor = "gladhanding" },
  { anchor = "streetwise" },
  { anchor = "quick-change", level = 5 },
]
trades = [
  { replaces = "Inspire courage", feature = "bardic-performance", power = "inspire courage", by = ["disappearing-act"] },
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["harmless-performer"] },
  { replaces = "Inspire greatness", feature = "bardic-performance", power = "inspire greatness", by = ["madcap-prank"] },
  { replaces = "Inspire heroics", feature = "bardic-performance", power = "inspire heroics", by = ["slip-through-the-crowd"] },
  { replaces = "Countersong", feature = "bardic-performance", power = "countersong", by = ["gladhanding"] },
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["streetwise"] },
  { replaces = "Lore master", feature = "lore-master", by = ["quick-change"] },
]
+++

Whether acrobat, troubadour, or thespian, the street performer mixes with the masses, singing for
his supper.

## Bardic Performance {#bardic-performance}

A street performer gains the following types of bardic performance.

## Disappearing Act (Su) {#disappearing-act}

A street performer can use performance to divert attention from an ally. All creatures within 30
feet that fail a Will save (DC 10 + 1/2 the bard's level + the bard's Cha modifier) treat one
creature chosen by the bard as if it were _[invisible](ref/rule/invisible)_. This performance
affects one additional creature at 5th level and every 6 levels thereafter. If the targets take any
action that would cause them to become visible, they become visible to everyone. The bard cannot use
this ability on himself. This ability is a mind-affecting effect that requires visual components.
This performance replaces inspire courage.

## Harmless Performer (Su) {#harmless-performer}

At 3rd level, a street performer can use performance to appear meek and unworthy of being attacked.
While using this performance, whenever an enemy targets the street performer, the enemy must succeed
at a Will save (DC 10 + 1/2 the bard's level + the bard's Cha bonus) or be unable to attack the bard
this round, as per _[sanctuary](ref/spell/sanctuary)_. The enemy loses the attack that targeted the
bard, but may spend additional attacks targeting other creatures. If the opponent was targeting the
street performer with a spell, it must succeed at a [concentration](ref/rule/concentration) check at
the same DC or lose the spell. If this check succeeds, it may target another creature with the spell
instead. This mind-affecting ability requires audible or visual components. This performance
replaces inspire competence.

## Madcap Prank (Su) {#madcap-prank}

At 9th level, a street performer can use performance to discomfit a target within 30 feet, causing
its clothing to become tangled, its headgear to fall down over its eyes, or even causing it to slip
and fall or otherwise be made to appear a fool. The target must make a Reflex save (DC 10 + 1/2 the
bard's level + the bard's Cha modifier) each round that it hears or sees the performance, or it
takes one of the following random effects each round: 1—[blinded](ref/misc/blinded),
2—[dazzled](ref/misc/dazzled), 3—[deafened](ref/misc/deafened), 4—[entangled](ref/rule/entangled),
5—fall [prone](ref/rule/prone), 6—[nauseated](ref/misc/nauseated). Each effect lasts 1 round. This
performance replaces inspire greatness.

## Slip through the Crowd (Su) {#slip-through-the-crowd}

At 15th level, a street performer's disappearing act enables affected creatures to move through
crowd squares and enemy-occupied squares without impediment. Affected creatures are treated as if
having _[greater invisibility](ref/spell/invisibility-greater)_, but enemies gain a new saving throw
to notice them each time they are attacked. This performance replaces inspire heroics.

## Gladhanding {#gladhanding}

A street performer earns double the normal amount of money from [Perform](ref/skill/perform-any)
checks. As a standard action, he may use a Bluff check in place of a Diplomacy check to improve a
creature's attitude for 1 minute, after which its attitude becomes one step worse than originally.
This ability replaces countersong.

## Streetwise {#streetwise}

A street performer gains a bonus equal to half his level on Bluff, Disguise, Knowledge (local), and
Sleight of Hand checks, Diplomacy or Intimidate checks made to influence crowds, and Diplomacy
checks to gather information (minimum +1). This replaces bardic knowledge.

## Quick Change (Ex) {#quick-change}

At 5th level, a street performer can don a disguise as a standard action by taking a -5 penalty on
his check. He can take 10 on Bluff and Disguise checks and use Bluff to create a diversion to hide
as a swift action. He can take 20 on a Bluff or Disguise check once per day, plus one time per six
levels beyond 5th. This ability replaces lore master.
