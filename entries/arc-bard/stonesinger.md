+++
id = "ref/arc-bard/stonesinger"
kind = "archetype"
title = "Stonesinger"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stonesinger", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "11"

[fields]
kind = "archetype"
replaces = ["Countersong", "Dirge of doom"]
alters = ["Spellcasting", "Bardic performance"]
+++

Once practiced by the dwarves in their Quest for Sky, the traditions of the stonesinger bards
changed when the dwarves arrived on the surface. The tradition still hearkens back to its
subterranean origins, however, and is practiced as a form of meditation or worship by many dwarves.
Stonesingers are rare bards capable of vocalizing their bardic performances through subsonic
harmonies, allowing their performances to carry as subtle vibrations through stone, rather than
through the air. They command considerable power underground.

**Earth Magic**

**Alters:** Spellcasting

**Passive:** A stonesinger is treated as having the [Eschew Materials](ref/feat/eschew-materials)
feat so long as he is touching natural or manufactured stone. Additionally, a stonesinger adds the
following spells to the bard spell list at the listed spell level.

**Spells:** Magic stone

**Spells:** Stone shield

**Spells:** Stone shape

**Spells:** Earth glide

**Spells:** Stoneskin

**Spells:** Stone tell

**Stone Song (Su)**

**Ability:** A stonesinger's bardic performance is a subsonic vibration that resonates from his body
and travels through solid rock. This vibration is subtle enough to not be heard, though creatures
with the [tremorsense](ref/umr/tremorsense) universal monster ability can distinctly hear the stone
song out to a range of 100 feet per bard level. All allies within 30 feet of the stonesinger benefit
from stone song, perceiving the effect due to proximity. An allied creature with tremorsense
benefits from stone song as long as it's within the extended range, provided that there is an
unobstructed path of solid earth between the creature and stonesinger. Natural and manufactured
stone does not inhibit stone song's range.

**Alters:** Bardic performance

**Special:** A stonesinger must use Perform (sing) or Perform (oratory) for this bardic performance.

**Tremor (Su)**

**Ability:** As part of another bardic performance, a stonesinger can cause the ground within 30
feet to tremble, throwing enemies off balance and causing them to take a -1 circumstance penalty to
AC as long as the stonesinger continues performing.

**At 11th Level:** The penalty becomes -3.

**At 17th Level:** The penalty becomes -4.

**At 5th Level:** The penalty becomes -2.

**Replaces:** Countersong

**Special:** Creatures levitating or flying above the ground are unaffected by this ability.

**Quake (Su)**

**At 8th Level:** A stonesinger causes the ground to shudder and buckle with his song. All enemies
within 30 feet of the stonesinger must succeed at a Reflex save (DC = 10 +
[half](ref/misc/fractions-and-rounding) the stonesinger's level + his Charisma bonus) when he begins
a bardic performance or be knocked [prone](ref/rule/prone).

**Replaces:** Dirge of doom

**Special:** Prone and flying creatures, as well as creatures with the
[earth glide](ref/umr/earth-glide) universal monster ability, are unaffected by this performance.
