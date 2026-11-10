+++
id = "ref/arc-druid/mountain-druid"
kind = "archetype"
title = "Mountain Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Mountain%20Druid"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mountain_druid", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "100"

[fields]
kind = "archetype"
replaces = ["Woodland stride", "Trackless step", "Resist nature's lure", "Venom immunity", "A thousand faces"]
alters = ["Wild shape"]
replaces_features = ["woodland-stride", "trackless-step", "resist-nature-s-lure", "venom-immunity", "a-thousand-faces"]
alters_features = ["wild-shape"]
+++

As more and more of the soft, easy lands become cultivated and civilized, many druids look for
refuge and solitude among the eternal peaks of the highest mountains.

**Mountaineer (Ex)**

**Gained:** At 2nd Level

**Passive:** A mountain druid gains a bonus on Initiative checks and Climb, Knowledge (geography),
Perception, Stealth, and Survival checks equal to [half](ref/misc/fractions-and-rounding) her druid
level in mountainous terrain, and she cannot be tracked in such an environment.

**Replaces:** Woodland stride

**Sure-Footed (Ex)**

**Gained:** At 3rd Level

**Passive:** A mountain druid suffers no penalty to speed or on Acrobatics or Stealth checks when
walking across steep slopes, rubble, or scree.

**Replaces:** Trackless step

**Spire Walker (Ex)**

**Gained:** At 4th Level

**Passive:** A mountain druid does not lose her Dexterity bonus when climbing. A mountain druid is
immune to [altitude sickness](ref/rule/mountain-travel) and ignores the effects of a cold climate as
if under the effects of [endure elements](ref/spell/endure-elements).

**Replaces:** Resist nature's lure

**Wild Shape (Su)**

**Ability:** A mountain druid gains _wild shape,_ except that her effective druid level for this
ability is equal to her druid level - 2. A mountain druid cannot use _wild shape_ to adopt a plant
form.

**Alters:** Wild shape

**At 12th Level:** She can assume the form of a Large giant as if using
[giant form I](ref/spell/giant-form-1).

**At 16th Level:** She may assume the form of a Huge giant as if using
[giant form II](ref/spell/giant-form-2).

**Gained:** At 6th Level

**Mountain Stance (Ex)**

**Gained:** At 9th Level

**Passive:** A mountain druid gains immunity to petrification and receives a +4 bonus on saving
throws or to CMD to resist any attempt to push, pull, bull rush, or drag her, or to resist any other
effect that would physically move her from her position (e.g., [repel wood](ref/spell/repel-wood),
[reverse gravity](ref/spell/reverse-gravity), or being blown away by high winds). This does not
protect her against being tripped, grappled, or overrun.

**Replaces:** Venom immunity

**Mountain Stone (Ex)**

**Ability:** A mountain druid can transform her body into a weathered stone outcrop and back at
will. This effect functions as [statue](ref/spell/statue).

**Gained:** At 13th Level

**Replaces:** A thousand faces
