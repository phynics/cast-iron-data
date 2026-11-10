+++
id = "ref/arc-druid/desert-druid"
kind = "archetype"
title = "Desert Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Desert%20Druid"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "desert_druid", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "99"

[fields]
kind = "archetype"
replaces = ["Woodland stride", "Trackless step", "Resist nature's lure", "Venom immunity", "A thousand faces"]
alters = ["Wild shape"]
replaces_features = ["woodland-stride", "trackless-step", "resist-nature-s-lure", "venom-immunity", "a-thousand-faces"]
alters_features = ["wild-shape"]
+++

Not all climates are verdant paradises, but even in the sere deserts there is life - though often
hidden from the sun and rarely friendly - and raw, desolate beauty. Here desert druids come to pay
homage, protect and maintain the few habitable locales, and witness nature's majesty in all its
burning, merciless glory.

**Desert Native (Ex)**

**Gained:** At 2nd Level

**Passive:** A desert druid gains a bonus on Initiative checks and Knowledge (geography),
Perception, Stealth, and Survival checks equal to [half](ref/misc/fractions-and-rounding) her druid
level in desert terrain, and she cannot be tracked in such environments.

**Replaces:** Woodland stride

**Sandwalker (Ex)**

**Gained:** At 3rd Level

**Passive:** A desert druid suffers no penalty to speed or on Acrobatics or Stealth checks when
moving through sandy or desert terrain.

**Replaces:** Trackless step

**Desert Endurance (Ex)**

**Gained:** At 4th Level

**Passive:** A desert druid ignores the effects of a hot climate as if using
[endure elements](ref/spell/endure-elements). She also has a reduced need to eat and drink, as if
wearing a [ring of sustenance](ref/magic-ring/ring-of-sustenance) (though normal sleep is still
required).

**Replaces:** Resist nature's lure

**Wild Shape (Su)**

**Ability:** A desert druid gains _wild shape,_ except that her effective druid level for this
ability is equal to her druid level - 2. A desert druid cannot use _wild shape_ to adopt a plant
form.

**Alters:** Wild shape

**At 10th Level:** She can assume the form of a Small or Medium vermin.

**At 12th Level:** She can take the form of a Tiny or Large vermin.

**At 14th Level:** She can assume the form of a Diminutive or Huge vermin.

**Gained:** At 6th Level

**Special:** Starting at 10th level, this effect functions as
[beast shape IV](ref/spell/beast-shape-4) (treating the vermin as an animal to determine its ability
and natural armor modifiers).

**Shaded Vision (Ex)**

**Gained:** At 9th Level

**Passive:** A desert druid becomes immune to blinding and dazzling effects and gains a +2 bonus on
saving throws against [gaze](ref/umr/gaze) attacks and illusions of the figment and pattern
subschools.

**Replaces:** Venom immunity

**Dunemeld (Ex)**

**Ability:** A desert druid can assume the form of a swirling mass of sand at will. This is
equivalent to [gaseous form](ref/spell/gaseous-form), but the druid gains a land and burrow speed of
10 feet rather than a fly speed. While in this form, the druid gains a circumstance bonus on Stealth
checks made in desert terrain equal to her druid level.

**Gained:** At 13th Level

**Replaces:** A thousand faces
