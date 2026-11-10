+++
id = "ref/arc-spiritualist/involutionist"
kind = "archetype"
title = "Involutionist"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Involutionist"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "involutionist", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "adventurers-guide"
page = "167"

[fields]
kind = "archetype"
replaces = ["Phantom's emotional focus", "Detect undead", "Additional uses of calm spirit available at 11th, 15th, and 19th levels"]
alters = ["Spellcasting", "Phantom", "Bonded manifestation"]
replaces_features = ["detect-undead"]
alters_features = ["phantom", "bonded-manifestation"]
+++

The [Rivethun](ref/rule/aff-animists) teach their followers to cultivate a well of inner power and
to open themselves to the spiritual world, but on occasion - especially among neophytes who join the
cult later in life - these processes overlap, and the acolyte invests her spiritual reservoir into
some aspect of the world around her. Rather than bond with an existing spirit as most Rivethun
eventually do, the involutionist creates a spirit from a piece of her own soul. The bond is deep,
and it creates a powerful minion utterly loyal to her creator, but it also cuts off the
involutionist's access to the wider spiritual world.

**Divine Spellcasting**

**Alters:** Spellcasting

**Info:** An involutionist is a divine spellcaster. Her spells use verbal components instead of
thought components and somatic components instead of emotional components. An involutionist's spirit
phantom is her conduit to the divine, and it serves as her divine focus; the involutionist must
either be within 5 feet on her spirit phantom or absorb her phantom into her consciousness to cast
spells that require a divine focus.

**Spirit Phantom**

**Action:** Ability

**Alters:** Phantom

**Flavor:** An involutionist's phantom is manifested from her own psyche and invested into the
spirit-stuff of the world around her.

**Repeat:** The spirit phantom gains one additional hex from their list., 7, 5

**Replaces:** Phantom's emotional focus

Rather than an emotional focus, the involutionist selects a spirit from those available to the
[shaman](ref/class/shaman). A spirit phantom always has good Fortitude and Reflex saves, and it
gains a number of ranks equal to the phantom's Hit Dice in two skills depending on the spirit it
represents, as summarized on the table below.

|Spirit|Associated Skills|
| --- | --- |
|[Battle](ref/shamanspirit/battle)|Intimidate and Sense Motive|
|[Bones](ref/shamanspirit/bones)|Heal and Stealth|
|[Flame](ref/shamanspirit/flame)|Acrobatics and Intimidate|
|[Heavens](ref/shamanspirit/heavens)|Acrobatics and Fly|
|[Life](ref/shamanspirit/life)|Diplomacy and Heal|
|[Lore](ref/shamanspirit/lore)|Knowledge (arcana) and Linguistics|
|[Nature](ref/shamanspirit/nature)|Knowledge (nature) and Survival|
|[Stone](ref/shamanspirit/stone)|Appraise and Knowledge (engineering)|
|[Waves](ref/shamanspirit/waves)|Diplomacy and Swim|
|[Wind](ref/shamanspirit/wind)|Bluff and Sense Motive|

When fully manifested, the involutionist's spirit phantom gains the special ability normally applied
to a shaman's spirit animal. The spirit phantom also gains a single hex from the list of those
provided by that spirit.

**Spirit Manifestation (Su)**

**Ability:** When an involutionist uses her _bonded manifestation_ ability, she can instead manifest
her spirit phantom's spirit animal special ability and use her spirit phantom's hexes as if they
were her own. Hexes used during this manifestation count toward any limited number of uses per day.

**Alters:** Bonded manifestation

**Gained:** At 3rd Level

**Spirit Awareness (Sp)**

**Ability:** She can cast [detect psychic significance](ref/spell/detect-psychic-significance) as a
[spell-like ability](ref/umr/spell-like-abilities) at will and
[analyze aura](ref/spell/analyze-aura) once per day as a spell-like ability (CL = her character
level).

**Flavor:** An involutionist gains great insight into the spiritual influence people invest into the
world around them.

**Gained:** At 5th Level

**Replaces:** Detect undead

**Involuate (Sp)**

**Ability:** She gains the ability to cast [animate objects](ref/spell/animate-objects) as a
[spell-like ability](ref/umr/spell-like-abilities) (CL = her character level).

**Flavor:** An involutionist gains the ability to awaken the latent spiritual energy in inanimate
objects.

**Gained:** At 11th Level

**Replaces:** Additional uses of calm spirit available at 11th, 15th, and 19th levels

**Usage:** 1 time/day + 1 per 4 spiritualist levels beyond 11th
