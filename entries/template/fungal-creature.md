+++
id = "ref/template/fungal-creature"
kind = "rule"
title = "Fungal Creature"
source_ids = ["bestiary-4"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fungal_creature", path = "json/monster_template2.json" },
]

[fields]
kind = "none"
+++

**Fungal Creature**

**Challenge rating:** +1

**Inherited:** present

**Source:** Bestiary 4/116

A fungal creature is an animate plant with the appearance of a living creature. It grows from spores
implanted in the dead body of a host creature, and takes on the host creature's basic form and many
of that creature's abilities. It retains none of the memories of the creature it grew from, yet it
instinctively knows how to use the abilities it inherited from its host. How exactly this is
possible is a question that continues to befuddle scholars. The leading theory is that the spores'
precise modeling of their host succeeds in capturing some of the creature's physiology - essentially
copying its mind - but that for some reason the departure of the creature's spirit or soul upon
death prevents the spores from copying the memories as well.

Fungal creatures are often content to sit in quiet contemplation, absorbing the nutrients they
require from the life-giving earth. But when faced with living creatures, the overwhelming
biological need to reproduce takes over, and the fungal creatures try to seed their spores into new
hosts to spawn the next generation of fungal creatures.

Fungal creatures have the general appearance of the base creatures from which they spawned, but
their skin is pale fungus rather than flesh and blood. Mushroom caps and shelf fungi sprout from a
fungal creature's body, along with fungal gills to deliver the fungal creature's spores. As with
many types of fungi, a fungal creature's flesh is poisonous, and any creature that ingests any part
of a fungal creature's body risks infection by its spores (as described in the _create spawn_
ability and _fungal spores poison_ below).

"Fungal creature" is an inherited template that can be added to any corporeal, living creature
susceptible to Constitution damage (referred to hereafter as the base creature). A fungal creature
uses all the base creature's statistics and special abilities except as noted here.

**CR:** Same as the base creature +1.

**Type:** The creature's type changes to [plant](ref/type/plant)
([augmented](ref/subtype/augmented)). Do not recalculate base class Hit Dice, BAB, saves, or skill
points.

**Senses:** A fungal creature gains [darkvision](ref/rule/darkvision) 60 feet.

**AC:** The fungal growths that appear on a fungal creature's body increase the base creature's
natural armor bonus by 2.

**Hit Dice:** Change all racial Hit Dice to d8s. Class Hit Dice are unaffected.

**Defensive Abilities:** A fungal creature gains [immunity](ref/umr/immunity) to disease in addition
to all of the standard plant traits.

**Speed:** Each of a fungal creature's speeds decreases by 10 feet from those of the base creature
(minimum 5 feet).

**Attacks:** A fungal creature retains all the natural weapons, manufactured weapon attacks, and
weapon proficiencies of the base creature. If the base creature has no other natural attacks, the
fungal creature gains a [slam attack](ref/umr/natural-attacks) that deals damage based on the fungal
creature's size.

**Special Attacks:** A fungal creature gains the following.

> **Create Spawn (Ex):** A creature killed by Constitution damage from a fungal creature's poison
> spore cloud transforms into a fungal spawn over a period of 24 hours. A
> [plant growth](ref/spell/plant-growth) spell halves the transformation time, and a
> [diminish plants](ref/spell/diminish-plants) spell doubles it. A [blight](ref/spell/blight) spell
> destroys the fungal spores and prevents the corpse's transformation, but spells that remove
> disease are ineffective against the growing spores. Once a creature fully transforms into a fungal
> spawn, the corpse from which it grew is destroyed.
>
> A fungal spawn gains the fungal creature template, but it loses all class levels and memories of
> the base creature from which it was spawned. If the base creature has 1 or fewer racial Hit Dice
> and normally has class levels, use a 1st-level [warrior](ref/npcclass/warrior) version of it as
> the base creature. The fungal spawn awakens as a free-willed being that knows all it needs to know
> (including language) in order to use its abilities and survive. Although it bears no allegiance to
> the fungal creature that created it, the new fungal creature immediately recognizes other fungal
> creatures as its own kind.
>
> **Poison Spore Cloud (Ex):** Once per day, a fungal creature can release a choking cloud of spores
> in a 15-foot-radius [spread](ref/misc/spread) that lingers in the air for 10 rounds. This cloud
> functions as an inhaled poison. Any breathing creature in the cloud must succeed at a Fortitude
> save or inhale the spores. A creature that remains in the area of the spore cloud must continue to
> attempt Fortitude saves against its effects. Multiple spore clouds from multiple fungal creatures
> require multiple saves from any creature in an area where the clouds overlap.
>
> - [Affliction: Fungal Spores](ref/affliction/fungal-creature/fungal-spores)
>
> **Poisonous Blood (Ex):** A fungal creature's blood and flesh are ingested poisons. Any creature
> that makes a bite attack against a fungal creature, [swallows one whole](ref/umr/swallow-whole),
> or otherwise ingests part of one must succeed at a Fortitude save or be afflicted by the poison.
>
> A fungal creature can drain its own blood to procure an ingested poison that functions as
> described above. However, its blood has a distinctive and largely unwelcome smell and taste, so
> most intelligent creatures would refuse to eat food tainted with it unless the taste was
> thoroughly disguised (which requires a successful DC 15
> [Profession (cook)](ref/skill/profession-any) check). The fungal creature must deal at least 1
> point of damage to itself to get a full dose of poison, and the drawn blood (or amputated flesh)
> retains its poisonous nature for only 24 hours unless additional living fungal blood is mixed into
> it.
>
> - [Affliction: Fungal Blood or Flesh](ref/affliction/fungal-creature/fungal-blood-or-flesh)

**Special Qualities:** A fungal creature gains the following.

> **Fungal Metabolism (Ex):** Fungal creatures breathe, but they do not eat or sleep in the typical
> manner.
>
> **Rejuvenation (Ex):** A fungal creature gains all the sustenance it requires from contact with
> moist natural earth, but it must rejuvenate itself as often and for as long as humans need sleep.
> As long as it is in contact with moist natural earth, a resting fungal creature regains hit points
> as though it were undergoing complete [bed rest](ref/rule/healing) and long term care (4 hit
> points per Hit Die for each day of rest). The fungal creature can engage in light activity during
> rejuvenation, but any strenuous activity (like fighting, running, or casting a spell) prevents it
> from regaining hit points for that day. Complete bed rest doesn't increase the amount of healing a
> fungal creature gains from rejuvenation.

**Abilities:** Str +4, Dex -2 (minimum 1), Con +4.

**Languages:** If a fungal creature is able to speak, it gains the ability to speak Sylvan in
addition to any other languages the base creature knows.
