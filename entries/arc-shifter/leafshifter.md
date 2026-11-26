+++
id = "ref/arc-shifter/leafshifter"
kind = "archetype"
title = "Leafshifter"
aon = "ArchetypeDisplay.aspx?FixedName=Shifter%20Leafshifter"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "leafshifter", path = "json/archetypes_shifter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shifter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "shifter-s-slam", level = 1 },
  { anchor = "leafshifter-s-aspect", level = 1 },
]
trades = [
  { alters = "Shifter claws", feature = "shifter-claws", by = ["shifter-s-slam"] },
  { alters = "Shifter aspect", feature = "shifter-aspect", by = ["leafshifter-s-aspect"] },
]
+++

Rather than assume aspects taken from the traits of natural animals, a leafshifter transforms into
plant-animal hybrids that resemble [living topiaries](ref/monster/living-topiary). This affords the
leafshifter the savage power of the animal kingdom while also granting her the strength and
timelessness of plant life. (The shifter class can be found on page 26.)

## Shifter's Slam (Ex) {#shifter-s-slam}

This ability functions as the shifter claws class feature, except the leafshifter gains two slam
attacks instead of two claw attacks. These slam attacks are made with her arms, which are covered in
jagged bark and thorns, so these attacks deal bludgeoning and piercing damage.

This alters shifter claws.

## Leafshifter's Aspect (Su) {#leafshifter-s-aspect}

This ability functions as the shifter aspect ability of the standard shifter, except a leafshifter
doesn't gain the minor forms of her aspects. Instead, whenever she gains a new aspect, she chooses
one of the plant focus abilities from the [plant master](ref/arc-hunter/plant-master) hunter
archetype (see page 53) to associate with her new aspect. This choice cannot be changed once made.

This alters shifter aspect.
