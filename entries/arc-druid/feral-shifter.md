+++
id = "ref/arc-druid/feral-shifter"
kind = "archetype"
title = "Feral Shifter"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Feral%20Shifter"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "feral_shifter", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-class-guide"
page = "92"

[fields]
kind = "archetype"
features = [
  { anchor = "animal-focus", level = 1 },
  { anchor = "second-animal-focus", level = 9 },
]
trades = [
  { replaces = "Nature bond", feature = "nature-bond", by = ["animal-focus"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["second-animal-focus"] },
  { replaces = "a thousand faces", feature = "a-thousand-faces", by = ["second-animal-focus"] },
  { replaces = "timeless body", feature = "timeless-body", by = ["second-animal-focus"] },
]
+++

A feral shifter internalizes her communion with and mastery over animals. Instead of forming a bond
with an animal companion or an aspect of nature, she alters her own essence or being as homage to
the noble creatures of the wild. More in tune with transformation and animal bodies than a normal
druid, a feral shifter blurs the line between humanoid and beast.

## Animal Focus (Su) {#animal-focus}

At 1st level, as a swift action, a feral shifter can take on the aspect of an animal, gaining a
bonus or special ability based on the type of animal emulated. This functions as the hunter's
[animal focus](ref/ability/animal-foci) class feature (see page 27). The feral shifter can use this
ability for a number of minutes per day equal to her druid level. This duration does not need to be
consecutive, but it must be spent in 1-minute increments. She can emulate only one animal at a time.
This ability replaces nature bond.

## Second Animal Focus (Su) {#second-animal-focus}

At 9th level, when a feral shifter uses her animal focus ability, she selects two different animal
aspects for herself instead of one. This ability replaces venom immunity, a thousand faces, and
timeless body.
