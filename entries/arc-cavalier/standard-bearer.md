+++
id = "ref/arc-cavalier/standard-bearer"
kind = "archetype"
title = "Standard Bearer"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Standard%20Bearer"
source_ids = ["ultimate-combat", "chronicle-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "standard_bearer", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "ultimate-combat"
page = "39"
[[sources]]
publication = "chronicle-of-legends"
page = "4"

[fields]
kind = "archetype"
features = [
  { anchor = "banner", level = 1 },
  { anchor = "mount", level = 5 },
  { anchor = "banner-of-solace", level = 11 },
  { anchor = "awesome-pennon", level = 20 },
]
trades = [
  { replaces = "Mount", feature = "mount", by = ["banner"] },
  { replaces = "Banner", feature = "banner", by = ["mount"] },
  { replaces = "Mighty charge", feature = "mighty-charge", by = ["banner-of-solace"] },
  { replaces = "Supreme charge", feature = "supreme-charge", by = ["awesome-pennon"] },
]
+++

Not all cavaliers are content to ride at the head of a charge, leading from the front and facing
down their enemies directly. Some prefer to stand away from the fray, their banners a beacon shining
brightly over the battlefield, rallying their troops to victory. The standard bearer employs the
banner of his order, his lord, or his own house to raise the spirits of his allies and warns enemies
of impending doom.

## Banner (Ex) {#banner}

At 1st level, a standard bearer gains the banner ability. This ability is identical to the standard
cavalier's banner ability, except that the morale bonuses on saving throws against fear effects and
on attack rolls made as part of a charge increase at 5th level, and every five levels thereafter.
This ability replaces the standard cavalier's mount ability.

## Mount (Ex) {#mount}

At 5th level, a standard bearer gains the service of a loyal and trusted mount. This mount is
identical in all ways to the standard cavalier's mount. This ability replaces the standard
cavalier's banner ability.

## Banner of Solace (Ex) {#banner-of-solace}

At 11th level, a standard bearer's banner becomes an even more potent symbol of protection and
inspiration to those around him. Once per day, while his banner is displayed, the standard bearer
can wave it through the air as a full-round action, granting all allies within 60 feet
[temporary hit points](ref/rule/temporary-hit-points) equal to 1/2 his cavalier level, and a +2
morale bonus on their next damage rolls. At 15th level, and every four levels thereafter, this bonus
increases by +1 (to a maximum of +4 at 19th level). The temporary hit points last for 10 minutes or
until depleted, whichever occurs first. This ability replaces mighty charge.

## Awesome Pennon (Ex) {#awesome-pennon}

At 20th level, a standard bearer's banner has become a powerful rallying point to his allies, and a
bane to his foes. Whenever his banner is visible, allies of the standard bearer within 60 feet gain
a +1 morale bonus on attack rolls, immunity to fear effects, and a +3 morale bonus on saving throws
against mind-affecting effects. This ability replaces supreme charge.
