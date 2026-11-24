+++
id = "ref/arc-warpriest/divine-commander"
kind = "archetype"
title = "Divine Commander"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Divine%20Commander"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "divine_commander", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "advanced-class-guide"
page = "129"

[fields]
kind = "archetype"
features = [
  { anchor = "mount" },
  { anchor = "battle-tactician", level = 3 },
  { anchor = "blessed-mount", level = 6 },
  { anchor = "greater-battle-tactician", level = 12 },
  { anchor = "bless-army", level = 15 },
]
trades = [
  { replaces = "Blessings", feature = "blessings", by = ["mount"] },
  { replaces = "Bonus feat gained at 3rd level", feature = "bonus-feats", levels = [3], by = ["battle-tactician"] },
  { replaces = "Bonus feat gained at 6th level", feature = "bonus-feats", levels = [6], by = ["blessed-mount"] },
  { replaces = "Bonus feat gained at 12th level", feature = "bonus-feats", levels = [12], by = ["greater-battle-tactician"] },
  { replaces = "Bonus feat gained at 15th level", feature = "bonus-feats", levels = [15], by = ["bless-army"] },
]
+++

Some warpriests are called to lead great armies and face legions of foes. These divine commanders
live for war and fight for glory. Their hearts quicken at battle cries, and they charge forth with
their deity's symbol held high. These leaders of armies do so to promote the agenda of their faith,
and lead armies of devoted followers willing to give their lives for the cause. (Several of the
divine commander's abilities reference and interact with the
[mass combat rules](ref/rule/mass-combat).)

## Mount (Ex) {#mount}

A divine commander gains the service of a loyal and trusty steed to carry her into battle. This
mount functions as a druid's [animal companion](ref/sidekick/animal-companion), using the divine
commander's level as her effective druid level. The creature must be one that she is capable of
riding and must be suitable as a mount. A Medium divine commander can select a
[camel](ref/companion/camel) or a [horse](ref/companion/horse). A Small divine commander can select
a [pony](ref/companion/pony) or [wolf](ref/companion/wolf), but can also select a
[boar](ref/companion/boar) or a [dog](ref/companion/dog) if she is at least 4th level. (The GM might
approve other animals as suitable mounts.)

A divine commander does not take an armor check penalty on Ride checks while riding this mount. The
mount is always considered combat trained, and begins play with
[Light Armor Proficiency](ref/feat/armor-proficiency-light) as a bonus feat. A divine commander's
mount does not gain the share spells special ability. Should a divine commander's mount die, she can
find another mount to serve her after 1 week of mourning. This new mount does not gain the link,
evasion, devotion, or improved evasion special abilities until the next time the divine commander
gains a level. This ability replaces blessings.

## Battle Tactician (Ex) {#battle-tactician}

At 3rd level, a divine commander gains a teamwork feat as a bonus feat. She must meet the
prerequisites for this feat. As a standard action, the divine commander can grant this feat to all
allies within 30 feet who can see and hear her. Allies retain the use of this bonus feat for 4
rounds, plus 1 round for every 2 levels beyond 3rd that the divine commander possesses. Allies do
not need to meet the prerequisites of this bonus feat. The divine commander can use this ability
once per day at 3rd level, plus one additional time per day at 9th and 15th levels. This ability
replaces the bonus feat gained at 3rd level.

## Blessed Mount (Su) {#blessed-mount}

At 6th level, a divine commander's mount becomes a creature blessed by his deity. The divine
commander's mount gains either the [celestial](ref/template/celestial),
[entropic](ref/template/entropic), [fiendish](ref/template/fiendish), or
[resolute](ref/template/resolute) template, matching the alignment of the warpriest's deity
(celestial for good, entropic for chaotic, fiendish for evil, and resolute for lawful). If the deity
matches more than one alignment, the divine commander can select which of the two templates the
mount receives. Once the type of template is selected, it cannot be changed.

If the divine commander's deity is neutral with no other alignment components, the mount receives
[spell resistance](ref/rule/spell-resistance) equal to the divine commander's level + 5, as well as
resistance 10 against two types of energy damage of the divine commander's choice.

If a divine commander's mount dies and the divine commander finds another mount, the new mount
becomes a blessed mount the next time the divine commander gains a level. This ability replaces the
bonus feat gained at 6th level.

## Greater Battle Tactician (Ex) {#greater-battle-tactician}

At 12th level, the divine commander gains an additional teamwork feat as a bonus feat. She must meet
the prerequisites for this feat. The divine commander can grant this feat to her allies using the
battle tactician ability. Additionally, using the battle tactician ability is now a swift action.
This ability replaces the bonus feat gained at 12th level.

## Bless Army (Su) {#bless-army}

At 15th level, a divine commander can raise her holy symbol high and give a blessing to the army she
is leading. The divine commander's army gains a +1 bonus to the army's
[OM and DV](ref/rule/mass-combat-quick-reference-guide) (_Ultimate Campaign_ 235). This is a sacred
bonus if the warpriest is good-aligned or able to spontaneously cast cure spells, and it is a
profane bonus if the warpriest is evil-aligned or able to spontaneously cast inflict spells. Using
this ability requires the divine commander to expend two uses of her fervor ability. This bonus
lasts for 1 battle, and it must be performed during the tactics phase of the battle. If this is
performed when a mass combat is not imminent, the fervor is spent without granting any bonus. This
ability replaces the bonus feat gained at 15th level.
