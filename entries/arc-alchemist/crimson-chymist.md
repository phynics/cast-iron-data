+++
id = "ref/arc-alchemist/crimson-chymist"
kind = "archetype"
title = "Crimson Chymist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Crimson%20Chymist"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "crimson_chymist", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "adventurers-guide"
page = "156"

[fields]
kind = "archetype"
features = [
  { anchor = "crimson-discoveries" },
  { anchor = "mantis-mutagen", level = 1 },
]
trades = [
  { alters = "Mutagen", feature = "mutagen", by = ["mantis-mutagen"] },
  { alters = "Discovery", feature = "discovery", by = ["crimson-discoveries"] },
]
+++

[Red Mantis](ref/rule/aff-assassins) agents are easily identifiable by their iconic equipment. Yet
some assassins believe even subtler killing methods can be employed while still honoring
[Achaekek](ref/faith/achaekek). These crimson chymists turn to the alchemical arts, infusing their
bodies with the mutagenic essence of the Mantis God.

## Crimson Discoveries (Su) {#crimson-discoveries}

A crimson chymist gains access to several additional unique discoveries, as detailed below.

This alters discovery.

### Arms of Achaekek {#arms-of-achaekek}

The small barbs that grow on the crimson chymist's arms when she drinks her mantis mutagen grow
significantly in size, granting her two claw attacks as [natural weapons](ref/umr/natural-attacks).
These claws deal damage as appropriate for her size (1d4 for Medium crimson chymists) and function
as secondary attacks. These claws do not replace the chymist's hands, and she can still use her
hands to wield weapons, attack, hold objects, and otherwise use her hands with ease, but she cannot
be wearing any item in the wrists slot or any armor—if she dons magic items that occupy the wrists
slot or any armor, her claws shrink back to cosmetic barbs that can't be used in combat as long as
the armor or wrist items are worn. A crimson chymist must be at least 6th level before selecting
this discovery.

### Blood Sight {#blood-sight}

When the crimson chymist is under the effects of her mantis mutagen, her eyes transform, becoming
red and multifaceted. This change grants her [darkvision](ref/rule/darkvision) to a range of 60 feet
and the effects of _[deathwatch](ref/spell/deathwatch)_ for the duration of her mutagen's effects.
If the crimson chymist already has darkvision as a benefit of her race, the range of her darkvision
increases by 30 feet while using blood sight.

### Improved Arms of Achaekek {#improved-arms-of-achaekek}

The claws granted by the arms of Achaekek discovery now function as primary weapons when the crimson
chymist makes no attacks with manufactured weapons (the claws function as secondary weapons if the
chymist attacks with a manufactured weapon). The damage die of the claws increases by one size
category (to 1d6 for Medium crimson chymists), and attacks deal 1d4 points of
[bleed](ref/rule/bleed) damage on a hit. A crimson chymist must be at least 10th level and have the
arms of Achaekek discovery before selecting this discovery.

### Ingest Venom {#ingest-venom}

Once per day as a standard action, the crimson chymist can ingest one dose of any poison without
harming herself. The next time she imbibes her mutagen and uses her arms of Achaekek discovery, both
claws are envenomed with a dose of the poison she ingested. An ingested venom remains latent in the
alchemist's system until she activates her arms of Achaekek discovery or until 24 hours have passed,
whichever comes first. Additional doses of venom ingested during that time affect the alchemist
normally.

A crimson chymist must have the arms of Achaekek discovery before selecting this discovery.

## Mantis Mutagen (Su) {#mantis-mutagen}

At 1st level, a crimson chymist discovers how to create a specialized mutagen that grants her
aspects of a praying mantis. A mantis mutagen functions as an alchemist mutagen, save that it always
enhances Dexterity and applies a penalty to Charisma. When imbibed, the mutagen causes the crimson
chymist's flesh to grow red chitinous plates on her body as natural armor and a row of small,
cosmetic barbed hooks along her arms.

This alters mutagen.
