+++
id = "ref/arc-druid/supernaturalist"
kind = "archetype"
title = "Supernaturalist"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Supernaturalist"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "supernaturalist", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "occult-origins"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "eldritch-botanist", level = 1 },
  { anchor = "paranormal-scholar", level = 1 },
  { anchor = "animal-spirit", level = 4 },
]
trades = [
  { replaces = "Nature sense", feature = "nature-sense", by = ["paranormal-scholar"] },
  { replaces = "trackless step", feature = "trackless-step", by = ["paranormal-scholar"] },
  { replaces = "resist nature's lure", feature = "resist-nature-s-lure", by = ["paranormal-scholar"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["animal-spirit"] },
  { replaces = "Nature bond", feature = "nature-bond", by = ["eldritch-botanist"] },
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["eldritch-botanist"] },
  { alters = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
]
+++

Supernaturalists wholly embrace paranormal phenomena as extensions of nature.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A supernaturalist is not proficient with any type of armor. This alters the druid's weapon and armor
proficiencies.

## Eldritch Botanist (Ex) {#eldritch-botanist}

A supernaturalist can affect plants with mind-affecting effects she creates and with spells that
normally affect animals. Any such spell that allows a Will save can instead be negated by the target
plant with a successful Fortitude save at the same DC. She also can choose plant bond and green
empathy, as a treesinger druid (_Advanced Race Guide_ 25), in place of nature bond and wild empathy.

### Plant Bond (Advanced Race Guide page 25) {#plant-bond-arg}

At 1st level, a treesinger forms a mystic bond with plant life. This bond can take one of two forms.
The first grants the treesinger one of the following domains: [Plant](ref/domain/plant) (Core
Rulebook); [Growth](ref/domain/plant) (Advanced Player's Guide); [Jungle](ref/druiddomain/jungle),
[Swamp](ref/druiddomain/swamp) (Ultimate Magic). When determining the powers and bonus spells
granted by this domain, the treesinger's effective cleric level is equal to her druid level. A
treesinger who selects this option also receives additional domain spell slots, just like a cleric.
She must prepare the spell from her domain in this slot, and this spell cannot be used to cast a
spell spontaneously.

The second option is to form a close bond with a plant companion. A treesinger may begin play with
any of the plants listed in Plant Companions (see page 26). This plant is a loyal companion that
accompanies the treesinger on her adventures. Except for the companion being a creature of the plant
type, drawn from the list of plant companions, this ability otherwise works like the standard
druid's animal companion ability.

Plant bond replaces the druid's nature bond ability.

### Green Empathy (Advanced Race Guide page 25) {#plant-bond-arg-green-empathy}

At 1st level, a treesinger can improve the attitude of a plant creature. This ability functions just
like a Diplomacy check made to improve the attitude of a person. The treesinger rolls 1d20 and adds
her druid level and her Charisma modifier to determine the wild empathy check result. The typical
wild plant creature has a starting attitude of indifferent.

To use green empathy, the treesinger and the plant creature must be within 30 feet of one another
under normal conditions. Generally, influencing a plant creature in this way takes 1 minute but, as
with influencing people, it might take more or less time.

A treesinger can also use this ability to influence an animal, but she takes a –4 penalty on the
check. This ability replaces the wild empathy class feature.

## Paranormal Scholar (Ex) {#paranormal-scholar}

A supernaturalist gains [Psychic Sensitivity](ref/feat/psychic-sensitivity) as a bonus feat and adds
[Diplomacy](ref/skill/diplomacy), [Knowledge (arcana)](ref/skill/knowledge-arcana), and
[Sense Motive](ref/skill/sense-motive) as class skills. At 3rd level and every 3 levels thereafter,
she can select a spell from the psychic class's spell list (_Occult Adventures_ 69) and add it to
her druid spell list, and is able to prepare and cast it as a druid spell. This replaces nature
sense, trackless step, and resist nature's lure.

## Animal Spirit (Su) {#animal-spirit}

At 4th level, a supernaturalist can perform a seance to call an animal spirit of any animal with
which she is familiar to serve as her companion and guide. The supernaturalist gains spirit, spirit
bonus, spirit surge, and taboo abilities as a [medium](ref/class/medium) 3 levels lower than her
druid level. The supernaturalist's allies cannot participate in this seance. This ability replaces
wild shape. The spirit abilities of the animal spirit are as follows.

### Spirit Bonus {#spirit-bonus}

Your spirit bonus applies on attack and damage rolls with natural weapons and on skill checks
relating to animals and plants.

### Seance Boon {#seance-boon}

Your natural armor bonus to AC increases by 1.

### Favored Location {#favored-location}

Native terrain of the animal type being invoked.

### Influence Penalty {#influence-penalty}

You become wild and savage, taking a penalty equal to your spirit bonus on caster level checks,
Charisma- and Intelligence-based ability checks, and skill checks.

### Taboos {#taboos}

Choose one: you must not speak (except with animals and plants); you must not wield manufactured
weapons; you must not eat anything you did not kill or harvest yourself.

### Totem Transformation (Lesser, Su) {#totem-transformation-lesser-su}

You gain any of the following abilities possessed by the animal you select as your animal spirit:
[bite](ref/umr/natural-attacks) (1d6 for a Medium druid), 2 claws (1d4 for a Medium druid),
[darkvision](ref/rule/darkvision), improved land movement speed (up to a +20-foot enhancement bonus
to the druid's base land movement speed), [low-light vision](ref/rule/low-light-vision),
[scent](ref/umr/scent), and swim (up to 30 feet).

### Pack Leader (Intermediate, Su) {#pack-leader-intermediate-su}

When you summon animals that match your animal spirit, they gain a +2 bonus on attack rolls, damage
rolls, and saving throws.

### Wildstrike (Greater, Su) {#wildstrike-greater-su}

You can allow your animal spirit to gain 1 point of influence over you as a swift action to allow an
animal or plant (including your companion) within 30 feet that can see or hear you to immediately
take an additional standard action.

### Wild Heart (Supreme, Ex) {#wild-heart-supreme-ex}

You gain a +4 bonus on saves against enchantment and mind-affecting effects, and immunity to effects
that affect only humanoids. Once per day, you can cast any
_[summon nature's ally](ref/spell/summon-natures-ally)_ spell you can cast spontaneously as a
standard action without expending a spell slot.
