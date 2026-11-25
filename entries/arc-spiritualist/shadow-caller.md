+++
id = "ref/arc-spiritualist/shadow-caller"
kind = "archetype"
title = "Shadow Caller"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Shadow%20Caller"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_caller", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "50"

[fields]
kind = "archetype"
features = [
  { anchor = "shadowcaster" },
  { anchor = "shade" },
  { anchor = "emotionless" },
  { anchor = "weakening-touch" },
  { anchor = "umbral-shroud" },
  { anchor = "shadow-caster" },
  { anchor = "midnight-shroud" },
  { anchor = "inhabit-shadow", level = 1 },
  { anchor = "shadow-bound", level = 1 },
  { anchor = "shadow-jump", level = 6 },
  { anchor = "see-in-darkness", level = 9 },
  { anchor = "umbral-aura", level = 10 },
  { anchor = "living-darkness", level = 20 },
]
trades = [
  { replaces = "Shared consciousness", feature = "shared-consciousness", by = ["inhabit-shadow"] },
  { replaces = "Etheric tether", feature = "etheric-tether", by = ["shadow-bound"] },
  { replaces = "Phantom recall", feature = "phantom-recall", by = ["shadow-jump"] },
  { replaces = "See invisibility", feature = "see-invisibility", by = ["see-in-darkness"] },
  { replaces = "Fused consciousness", feature = "fused-consciousness", by = ["umbral-aura"] },
  { replaces = "Empowered consciousness", feature = "empowered-consciousness", by = ["living-darkness"] },
  { alters = "Spellcasting", feature = "spells", by = ["shadowcaster"] },
  { alters = "Phantom", feature = "phantom", by = ["shade"] },
]
+++

While most spiritualists form a bond with the remnants of a creature's soul, some explore ways to
bind ephemeral shadows to their own souls in exchange for power.

## Shadowcaster {#shadowcaster}

A shadow caller adds _[darkness](ref/spell/darkness)_ and
_[deeper darkness](ref/spell/deeper-darkness)_ to their class spell list as 2nd- and 3rd-level
spells, respectively. When her shade (see below) inhabits her shadow, the shadow caller's effective
caster level is one higher when she casts all spells with the shadow or darkness descriptor.

This ability alters the spiritualist's spellcasting.

## Shade {#shade}

A shadow caller gains a special kind of phantom known as a shade. A shade functions as a phantom,
except as noted below. A shade is from the Shadow Plane instead of the Ethereal Plane. A shade is
not confined to the shadow caller's consciousness, but instead inhabits her shadow.

This ability alters phantom.

## Emotionless (Su) {#emotionless}

A shadow caller's shade lacks an emotional focus; it is cold and devoid of all emotions. The shade
gains a number of ranks in Intimidate and Stealth equal to its Hit Dice. The shadow caller gains
[Skill Focus](ref/feat/skill-focus) in each of these skills while the shade inhabits her shadow. The
shade has good Reflex and Will saves, gains [Lightning Reflexes](ref/feat/lightning-reflexes) as a
bonus feat, and gains the following abilities.

## Weakening Touch (Su) {#weakening-touch}

A shade's slam attack causes its victim to take a -2 penalty to Strength for 1 round. As a standard
action, a shade in incorporeal form can deliver the penalty as a touch attack. This penalty does not
stack with itself. This is a negative energy effect.

## Umbral Shroud (Su) {#umbral-shroud}

When the shadow caller reaches 7th level, her shade can emit a 10-foot aura of swirling shadows that
grants all allies 20% [concealment](ref/rule/concealment) against creatures without
[darkvision](ref/rule/darkvision) or the [see in darkness](ref/umr/see-in-darkness) ability, and a
+4 bonus on Stealth checks.

## Shadow Caster (Sp) {#shadow-caster}

When the shadow caller reaches 12th level, her shade gains the ability to cast either
_[shadow conjuration](ref/spell/shadow-conjuration)_ or
_[shadow evocation](ref/spell/shadow-evocation)_ once per day. It uses its Hit Dice as its caster
level, and the DC for these spells equals 10 + 1/2 the shade's Hit Dice + its Charisma modifier.
Instead of the normal spell level and percentage of reality for the two spells, the maximum spell
level of the duplicated spell is 4th level, and the effects are 40% real. When the shadow caller
reaches 18th level, the maximum spell level improves to 6th level and effects are 60% real.

## Midnight Shroud (Su) {#midnight-shroud}

When the shadow caller reaches 17th level, her shade's umbral shroud also lowers the
[light level](ref/rule/vision-and-light) in its range to [darkness](ref/spell/darkness), regardless
of the prevailing conditions; this counts as a 7th-level _darkness_ spell for the purpose of
adjudicating light and darkness effects.

## Inhabit Shadow (Su) {#inhabit-shadow}

A shade resides within a shadow caller's own shadow. When the shade is summoned, the shadow caller
does not cast a shadow under any circumstances. Creatures that don't normally cast shadows (such as
vampires) cannot be shadow callers. While the shade inhabits its master's shadow, the shadow caller
gains a +4 circumstance bonus on Stealth checks against creatures without
[darkvision](ref/rule/darkvision) or the
[see in darkness](ref/carried/bestiary/rules/universal-monster-rules/see-in-darkness) ability; at
12th level, this bonus increases to +8. Additionally, the shadow caller gains darkvision 60 feet
while her shade inhabits her shadow. If the shadow caller already has darkvision, its range
increases by 30 feet.

This ability replaces shared consciousness.

## Shadow Bound (Su) {#shadow-bound}

A shadow caller's shade remains stable while adjacent to the shadow caller, or while up to 5 feet
away from the shadow caller for every 5 levels the shadow caller possesses. If the shade moves
beyond this distance, it is automatically dismissed back to the Shadow Plane (preventing the shade
from being summoned back for 24 hours) unless the shadow caller concentrates as per the etheric
tether ability. However, if both the shadow caller and shade are in areas of total darkness, the
shade can move any distance from the shadow caller. If the shade is beyond its maximum distance and
enters an area of dim or brighter illumination, it immediately returns to the Shadow Plane and
cannot be summoned for 24 hours.

This ability replaces etheric tether.

## Shadow Jump (Su) {#shadow-jump}

At 6th level, when a shadow caller's shade inhabits her shadow, she can travel between shadows as
per the [shadowdancer's](ref/pclass/shadowdancer) shadow jump ability. Each day, she can travel a
total of 40 feet per spiritualist level in this way and, as with a shadowdancer, the distance is
rounded to the nearest 10-foot increment.

This ability replace phantom recall.

## See in Darkness (Su) {#see-in-darkness}

At 9th level, a shadow caller can gain the [see in darkness](ref/umr/see-in-darkness) universal
monster ability as a standard action. She can use this ability for a number of rounds per day equal
to her spiritualist level, though these rounds need not be consecutive.

This ability replaces _see invisibility_.

## Umbral Aura (Su, Sp) {#umbral-aura}

At 10th level, a shadow caller is wreathed in an aura of [darkness](ref/spell/darkness) while her
shade inhabits her shadow, gaining 50% [concealment](ref/rule/concealment) against creatures without
[darkvision](ref/rule/darkvision) or the
[see in darkness](ref/carried/bestiary/rules/universal-monster-rules/see-in-darkness) ability.
Additionally, the shadow caller's square and all adjacent squares are treated as areas of dim
illumination while she benefits from this ability; this second effect counts as a 4th-level
_darkness_ spell for the purpose of adjudicating light and darkness effects. While her shade
inhabits her shadow, the shadow caller can hide in plain sight, even if an observing creature has
[darkvision](ref/rule/darkvision) or
[see in darkness](ref/carried/bestiary/rules/universal-monster-rules/see-in-darkness).

This ability replaces fused consciousness.

## Living Darkness (Su) {#living-darkness}

At 20th level, a shadow caller becomes a creature of absolute darkness. When using her incorporeal
bonded manifestation, she is immune to cold and mind-affecting effects and gains an incorporeal
touch attack that she can use as a standard action to deal 20d6 points of negative energy damage.
When the shadow caller damages a creature with this ability, she gains 5d6
[temporary hit points](ref/rule/temporary-hit-points) (Fortitude half; DC = 20 + her Wisdom
modifier), so long as she doesn't already have any temporary hit points gained via this ability).
Temporary hit points gained this way disappear after 1 hour.

This ability replaces empowered consciousness.
