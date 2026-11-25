+++
id = "ref/arc-medium/kami-medium"
kind = "archetype"
title = "Kami Medium"
aon = "ArchetypeDisplay.aspx?FixedName=Medium%20Kami%20Medium"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kami_medium", path = "json/archetypes_medium.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/medium" },
]
[[sources]]
publication = "occult-adventures"
page = "92"

[fields]
kind = "archetype"
features = [
  { anchor = "kami-channeler" },
  { anchor = "natural-taboo" },
  { anchor = "ofuda" },
  { anchor = "shikigami", level = 3 },
  { anchor = "ask-the-kami", level = 13 },
  { anchor = "ward", level = 14 },
]
trades = [
  { replaces = "Haunt channeler", feature = "haunt-channeler", by = ["shikigami"] },
  { replaces = "location channel", feature = "location-channel", by = ["shikigami"] },
  { replaces = "connection channel", feature = "connection-channel", by = ["shikigami"] },
  { replaces = "Ask the spirits", feature = "ask-the-spirits", by = ["ask-the-kami"] },
  { replaces = "Astral journey", feature = "astral-journey", by = ["ward"] },
  { alters = "Spirit", feature = "spirit", by = ["kami-channeler"] },
  { alters = "Taboo", feature = "taboo", by = ["natural-taboo"] },
  { alters = "Spellcasting", feature = "spells", by = ["ofuda"] },
]
+++

Some mediums channel the power of nature spirits called [kami](ref/family/kami) rather than the
spirits of legend. See pages 159–165 of _Pathfinder RPG Bestiary 3_ for more information on kami.

## Kami Channeler (Su) {#kami-channeler}

A kami medium channels the kami at locations different from where a normal medium channels his
spirits. The kami medium channels the [dosojin](ref/monster/kami-dosojin) (which acts as the
[trickster](ref/spirit/trickster)) at crossroads and other major roadway milestones;

the [fukujin](ref/monster/kami-fukujin) (which acts as the [marshal](ref/spirit/marshal)) at
ornamental shrubs and bonsai trees; the [kaminari](ref/monster/kami-kaminari) (which acts as the
[champion](ref/spirit/champion)) in the midst of storms; the [suijin](ref/monster/kami-suijin)
(which acts as the [hierophant](ref/spirit/hierophant)) at pure lakes, ponds, springs, and wells;
and the [zuishin](ref/monster/kami-zuishin) (which acts as the [guardian](ref/spirit/guardian)) at
significant gates, doorways, and torii. The kami medium does not have access to the archmage legend.
This ability alters spirit.

## Natural Taboo (Ex) {#natural-taboo}

A kami medium gains the taboo ability at 1st level. Regardless of which kami he channels, each day
he must accept the hierophant taboo to strongly revere nature and avoid metal armor. The kami medium
gains two free uses of spirit surge from accepting this taboo, as normal. This ability alters taboo.

## Ofuda (Su) {#ofuda}

A kami medium uses ofudas—psychically charged prayer scrolls—to focus his spells. Each of his spells
gains an ofuda as an additional inexpensive material component, and the ofuda replaces the divine
focus for spells the kami medium gains via the divine surge spirit power. Unless the spell involves
a touch attack or ranged touch attack, the kami medium doesn't need to attempt an attack roll to
place an ofuda on an unwilling target; the ofuda simply appears on affected targets. For
instantaneous spells, the ofuda is consumed during the casting, but for spells with any other
duration, the ofuda remains on the target or targets throughout the duration and then disintegrates
when the duration expires.

A kami medium's spells can't be dispelled by _[dispel magic](ref/spell/dispel-magic)_ or
_[greater dispel magic](ref/spell/dispel-magic-greater)_, but removing or destroying the ofuda ends
the duration immediately. An ofuda must be displayed prominently and can't be hidden (though a
creature bearing an ofuda can hide normally).

A successful [steal](ref/rule/steal) or [grapple](ref/rule/grapple) combat maneuver check to remove
an item is sufficient to remove an ofuda from an unwilling target, and a standard action
automatically removes it from a willing target. An ofuda counts as an object made of paper with 5
hit points per medium level. The target of the spell can't see, harm, or remove the ofuda attached
to her, though her allies can do so. If the spell is harmless, the target can see her ofuda.

This ability alters the medium's spellcasting.

## Shikigami (Ex) {#shikigami}

At 3rd level, a kami medium learns to fold an origami animal to serve as a temporary ward for a
minor [shikigami](ref/monster/kami-shikigami). Initially, the merged minor shikigami can't leave the
paper body and acts in all ways as an ordinary animal [familiar](ref/sidekick/familiar) of the
origami animal's type, although it still appears to be made of paper. At 5th level, it gains the
abilities of a shikigami [improved familiar](ref/ability/improved-familiars), even if the kami
medium doesn't meet the prerequisites for having a shikigami as a familiar. The shikigami treats the
kami medium as its ward. Additionally, it gains the ability to use
[change shape](ref/carried/bestiary/rules/universal-monster-rules/change-shape) to change between
its full shikigami form and its origami form at will (as
_[beast shape II](ref/spell/beast-shape-2)_).

This ability replaces haunt channeler, location channel, and connection channel.

## Ask the Kami (Su) {#ask-the-kami}

At 13th level, a kami medium can ask the local kami for information, as
_[commune with nature](ref/spell/commune-with-nature)_. While he can do so any number of times per
day, he can ask questions of the kami in any particular area only once per day. Afterward, he must
move to a non-overlapping area to use this ability again. This ability replaces ask the spirits.

## Ward (Su) {#ward}

At 14th level, a [kami](ref/subtype/kami) medium can declare an area or object that's an appropriate
place to contact his channeled kami as his ward. This grants the kami medium the ward and merge with
ward abilities of the kami subtype. For large areas such as lakes or storms, a kami medium's ward
encompasses a radius of up to 5 feet per medium level. This ability replaces astral journey.
