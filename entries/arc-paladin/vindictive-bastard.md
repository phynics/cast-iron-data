+++
id = "ref/arc-paladin/vindictive-bastard"
kind = "archetype"
title = "Vindictive Bastard"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Vindictive%20Bastard"
source_ids = ["antiheros-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vindictive_bastard", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "antiheros-handbook"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "no-aura", level = 1 },
  { anchor = "locate-ally", level = 1 },
  { anchor = "vindictive-smite", level = 1 },
  { anchor = "faded-grace", level = 2 },
  { anchor = "solo-tactics", level = 2 },
  { anchor = "spiteful-tenacity", level = 3 },
  { anchor = "teamwork-feat", level = 3 },
  { anchor = "gang-up", level = 5 },
  { anchor = "swift-justice", level = 11 },
  { anchor = "stalwart", level = 14 },
  { anchor = "aura-of-self-righteousness", level = 17 },
  { anchor = "ultimate-vindication", level = 20 },
]
trades = [
  { replaces = "Detect evil", feature = "detect-evil", by = ["locate-ally"] },
  { replaces = "Smite evil", feature = "smite-evil", by = ["vindictive-smite"] },
  { replaces = "Divine grace", feature = "divine-grace", by = ["faded-grace"] },
  { replaces = "Lay on hands", feature = "lay-on-hands", by = ["solo-tactics"] },
  { replaces = "Divine health", feature = "divine-health", by = ["spiteful-tenacity"] },
  { replaces = "Mercy", feature = "mercy", by = ["teamwork-feat"] },
  { replaces = "channel energy", feature = "channel-positive-energy", by = ["teamwork-feat"] },
  { replaces = "Divine bond", feature = "divine-bond", by = ["gang-up"] },
  { replaces = "Aura of justice", feature = "aura-of-justice", by = ["swift-justice"] },
  { replaces = "Aura of faith", feature = "aura-of-faith", by = ["stalwart"] },
  { replaces = "Aura of righteousness", feature = "aura-of-righteousness", by = ["aura-of-self-righteousness"] },
  { replaces = "Holy champion", feature = "holy-champion", by = ["ultimate-vindication"] },
  { alters = "Aura", by = ["no-aura"] },
]
+++

While paladins often collaborate with less righteous adventurers in order to further their causes,
those who spend too much time around companions with particularly loose morals run the risk of
adopting those same unscrupulous ideologies and methods. Such a vindictive bastard, as these fallen
paladins are known, strikes out for retribution and revenge, far more interested in tearing down
those who have harmed her or her companions than furthering a distant deity's cause.

This is an ex-class archetype and can be taken by a character immediately upon becoming an
ex-paladin.

## No Aura {#no-aura}

A vindictive bastard does not radiate an alignment aura.

This alters the paladin's aura.

## Locate Ally (Sp) {#locate-ally}

Once per day, a vindictive bastard can cast _[locate creature](ref/spell/locate-creature)_ as a
[spell-like ability](ref/umr/spell-like-abilities) with a caster level equal to her paladin level,
but she can do so only to target an ally whom she has spent at least 24 hours in close proximity to
within the last week. This replaces detect evil.

## Vindictive Smite (Ex) {#vindictive-smite}

A vindictive bastard is particularly ruthless against those who have harmed her or her allies. Once
per day as a swift action, she can smite one target within sight who has dealt hit point damage to
her or an ally. She adds her Charisma modifier to her attack rolls and adds her paladin level to
damage rolls against the target of her smite. In addition, while vindictive smite is in effect, the
vindictive bastard gains a deflection bonus equal to her Charisma bonus (if any) to her AC against
attacks by the target of the smite. If the target of vindictive smite has rendered an ally of the
vindictive bastard unconscious or dead within the last 24 hours, the bonus on damage rolls on the
first attack that hits increases by 2 for every paladin level she has.

The vindictive smite effect remains until the target of the smite is dead or the next time the
vindictive bastard rests and regains her uses of this ability. At 4th level and every 3 levels
thereafter, the vindictive bastard can invoke her vindictive smite one additional time per day, to a
maximum of seven times per day at 19th level.

This replaces smite evil.

## Faded Grace (Ex) {#faded-grace}

At 2nd level, a vindictive bastard gains one of the following as a bonus feat:
[Great Fortitude](ref/feat/great-fortitude), [Iron Will](ref/feat/iron-will), or
[Lightning Reflexes](ref/feat/lightning-reflexes).

This replaces divine grace.

## Solo Tactics (Ex) {#solo-tactics}

At 2nd level, a vindictive bastard gains solo tactics, as per the [inquisitor](ref/class/inquisitor)
class feature. She can activate this ability as a swift action and gains the benefits of it for 1
round. She can use this ability a number of rounds per day equal to
[half](ref/misc/fractions-and-rounding) her paladin level + her Charisma modifier.

This replaces lay on hands.

## Spiteful Tenacity (Ex) {#spiteful-tenacity}

At 3rd level, whenever a vindictive bastard has a vindictive smite in effect, she gains the benefits
of the [Diehard](ref/feat/diehard) feat.

This replaces divine health.

## Teamwork Feat {#teamwork-feat}

At 3rd level and every 6 levels thereafter, the vindictive bastard gains a bonus feat in addition to
those gained from normal advancement. These bonus feats must be selected from those listed as
teamwork feats. The vindictive bastard must meet the prerequisites of the selected bonus feat.

This replaces mercy and channel energy.

## Gang Up (Ex) {#gang-up}

At 5th level, a vindictive bastard forms a close bond with her companions. This allows her to spend
a move action to grant [half](ref/misc/fractions-and-rounding) her vindictive smite bonus against a
single target to all allies within 30 feet who can see and hear her. This bonus lasts for a number
of rounds equal to the vindictive bastard's Charisma modifier (minimum 1).

This replaces divine bond.

## Swift Justice (Ex) {#swift-justice}

At 11th level, a vindictive bastard can activate her gang up ability as a swift action.

This replaces aura of justice.

## Stalwart (Ex) {#stalwart}

At 14th level, a vindictive bastard gains stalwart, as per the inquisitor class feature, except she
can also benefit from this ability while wearing heavy armor.

This replaces aura of faith.

## Aura of Self-Righteousness (Ex) {#aura-of-self-righteousness}

At 17th level, a vindictive bastard gains DR 5/lawful or good and immunity to compulsion spells and
[spell-like abilities](ref/umr/spell-like-abilities). Each ally within 10 feet of her gains a +4
morale bonus on saving throws against compulsion effects. Aura of self-righteousness functions only
while the vindictive bastard is conscious, not if she is unconscious or dead.

This replaces aura of righteousness.

## Ultimate Vindication (Ex) {#ultimate-vindication}

At 20th level, if a foe kills one of a vindictive bastard's allies or knocks the vindictive bastard
unconscious (and she later regains consciousness), the vindictive bastard musters a vindictive fury.
The next time she hits that foe within 1 minute, the vindictive bastard can channel the effects of a
_[disintegrate](ref/spell/disintegrate)_ spell through her weapon, using her paladin level as her
effective caster level. Whether or not the target succeeds at its save against the _disintegrate_
effect, it is immune to this ability for the next 24 hours.

This replaces holy champion.
