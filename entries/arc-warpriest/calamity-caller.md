+++
id = "ref/arc-warpriest/calamity-caller"
kind = "archetype"
title = "Calamity Caller"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Calamity%20Caller"
source_ids = ["heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "calamity_caller", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "heroes-from-the-fringe"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "catastrophic-blessing", level = 1 },
  { anchor = "calamity", level = 1 },
  { anchor = "aspect-of-disaster", level = 20 },
]
trades = [
  { replaces = "Focus weapon", feature = "focus-weapon", by = ["calamity"] },
  { replaces = "sacred weapon", feature = "sacred-weapon", by = ["calamity"] },
  { replaces = "bonus feats", feature = "bonus-feats", by = ["calamity"] },
  { replaces = "Aspect of war", feature = "aspect-of-war", by = ["aspect-of-disaster"] },
  { alters = "Blessings", feature = "blessings", by = ["catastrophic-blessing"] },
]
+++

While all elves feel a deep connection to nature, some elven priests take this bond further, using
their link to call down the wrath of nature upon their enemies. Ekujae are most inclined to harness
this connection, but any elf can wield their bond to nature in this way.

Calamity caller is a warpriest archetype that is available only to elves.

## Catastrophic Blessing {#catastrophic-blessing}

A calamity caller must select a disaster blessing (_Pathfinder RPG Ultimate Wilderness_ 97) as one
of his two blessings, even if the calamity caller's deity does not grant the disaster blessing's
associated domain.

This alters blessings.

## Calamity (Su) {#calamity}

As a standard action, a calamity caller can cause a 5-foot square within 30 feet to suffer a
calamity. A calamity deals 1d6 damage plus an additional 1d6 damage for every 2 warpriest levels he
has beyond 1st to creatures within that square. The type of calamity determines what type of damage
the calamity deals (see below). An affected creature can attempt a saving throw to reduce this
damage by [half](ref/misc/fractions-and-rounding) (DC = 10 + half the calamity caller's warpriest
level + the calamity caller's Wisdom modifier); the type of save is determined by the calamity. The
calamity caller can use this ability at will.

At 4th level, a calamity caller can create an enhanced calamity when he uses this ability. An
enhanced calamity deals twice the calamity's normal damage; in addition, a creature that fails its
save suffers an additional effect (see below). At 8th level and again at 12th level and 16th level,
effects created by an enhanced calamity that last for 1 or more rounds persist for 1 additional
round. The calamity caller can create an enhanced calamity once per day for every 2 warpriest levels
he has. A creature must take damage from the calamity to suffer these additional effects.

The calamities available to calamity callers, the type of damage they deal, the saving throw to
resist the damage, and the secondary effect they cause when enhanced, are listed below.

### Acid Rain {#acid-rain}

A brief rain shower deals acid damage to the target square, with a Fortitude save for half damage. A
creature that fails its save against enhanced acid rain continues to dissolve for 1 round,
automatically taking half the original damage.

### Blizzard {#blizzard}

Hail deals cold damage to the target square, with a Fortitude save for half damage. A creature that
fails its save against an enhanced blizzard is [blinded](ref/misc/blinded) for 1 round.

### Deadfall {#deadfall}

A tree branch, stone boulder, or other heavy object falls on the target square. A deadfall deals
bludgeoning damage, with a Reflex save for half damage. A creature that fails its save against an
enhanced deadfall is knocked [prone](ref/rule/prone); at 12th level, the target is also
[confused](ref/misc/confused) for 1 round.

### Flash Flood {#flash-flood}

A brief surge of stormy water deals bludgeoning damage to the target square, with a Reflex save for
half damage. An enhanced flash [flood](ref/blessing/flood) does not cause additional effects;
instead, an enhanced flash flood targets creatures in a 5-foot radius. At 12th level, the area
increases to a 10-foot radius; at 16th level, the area increases to a 15-foot radius.

### Lightning Strike {#lightning-strike}

A bolt of lightning deals electricity damage to the target square, with a Reflex save for half
damage. A creature that fails its save against an enhanced lightning strike is
[staggered](ref/misc/staggered) for 1 round by electrical impulses.

### Thorny Vines {#thorny-vines}

Vines covered with thick thorns wrap around the target square. The thorny vines deal piercing
damage, with a Reflex save for half damage. A creature that fails its save against enhanced thorny
vines is [entangled](ref/rule/entangled) for 1 round.

### Volcanic Rift {#volcanic-rift}

A magmatic rift emits a plume of fire into the air, dealing fire damage to the target square, with a
Fortitude save for half damage. An enhanced volcanic rift also emits poisonous and corrosive gases;
a creature that fails its save against the enhanced volcanic rift is [sickened](ref/misc/sickened)
for 1 round.

This replaces focus weapon, sacred weapon, and bonus feats.

## Aspect of Disaster (Su) {#aspect-of-disaster}

At 20th level, a creature affected by a calamity caller's enhanced calamity does not receive a save
to reduce the damage or avoid the calamity's effects.

This replaces aspect of war.
