+++
id = "ref/arc-spiritualist/fractured-mind"
kind = "archetype"
title = "Fractured Mind"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Fractured%20Mind"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fractured_mind", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "occult-adventures"
page = "109"
[[expanded_in]]
publication = "heroes-from-the-fringe"
page = "19"
via = "ref/emotionalfocus/whimsey"
[[expanded_in]]
publication = "occult-origins"
page = "19"
via = "ref/emotionalfocus/remorse"
[[expanded_in]]
publication = "psychic-anthology"
page = "5"
via = "ref/emotionalfocus/kindness"

[fields]
kind = "archetype"
features = [
  { anchor = "emotional-spellcasting" },
  { anchor = "emotional-power" },
]
trades = [
  { replaces = "Detect undead", feature = "detect-undead", by = ["emotional-power"] },
  { replaces = "calm spirit", feature = "calm-spirit", by = ["emotional-power"] },
  { replaces = "see invisibility", feature = "see-invisibility", by = ["emotional-power"] },
  { replaces = "call spirit", feature = "call-spirit", by = ["emotional-power"] },
  { alters = "Spellcasting", feature = "spells", by = ["emotional-spellcasting"] },
]
+++

Most spiritualists harbor the spirits of the deceased in their psyches, but a small number of
them—known as fractured minds—draw their powers instead from a fraction of their own souls that
resonates with extremely powerful emotions. These spiritualists' phantoms are not spiritual allies,
but rather extensions of the fractured minds' own inner thoughts and emotions.

## Emotional Spellcasting {#emotional-spellcasting}

A fractured mind's ability to cast spells is tied to the force of her own spirit rather than her
connection to the spirit world. As a result, she uses her Charisma score rather than her Wisdom
score to determine the highest spell level she can cast, the saving throw DCs of spells she casts,
and her bonus spells per day. This ability alters spellcasting.

## Emotional Power (Sp) {#emotional-power}

The fractured mind gains a number of [spell-like abilities](ref/umr/spell-like-abilities), which are
tied to her phantom's emotional focus. She gains one spell-like ability at 5th level, a second at
7th level, a third at 9th level, and a fourth at 16th level. A fractured mind can use each of these
abilities once per day, plus one additional time per day for every 4 spiritualist levels she
possesses beyond the level at which she gained the spell-like ability. The saving throw DCs for
these spell-like abilities are equal to 10 + 1/2 the fractured mind's spiritualist class level + the
fractured mind's Charisma modifier, rather than being based on the spell's level. The spell-like
abilities granted by each emotional focus are listed below.

### Anger {#anger}

_Enlarge person_ (5th), _rage_ (7th), _longstrider_ (9th), _shout_ (16th).

### Dedication {#dedication}

_Command_ (5th), _spiritual weapon_ (7th), _bless_ (9th), _death ward_ (16th).

### Despair {#despair}

_Bungle_ (5th), _stricken heart_ (7th), _doom_ (9th), _crushing despair_ (16th).

### Fear {#fear}

_Bane_ (5th), _mad hallucination_ (7th), _doom_ (9th), _phantasmal killer_ (16th).

### Hatred {#hatred}

_Doom_ (5th), _inflict moderate wounds_ (7th), _bane_ (9th), _bestow curse_ (16th).

### Jealousy {#jealousy}

_Sanctuary_ (5th), _resist energy_ (7th), _entropic shield_ (9th), _spell immunity_ (16th).

### Zeal {#zeal}

_Bless_ (5th), _spiritual weapon_ (7th), _divine favor_ (9th), _freedom of movement_ (16th).

This ability replaces _detect undead_, _calm spirit_, _see invisibility_, and _call spirit_.
