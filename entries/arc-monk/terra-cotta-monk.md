+++
id = "ref/arc-monk/terra-cotta-monk"
kind = "archetype"
title = "Terra-Cotta Monk"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Terra-Cotta%20Monk"
source_ids = ["dungeoneers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "terra_cotta_monk", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "dungeoneers-handbook"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "trap-intuition", level = 2 },
  { anchor = "stone-grip", level = 5 },
  { anchor = "trap-dodge", level = 10 },
  { anchor = "sudden-adit", level = 12 },
  { anchor = "petrifying-strike", level = 15 },
  { anchor = "rainmaker", level = 19 },
]
trades = [
  { replaces = "Evasion", feature = "evasion", by = ["trap-intuition"] },
  { replaces = "High jump", feature = "high-jump", by = ["stone-grip"] },
  { replaces = "Improved evasion", feature = "improved-evasion", by = ["trap-dodge"] },
  { replaces = "Abundant step", feature = "abundant-step", by = ["sudden-adit"] },
  { replaces = "Quivering palm", feature = "quivering-palm", by = ["petrifying-strike"] },
  { replaces = "Empty body", feature = "empty-body", by = ["rainmaker"] },
]
+++

Possessing a natural affinity for all things earthen, terra-cotta monks are experts at turning the
stone around them against their enemies.

## Class Skills {#class-skills}

A terra-cotta monk adds Knowledge (dungeoneering), Knowledge (engineering), and Disable Device to
his list of class skills and removes Knowledge (history), Perform, and Ride.

## Trap Intuition (Ex) {#trap-intuition}

At 2nd level, whenever a terra-cotta monk comes within 10 feet of a trap, he receives an immediate
Perception check to notice the trap. The GM should make this check in secret. A terra-cotta monk
gains a +2 bonus on Perception checks to notice traps. This bonus increases to +4 if the trap is
located in a stone wall or floor. This ability replaces evasion.

## Stone Grip (Su) {#stone-grip}

At 5th level, a terra-cotta monk adds a bonus equal to his class level on all Climb checks. He can
move at his full movement rate while climbing with no increase to the check's DC. By spending 1
point from his ki pool as a swift action, a monk gains the benefits of
_[spider climb](ref/spell/spider-climb)_ for 1 round. This ability replaces high jump.

## Trap Dodge (Ex) {#trap-dodge}

At 10th level, a terra-cotta monk gains a bonus equal to his Wisdom modifier on all saving throws
made against effects produced by mechanical traps. This ability replaces improved evasion.

## Sudden Adit (Su) {#sudden-adit}

At 12th level, a terra-cotta monk can create passages through stone or dirt as if using the spell
_[passwall](ref/spell/passwall)_ with a caster level equal to his monk level. Using this ability is
a move action that consumes 2 points of the monk's ki pool. This ability replaces abundant step.

## Petrifying Strike (Su) {#petrifying-strike}

At 15th level, a terra-cotta monk can turn an opponent to stone with a single strike. He can use
this ability once per day, and must announce the attempt before making his attack roll. If the
terra-cotta monk's strike is successful, the creature must succeed at a Fortitude save (DC = 10 +
1/2 the monk's level + the monk's Wis modifier) or be [petrified](ref/rule/petrified) for 1 hour per
monk level. Incorporeal creatures and creatures immune to petrification are unaffected by this
ability. This ability replaces quivering palm.

## Rainmaker (Su) {#rainmaker}

At 19th level, anytime a terra-cotta monk is underground, he may cause a section of the roof to come
down on his enemies per the spell _[earthquake](ref/spell/earthquake)_, with a caster level equal to
his monk level. The terra-cotta monk may use this ability only while in a cave, cavern, or tunnel.
Using this ability is a standard action that consumes 3 points from his ki pool. This ability
replaces empty body.
