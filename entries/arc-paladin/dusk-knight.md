+++
id = "ref/arc-paladin/dusk-knight"
kind = "archetype"
title = "Dusk Knight"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Dusk%20Knight"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dusk_knight", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "blood-of-shadows"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "shadow-smite", level = 1 },
  { anchor = "illuminating-zeal", level = 4 },
  { anchor = "shadow-s-embrace", level = 5 },
  { anchor = "cloak-of-shadow", level = 8 },
  { anchor = "clouding-smite", level = 11 },
]
trades = [
  { replaces = "Channel positive energy", feature = "channel-positive-energy", by = ["illuminating-zeal"] },
  { replaces = "Divine bond", feature = "divine-bond", by = ["shadow-s-embrace"] },
  { replaces = "Aura of resolve", feature = "aura-of-resolve", by = ["cloak-of-shadow"] },
  { replaces = "Aura of justice", feature = "aura-of-justice", by = ["clouding-smite"] },
  { alters = "Smite evil", feature = "smite-evil", by = ["shadow-smite"] },
  { alters = "Class skills" },
]
+++

Some paladins focus their training to combat the shadows and use darkness to their advantage. Known
as dusk knights, these paladins are primarily worshipers of [Abadar](ref/faith/abadar), but dusk
knights who serve [Iomedae](ref/faith/iomedae) and [Irori](ref/faith/irori), though rare, do exist.

## Skills {#skills}

A dusk knight adds Stealth to her list of class skills, instead of Sense Motive.

This alters the paladin's class skills.

## Shadow Smite (Su) {#shadow-smite}

A dusk knight gains [concealment](ref/rule/concealment) for 1 round per paladin level against the
target of her smite evil ability in addition to its other effects. The dusk knight doesn't deal
additional damage with her smite evil ability.

This ability alters smite evil.

## Illuminating Zeal (Su) {#illuminating-zeal}

At 4th level, a dusk knight gains the ability to grant [darkvision](ref/rule/darkvision) to her
allies. As a standard action, the dusk knight grants one target touched
[darkvision](ref/rule/darkvision) with a range of 60 feet for 1 hour. If the target already has
darkvision, the range increases by 60 feet instead. If the dusk knight targets herself, using this
ability is a swift action. Using this ability consumes two uses of her lay on hands ability.

This ability replaces channel positive energy.

## Shadow's Embrace (Su) {#shadow-s-embrace}

At 5th level, a dusk knight learns to fight effectively in areas of darkness. She gains
[Blind-Fight](ref/feat/blind-fight) as a bonus feat and [darkvision](ref/rule/darkvision) with a
range of 60 feet. If she already has darkvision, the range increases by 30 feet instead. At 10th
level, a dusk knight gains [Improved Blind-Fight](ref/feat/improved-blind-fight) as a bonus feat. At
15th level, a dusk knight gains the [see in darkness](ref/umr/see-in-darkness) ability.

This ability replaces divine bond.

## Cloak of Shadow (Su) {#cloak-of-shadow}

At 8th level, a dusk knight becomes adept at moving through darkness. She ignores her armor penalty
when attempting Stealth checks and gains a bonus on Stealth checks equal to half her paladin level
while in areas of [dim light](ref/rule/vision-and-light) or darkness.

This ability replaces aura of resolve.

## Clouding Smite (Su) {#clouding-smite}

At 11th level, a dusk knight's smite impairs her foe's abilities in the dark. When a dusk knight
successfully smites a foe, she reduces the target's [darkvision](ref/rule/darkvision) by 60 feet for
the duration of the smite. If the target has the
[see in darkness](ref/carried/bestiary/rules/universal-monster-rules/see-in-darkness) ability, it
must succeed at a Fortitude save or lose this ability for the duration of the smite. The save DC is
equal to 10 + 1/2 the dusk knight's paladin level + her Charisma modifier.

This ability replaces aura of justice.
