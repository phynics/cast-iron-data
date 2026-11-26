+++
id = "ref/arc-ranger/flamewarden"
kind = "archetype"
title = "Flamewarden"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Flamewarden"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flamewarden", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "72"

[fields]
kind = "archetype"
features = [
  { anchor = "touch-of-flame", level = 4 },
  { anchor = "spells" },
  { anchor = "stoking-the-embers", level = 9 },
  { anchor = "burning-renewal", level = 12 },
  { anchor = "phoenix-rising", level = 16 },
]
trades = [
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["touch-of-flame"] },
  { replaces = "Evasion", feature = "evasion", by = ["stoking-the-embers"] },
  { replaces = "Camouflage", feature = "camouflage", by = ["burning-renewal"] },
  { replaces = "Improved evasion", feature = "improved-evasion", by = ["phoenix-rising"] },
  { replaces = "master hunter", feature = "master-hunter", by = ["phoenix-rising"] },
  { alters = "Spells", feature = "spells", by = ["spells"] },
]
+++

Emulating the blazing phoenix, flamewardens sweep through the world like a selective forest fire,
burning away corruption, evil, and those who cling to decay.

## Touch of Flame (Su) {#touch-of-flame}

At 4th level, a flamewarden can cause his weapons to burst into flame. As a standard action, the
ranger can grant a single weapon he holds the _[flaming](ref/magic-enh/flaming)_ special ability for
1 minute; while under this effect, the weapon counts as magic for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction). A flamewarden can use this ability a number of times
per day equal to 3 + his Wisdom modifier. At 12th level, weapons affected by this ability gain the
_[flaming burst](ref/magic-enh/flaming-burst)_ special ability instead.

This replaces hunter's bond.

## Spells {#spells}

A flamewarden can prepare spells from the druid list that have the fire descriptor.

This alters the ranger's spells.

## Stoking the Embers (Sp) {#stoking-the-embers}

At 9th level, a flamewarden can fan the last spark of a recently slain creature's life force back
into a full flame. Once per day as a standard action, a flamewarden can touch the corpse of a
creature that has died within 1 round to grant it the effects of
_[breath of life](ref/spell/breath-of-life)_.

This replaces evasion.

## Burning Renewal (Su) {#burning-renewal}

At 12th level, a flamewarden can use the cleansing power of fire to remove afflictions from his
body, mind, and soul. When the flamewarden takes 5 or more points of fire damage, he can remove one
of the following conditions: fatigued, shaken, or sickened. Alternatively, he can remove 1 point of
[ability damage](ref/rule/ability-damage-drain) or drain from an ability score of his choice.

If the flamewarden takes 10 or more points of fire damage, he can remove one of the following
conditions: exhausted, frightened, or nauseated. Alternatively, he can remove 1d6 points of ability
damage or drain from an ability score of his choice.

The ranger can use this ability only once each time he takes fire damage, regardless of how much
damage it deals over the required amount. He can use this ability a number of times per day equal to
3 + her Wisdom modifier.

If the flamewarden has fire [resistance](ref/umr/resistance) or [immunity](ref/umr/immunity) to
fire, fire damage he would have otherwise taken still counts toward activating burning renewal.

This replaces camouflage.

## Phoenix Rising (Su) {#phoenix-rising}

At 16th level, if a flamewarden dies, his body explodes in a conflagration in a 20-foot
[spread](ref/misc/spread). Each hostile creature in the area takes 10d6 points of fire damage unless
it succeeds at a Reflex save (DC = 10 + half the ranger's level + his Constitution modifier) for
half damage. The flames don't harm the flamewarden's allies, who instead are healed 5d6 points of
damage, and any poisons they are currently suffering are neutralized as per
_[neutralize poison](ref/spell/neutralize-poison)_. The flamewarden's body is reduced to ashes by
the explosion.

At 20th level, the flamewarden gains immunity to fire, and once per week, the flamewarden rises from
the ashes of his own destruction 1 round after dying. The flamewarden's body re-forms with all his
equipment, and he returns to life with half his maximum hit points. Any ability scores that were 0
become 1, and nonmagical diseases and poisons are cured. A _[limited wish](ref/spell/limited-wish)_,
_[miracle](ref/spell/miracle)_, or _[wish](ref/spell/wish)_ spell cast before he rises from the
ashes prevents him from doing so, as does the area of an _[unhallow](ref/spell/unhallow)_ effect.

This replaces improved evasion and master hunter.
