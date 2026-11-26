+++
id = "ref/arc-cavalier/green-knight"
kind = "archetype"
title = "Green Knight"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Green%20Knight"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "green_knight", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "44"

[fields]
kind = "archetype"
features = [
  { anchor = "beast-tongue", level = 1 },
  { anchor = "implacable-knight", level = 1 },
  { anchor = "nature-s-servant" },
  { anchor = "ferocious", level = 3 },
  { anchor = "woodland-stride", level = 4 },
  { anchor = "stalwart", level = 9 },
  { anchor = "oaken-vitality", level = 11 },
  { anchor = "take-their-heads" },
  { anchor = "indestructible", level = 20 },
]
trades = [
  { replaces = "Tactician", feature = "tactician", by = ["beast-tongue"] },
  { replaces = "Mount", feature = "mount", by = ["implacable-knight"] },
  { replaces = "Cavalier's charge", feature = "cavalier-s-charge", by = ["ferocious"] },
  { replaces = "Expert trainer", feature = "expert-trainer", by = ["woodland-stride"] },
  { replaces = "banner", feature = "banner", by = ["woodland-stride"] },
  { replaces = "Greater tactician", feature = "greater-tactician", by = ["stalwart"] },
  { replaces = "Mighty charge", feature = "mighty-charge", by = ["oaken-vitality"] },
  { replaces = "greater banner", feature = "greater-banner", by = ["oaken-vitality"] },
  { replaces = "Master tactician", feature = "master-tactician", by = ["take-their-heads"] },
  { replaces = "Supreme charge", feature = "supreme-charge", by = ["indestructible"] },
  { alters = "Order", feature = "order", by = ["nature-s-servant"] },
]
+++

Some knights serve nature itself and can be found protecting unspoiled natural places or serving fey
beings.

## Beast Tongue (Ex) {#beast-tongue}

A green knight can use Diplomacy to improve an animal's attitude. Beast tongue otherwise functions
like the druid's [wild empathy](ref/ability/wild-empathy) ability, using the green knight's
Diplomacy modifier and using her cavalier level as her effective druid level, and it counts as that
ability for the purpose of other effects (such as feat prerequisites or effects that alter or
improve wild empathy).

This replaces tactician.

## Implacable Knight (Ex) {#implacable-knight}

A green knight gains [Endurance](ref/feat/endurance) and [Diehard](ref/feat/diehard) as bonus feats.

This replaces mount.

## Nature's Servant (Ex) {#nature-s-servant}

A green knight must select the [order of the Green](ref/order/order-of-the-green).

This alters order.

## Ferocious (Ex) {#ferocious}

At 3rd level, a green knight is not staggered when below 0 hit points. At 9th level, taking actions
when below 0 hit points does not cause her to lose hit points.

This replaces cavalier's charge.

## Woodland Stride (Ex) {#woodland-stride}

At 4th level, a green knight gains the druid's [woodland stride](ref/ability/woodland-stride)
ability.

This replaces expert trainer and banner.

## Stalwart (Ex) {#stalwart}

At 9th level, whenever a green knight succeeds at a Fortitude or Will save against an effect that
has a reduced effect on a successful save, she instead negates the effect.

This replaces greater tactician.

## Oaken Vitality (Su) {#oaken-vitality}

At 11th level, nature protects a green knight from many afflictions. The green knight becomes immune
to disease, [infestations](ref/rule/infestations), and poison.

This replaces mighty charge and greater banner.

## Take Their Heads (Su) {#take-their-heads}

A green knight's blade is blessed by mighty fey powers and unerringly seeks out foes' necks. At 17th
level, any slashing weapon a green knight wields gains the _[vorpal](ref/magic-enh/vorpal)_ weapon
special ability.

This replaces master tactician.

## Indestructible (Su) {#indestructible}

At 20th level, a green knight is virtually impervious to death. She gains a +6 bonus to her
Constitution score. In addition, the green knight becomes immune to death effects and to effects
that would kill her without reducing her to 0 hit points, unless the effect involves decapitation.
If she is decapitated, the green knight can continue to act normally. Reattachment requires the head
and body to be joined and the application of any effect that restores hit points.

This replaces supreme charge.
