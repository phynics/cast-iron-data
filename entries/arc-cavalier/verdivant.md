+++
id = "ref/arc-cavalier/verdivant"
kind = "archetype"
title = "Verdivant"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Verdivant"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "verdivant", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "wilderness-origins"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "plant-mount", level = 1 },
  { anchor = "effloresce", level = 2 },
  { anchor = "sinuous-steps", level = 3 },
]
trades = [
  { replaces = "Expert trainer", feature = "expert-trainer", by = ["plant-mount"] },
  { replaces = "Tactician", feature = "tactician", by = ["effloresce"] },
  { replaces = "banner", feature = "banner", by = ["effloresce"] },
  { replaces = "greater tactician", feature = "greater-tactician", by = ["effloresce"] },
  { replaces = "greater banner", feature = "greater-banner", by = ["effloresce"] },
  { replaces = "master tactician", feature = "master-tactician", by = ["effloresce"] },
  { replaces = "bonus feats", feature = "bonus-feat", by = ["effloresce"] },
  { alters = "Mount", feature = "mount", by = ["plant-mount"] },
  { alters = "Cavalier's charge", feature = "cavalier-s-charge", by = ["sinuous-steps"] },
]
+++

Some vine leshys' spirits are vibrant enough to project this animus beyond their own bodies. Called
verdivants, these leshys explore the world atop unique companions formed from the leshy's vines and
animated by their nearly boundless energy. Both mount and rider brim with new growth, sporting
bright flowers, whipping tendrils, clouds of pollen, and other manifestations charged with nature's
power. This archetype is typically available only to vine leshys, but with the GM's permission,
other races can take it as well.

## Plant Mount (Ex) {#plant-mount}

A verdivant buds off and cultivates his vines into an animal form, imbuing them with limited
intelligence. The verdivant selects a mount appropriate for his size as normal, but this mount is a
plant with the [leshy](ref/subtype/leshy) subtype and has the same immunities as a vine leshy.

A verdivant can absorb and regrow his plant mount. This can either replace a slain mount or change a
mount's form; the new form must still be a suitable mount the verdivant is capable of riding. Either
function takes 1 week, after which the newly regrown mount immediately benefits from its special
abilities.

At 4th level, regrowing a mount takes only 24 hours.

This alters mount and replaces expert trainer.

## Effloresce {#effloresce}

At 2nd level, a verdivant can use a standard action to create efflorescences, explosive growths fed
by his animating spirit. A verdivant can use this ability three times per day, plus one additional
time per day for every 4 cavalier levels he has beyond 2nd. A verdivant can apply effloresces to
himself, or his plant mount if it is adjacent. Efflorescences last for 1 round per cavalier level,
and a verdivant can have at most two efflorescences in effect at a time. A verdivant can end an
efflorescence during his turn as a free action.

At 6th level, a verdivant can effloresce as a move action. At 12th level, a verdivant can effloresce
as a swift action, and he can have two efflorescences in effect simultaneously. At 17th level, a
verdivant can effloresce twice as part of the same action.

At 2nd level, a verdivant can use the following efflorescences.

### Shieldvines (Ex) {#shieldvines}

Allies within 10 feet do not provoke attacks of opportunity when leaving threatened squares; this
increases to 20 feet at 9th level.

### Floatflower (Ex) {#floatflower}

Allies within 10 feet ignore the effects of nonmagical
[difficult terrain](ref/rule/terrain-and-obstacles). At 9th level, they also gain the effects of
_[air walk](ref/spell/air-walk)_ while within 10 feet of the verdivant.

At 5th level, a verdivant gains the following efflorescences.

### Innervating Pollen (Ex) {#innervating-pollen}

The verdivant and his allies within 30 feet gain a competence bonus either on attack rolls or to
saving throws (the verdivant's choice; all allies gain the same benefit) equal to
[one-third](ref/misc/fractions-and-rounding) the verdivant's cavalier level.

### Bolsterbloom (Su) {#bolsterbloom}

The verdivant and his allies within 30 feet gain [fast healing](ref/umr/fast-healing) 1; this
[fast healing](ref/umr/fast-healing) increases by 1 at 9th level, and again at 14th and 17th levels.

At 9th level, a verdivant gains the following efflorescences.

### Charged Blossoms (Su) {#charged-blossoms}

Choose an energy type: acid, cold, electricity, or fire. The verdivant and his allies within 10 feet
gain energy resistance 10 to the chosen energy type. At 14th level this affects allies within 20
feet, and the energy resistance increases to 20.

### Slipstrands (Su) {#slipstrands}

The verdivant and his allies within 10 feet are affected by
_[freedom of movement](ref/spell/freedom-of-movement)_; this increases to 20 feet at 17th level.

At 14th level, a verdivant gains the following efflorescences.

### Ambrosia (Su) {#ambrosia}

The efflorescence temporarily suppresses enchantments, transmutations, and curses on the verdivant
and his allies within 30 feet, as _[break enchantment](ref/spell/break-enchantment)_ with a caster
level equal to the verdivant's cavalier level. Affected creatures ignore the effects of such
conditions for the duration of the efflorescence, after which the conditions' full effects resume.
The duration of suppressed conditions continues to elapse while the condition is suppressed.

### Luckleaf (Su) {#luckleaf}

When attempting a d20 roll, allies of the verdivant within 30 feet of him can roll twice and use the
better result; each ally can benefit from this ability only once per efflorescence. Luckleaf can be
activated once per minute.

This replaces tactician, banner, greater tactician, greater banner, master tactician, and bonus
feats.

## Sinuous Steps (Ex) {#sinuous-steps}

At 3rd level, a verdivant and his plant mount gain the
[woodland stride](ref/ability/woodland-stride) druid class feature. In addition, they do not take
any penalty to AC after making a charge attack.

This alters cavalier's charge.
