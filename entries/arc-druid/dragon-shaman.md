+++
id = "ref/arc-druid/dragon-shaman"
kind = "archetype"
title = "Dragon Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Dragon%20Shaman"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dragon_shaman", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-magic"
page = "37"

[fields]
kind = "archetype"
features = [
  { anchor = "nature-bond", level = 1 },
  { anchor = "wild-empathy", level = 1 },
  { anchor = "totem-transformation", level = 2 },
  { anchor = "totemic-summons", level = 5 },
  { anchor = "wild-shape", level = 6 },
  { anchor = "dragon-bite", level = 8 },
  { anchor = "bonus-feat", level = 9 },
]
trades = [
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["totemic-summons"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
  { replaces = "The additional use of wild shape at 8th level", by = ["dragon-bite"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["bonus-feat"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["nature-bond"] },
  { alters = "Wild empathy", feature = "wild-empathy", by = ["wild-empathy"] },
]
+++

Your totem is the legendary dragon, fearsome and deadly yet cunning and wise, a creature born of
pure magic and raw elemental fury, bound within a shell of fangs, claws, and scales that few dare to
challenge. Though your initial focus is on dragons' mundane cousins, as your powers grow you become
attuned to actual dragons.

## Nature Bond {#nature-bond}

A dragon shaman who chooses an animal companion must select a [crocodile](ref/companion/crocodile)
(see page 54 of the _Core Rulebook_) or [monitor lizard](ref/companion/lizard-monitor-lizard) (see
page 194 of the _Bestiary_). If choosing a domain, the dragon shaman must choose from the
[Air](ref/domain/air), [Animal](ref/domain/animal), [Destruction](ref/domain/destruction),
[Earth](ref/domain/earth), [Fire](ref/domain/fire), [War](ref/domain/war), and
[Water](ref/domain/water) domains.

## Wild Empathy (Ex) {#wild-empathy}

A dragon shaman can use her wild empathy ability with lizards as a full-round action with a +4
bonus.

## Totem Transformation (Su) {#totem-transformation}

At 2nd level, a dragon shaman may adopt an aspect of the dragon while retaining her normal form. She
gains one of the following bonuses: movement (fly speed 30 feet \[average\], the druid must be 5th
level to select this bonus), senses ([low-light vision](ref/rule/low-light-vision), +4 racial bonus
to Perception), toughness (+2 natural armor bonus to AC, [Endurance](ref/feat/endurance) feat), or
[natural weapons](ref/umr/natural-attacks) (bite \[1d6\] and 2 claws \[1d4\] for a Medium shaman, +2
bonus on CMB on grapple checks). While using totem transformation, the dragon shaman may speak
normally and can cast _[speak with animals](ref/spell/speak-with-animals)_ (lizards only) at will.
Using this ability is a standard action at 2nd level, a move action at 7th level, and a swift action
at 12th level. The dragon shaman can use this ability for a number of minutes per day equal to her
druid level. These minutes do not need to be consecutive, but they must be used in 1-minute
increments. This is a polymorph effect and cannot be used while the druid is using another polymorph
effect, such as wild shape.

## Totemic Summons (Su) {#totemic-summons}

At 5th level, a dragon shaman may cast _[summon nature's ally](ref/spell/summon-natures-ally)_ as a
standard action when summoning lizards, and summoned lizards gain
[temporary hit points](ref/rule/temporary-hit-points) equal to her druid level. She can apply the
[young](ref/template/young) template to any lizard to reduce the level of the summoning spell
required by one. She can also increase the level of summoning required by one in order to apply
either the [advanced](ref/template/advanced) or the [giant](ref/template/giant) template, or
increase it by two to apply both the advanced and giant templates. This ability replaces a thousand
faces.

## Wild Shape (Su) {#wild-shape}

At 6th level, a dragon shaman's wild shape ability functions at her druid level - 4. If she takes on
the form of a lizard, she instead uses her unmodified druid level.

## Dragon Bite (Su) {#dragon-bite}

At 8th level, a dragon shaman's bite attack (whether using totem transformation or wild shape to
take the form of a lizard) deals +1d6 points of energy damage (acid, cold, electricity, or fire).
She chooses what kind of energy damage that she deals each time she bites. This ability replaces the
additional use of wild shape at 8th level.

## Bonus Feat {#bonus-feat}

At 9th level and every 4 levels thereafter, a dragon shaman gains one of the following bonus feats:
[Combat Casting](ref/feat/combat-casting), [Dazzling Display](ref/feat/dazzling-display),
[Magical Aptitude](ref/feat/magical-aptitude), [Skill Focus](ref/feat/skill-focus) (Knowledge
\[arcana\]), and [Spell Penetration](ref/feat/spell-penetration). She must meet the prerequisites
for these bonus feats. This ability replaces venom immunity.
