+++
id = "ref/arc-skald/totemic-skald"
kind = "archetype"
title = "Totemic Skald"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Totemic%20Skald"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "totemic_skald", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "advanced-class-guide"
page = "117"

[fields]
kind = "archetype"
features = [
  { anchor = "totem", level = 3 },
  { anchor = "song-of-the-beast", level = 3 },
  { anchor = "totem-empathy", level = 4 },
  { anchor = "wild-shape", level = 5 },
]
trades = [
  { replaces = "Rage power gained at 3rd level", feature = "rage-powers", levels = [3], by = ["song-of-the-beast"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["totem-empathy"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["totem-empathy"] },
  { replaces = "Spell kenning", feature = "spell-kenning", by = ["wild-shape"] },
]
+++

The totemic skald forms a close connection to an animal totem. Through the power of this mystical
ally, the skald can change shapes, assuming its form as his own. Additionally, the totem animal
grants the skald a measure of its spiritual power that he can share with his allies.

## Totem (Su) {#totem}

At 3rd level, the totemic skald chooses one animal from the hunter's
[animal focus](ref/ability/animal-foci) list (see page 27). Once selected, this choice cannot be
changed. This animal becomes the skald's personal totem animal and influences his later abilities.
He gains the following rage power.

## Song of the Beast (Su) {#song-of-the-beast}

The totemic skald grants the animal focus abilities of his totem animal (as the hunter's animal
focus ability) to all allies affected by his raging song. He treats his skald level as his hunter
level for determining the abilities of the animal focus (such as the improvements gained at 8th and
15th level). This ability replaces the rage power gained at 3rd level.

## Totem Empathy (Ex and Sp) {#totem-empathy}

At 4th level, the totemic skald can improve the attitude of animals of the same type as his totem.
This ability functions just like a Diplomacy check to improve the attitude of a person. The skald
rolls 1d20 and adds his skald level and his Charisma modifier to determine the totem empathy check
result. The typical domestic animal has a starting attitude of indifferent, while wild animals are
usually unfriendly.

In addition, at 4th level, the totemic skald can cast _[charm animal](ref/spell/charm-animal)_ once
per day as a [spell-like ability](ref/umr/spell-like-abilities), using his skald level as his caster
level and his Charisma modifier to determine the DC. This only functions against animals that are of
the same type as his totem animal (subject to GM discretion). At 8th level, and every 4 levels
thereafter, he can use this ability one additional time per day.

This ability replaces uncanny dodge and improved uncanny dodge.

## Wild Shape (Su) {#wild-shape}

At 5th level, a totemic skald gains the ability to wild shape into the form of a Small or Medium
version of his totem animal, as the [druid](ref/class/druid) class feature. His effective druid
level for this ability is equal to his skald level - 1. He can use this ability twice per day at
11th level, and three times per day at 17th level. This doesn't allow the skald to assume other
forms, such as elementals, plants, or other kinds of animals.

When in animal form, the skald is treated as able to speak normally for the purpose of using raging
song, but not for using other abilities that require speech (such as spellcasting). The skald uses
his class level as his druid level for the purpose of qualifying for feats that affect wild shape
(such as [Wild Speech](ref/feat/wild-speech)). This ability replaces spell kenning.

## Rage Powers {#rage-powers}

The following rage powers complement the totemic skald archetype: animal fury, beast totem (lesser,
normal, and greater), knockback, knockdown, low-light vision, primal scent, scent, sprint, and swift
foot.
