+++
id = "ref/arc-vigilante/bellflower-harvester"
kind = "archetype"
title = "Bellflower Harvester"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Bellflower%20Harvester"
source_ids = ["adventurers-guide", "spymasters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bellflower_harvester", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "adventurers-guide"
page = "42"
[[sources]]
publication = "spymasters-handbook"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "rebellious-identity" },
  { anchor = "bellflower-crop" },
  { anchor = "crop-vigilance", level = 1 },
  { anchor = "obsequious", level = 1 },
  { anchor = "tend-the-garden", level = 2 },
]
trades = [
  { replaces = "Vigilante specialization", feature = "vigilante-specialization", by = ["crop-vigilance"] },
  { replaces = "Social talent gained at 1st level", feature = "social-talent", levels = [1], by = ["obsequious"] },
  { replaces = "Vigilante talent gained at 2nd level", feature = "vigilante-talent", levels = [2], by = ["tend-the-garden"] },
  { alters = "Dual identity", feature = "dual-identity", by = ["rebellious-identity"] },
]
+++

Bellflower harvesters are the front-line operatives of the secretive
[Bellflower Network](ref/rule/aff-antislavery), whose members infiltrate Chelish estates in the
guise of servants and slaves, and tolerate a harsh life as they uncover secrets, gauge security, and
send slaves on the first steps toward freedom. While
[Bellflower tillers](ref/pclass/bellflower-tiller) (see page 40) wander the countryside, escorting
the crop of escapees to freedom, Bellflower harvesters remain in seeming bondage to direct others to
the road to freedom, undermine efforts to recapture slaves, and end the threat of especially vile
masters.

Bellflower harvesters consist almost exclusively of halflings, though the role could be taken by
anyone with the patience or humility to withstand months or years of cruel abuse without risking
being caught raising a hand in his own defense.

## Rebellious Identity (Ex) {#rebellious-identity}

A Bellflower harvester's vigilante identity must be within one step of chaotic good, and his social
identity must appear to be a servant, slave, or other menial laborer.

This alters dual identity.

## Bellflower Crop (Ex) {#bellflower-crop}

As a standard action, a Bellflower harvester can designate a number of allies equal to 3 + his
Charisma modifier as part of his Bellflower crop. Members of a Bellflower crop must remain within 30
feet of the vigilante to gain any benefits from abilities that affect a Bellflower crop, regardless
of the ability's source (whether it's a Bellflower harvester,
[irrigator](ref/arc-rogue/bellflower-irrigator), or [tiller](ref/pclass/bellflower-tiller)). If the
allies leave this range, the Bellflower harvester must designate them again to include them in his
crop.

## Crop Vigilance (Ex) {#crop-vigilance}

When the Bellflower harvester uses the [aid another](ref/rule/aid-another-2) action to grant a
member of his Bellflower crop a bonus on an attack roll against an opponent, on a skill check, or to
AC against an opponent's next attack, the bonus increases to +3. This doesn't stack with the
benefits of other feats or class features that improve the bonus he grants to an ally with aid
another. At 5th level and every 6 vigilante levels thereafter, the bonus that the Bellflower
harvester provides when using aid another to assist a member of his Bellflower crop increases by 1,
to a maximum of +6 at 17th level.

This ability replaces vigilante specialization, but the Bellflower harvester is still treated as if
he had the stalker specialization for the purpose of selecting other vigilante talents.

## Obsequious (Ex) {#obsequious}

A Bellflower harvester works hard to cultivate a social identity that plays off others' racist
assumptions to deflect blame and excuse suspicious behavior, making him seem harmless or even a
model servant. He can use the Bluff skill to deflect suspicion about his vigilante identity and
activities (including use of vigilante talents when in his social identity) rather than Disguise,
and gains a +2 bonus on Bluff checks to do so. This bonus increases by 1 for every 4 vigilante
levels he has beyond 1st, to a maximum of +6 at 17th level.

This ability replaces the social talent gained at 1st level.

## Tend the Garden (Ex) {#tend-the-garden}

At 2nd level, a Bellflower harvester gains the ability to coordinate the members of his Bellflower
crop to improve their performance in battle. He gains [Stealth Synergy](ref/feat/stealth-synergy) as
a bonus feat. As a standard action, a Bellflower harvester can grant any one teamwork feat he has to
all members of his Bellflower crop who can see and hear him. Members of his Bellflower crop retain
this feat for 1 round, plus 1 round for every 5 vigilante levels the Bellflower harvester has beyond
2nd, to a maximum of 4 rounds at 17th level. A Bellflower harvester can share only one teamwork feat
at a time in this manner.

This ability replaces the vigilante talent gained at 2nd level.

## Social Talents {#social-talents}

The following social talents complement the Bellflower harvester:
[case the joint](ref/soctalent/case-the-joint), [feign innocence](ref/soctalent/feign-innocence),
[gossip collector](ref/soctalent/gossip-collector), [loyal aid](ref/soctalent/loyal-aid), and
[subjective truth](ref/soctalent/subjective-truth).

## Vigilante Talents {#vigilante-talents}

The following vigilante talents complement the Bellflower harvester:
[blind spot](ref/vigtalent/blind-spot), environment weapon,
[shadow's sight](ref/vigtalent/shadows-sight), and [team player](ref/vigtalent/team-player) (see
below).
