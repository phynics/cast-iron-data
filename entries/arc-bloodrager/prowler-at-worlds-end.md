+++
id = "ref/arc-bloodrager/prowler-at-worlds-end"
kind = "archetype"
title = "Prowler at World's End"
aon = "ArchetypeDisplay.aspx?FixedName=Bloodrager%20Prowler%20at%20World%27s%20End"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "prowler_at_worlds_end", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "4"

[fields]
kind = "archetype"
features = [
  { anchor = "spirit", level = 1 },
  { anchor = "bloodline-powers", level = 4 },
  { anchor = "chosen-of-the-spirits", level = 11 },
  { anchor = "shapeshifted-spellcasting", level = 12 },
]
trades = [
  { replaces = "The 1st-, 8th-, and 16th-level bloodline powers", feature = "bloodline", levels = [1, 8, 16], power = "bloodline power", by = ["spirit"] },
  { replaces = "9th-level and 15th-level bloodline feats", feature = "bloodline", levels = [9, 15], power = "bloodline feat", by = ["bloodline-powers"] },
  { replaces = "The 12th-level bloodline feat", feature = "bloodline", levels = [12], power = "bloodline feat", by = ["shapeshifted-spellcasting"] },
  { alters = "The 4th-, 16th-, and 20th-level bloodline powers", feature = "bloodline", levels = [4, 16, 20], power = "bloodline power", by = ["bloodline-powers"] },
  { alters = "Greater bloodrage", feature = "greater-bloodrage", by = ["chosen-of-the-spirits"] },
  { alters = "mighty bloodrage", feature = "mighty-bloodrage", by = ["chosen-of-the-spirits"] },
]
+++

Ancient [catfolk](ref/race/catfolk) legends claim their kind was created to protect the world from
the sinister forces that exist at the world's fringes. Many catfolk bloodragers capable of communing
with the ancient spirits of creation take on the burden of this ancient tradition.

## Bloodline {#bloodline}

A prowler at world's end must choose the destined bloodline as his bloodline.

## Spirit {#spirit}

At 1st level, a prowler at world's end gains the ability to channel the spirits of creation,
granting him the [medium's](ref/class/medium) [spirit](ref/ability/spirits) and spirit surge
abilities (_Pathfinder RPG Occult Adventures_ 30–31). A prowler channels the cheetah (which acts as
the [trickster](ref/spirit/trickster)), the leopard (which acts as the
[guardian](ref/spirit/guardian)), the lion (which acts as the [marshal](ref/spirit/marshal)), and
the tiger (which acts as the [champion](ref/spirit/champion)). The prowler does not have access to
the archmage or hierophant legends. The favored locations for these spirits are altars, churches,
sacred groves, and shrines, and their taboo requires the prowler to strongly revere nature and
attempt to either destroy or incapacitate evil wherever he encounters it.

A prowler at world's end gains his spirit's lesser power at 1st level, its intermediate power at 8th
level, and its greater power at 16th level. A prowler's spirit surge bonus never advances beyond
1d6.

This ability replaces the 1st-, 8th-, and 16th-level bloodline powers.

## Bloodline Powers {#bloodline-powers}

At 4th level, a prowler at world's end gains the bloodline power normally granted by his bloodline
at 1st level. At 9th level, he gains the bloodline power normally granted by his bloodline at 4th
level. At 12th level, he gains the bloodline power normally granted by his bloodline at 8th level.
At 15th level, he gains the bloodline power normally granted by his bloodline at 12th level. At 20th
level, he gains the bloodline power normally granted by his bloodline at 16th level.

This ability alters the 4th-, 16th-, and 20th-level bloodline powers and replaces the 9th-level and
15th-level bloodline feats.

## Chosen of the Spirits (Su) {#chosen-of-the-spirits}

At 11th level, whenever a prowler at world's end enters a bloodrage, he can apply the effects of
_[beast shape IV](ref/spell/beast-shape-4)_ to himself instead of using greater bloodrage or mighty
bloodrage to apply the effects of a bloodrager spell to himself. He must assume the form of a great
cat of the same kind as a channeled spirit (cheetah, leopard, lion, or tiger). This effect lasts for
as long as the prowler continues bloodraging, regardless of its normal duration, and using it does
not consume a spell slot.

This ability alters the bloodrager's greater bloodrage and mighty bloodrage.

## Shapeshifted Spellcasting (Su) {#shapeshifted-spellcasting}

At 12th level, the prowler at world's end can cast spells while under the effects of chosen of the
spirits. This ability functions as [Natural Spell](ref/feat/natural-spell), except the prowler uses
the ability to cast while under the effects of chosen of the spirits instead of wild shape.

This ability replaces the 12th-level bloodline feat.
