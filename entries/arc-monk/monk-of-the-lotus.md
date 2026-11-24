+++
id = "ref/arc-monk/monk-of-the-lotus"
kind = "archetype"
title = "Monk of the Lotus"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Monk%20of%20the%20Lotus"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "monk_of_the_lotus", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "advanced-players-guide"
page = "114"

[fields]
kind = "archetype"
features = [
  { anchor = "touch-of-serenity", level = 1 },
  { anchor = "touch-of-surrender", level = 12 },
  { anchor = "touch-of-peace", level = 15 },
  { anchor = "learned-master", level = 17 },
]
trades = [
  { replaces = "Stunning Fist", feature = "stunning-fist", by = ["touch-of-serenity"] },
  { replaces = "Abundant step", feature = "abundant-step", by = ["touch-of-surrender"] },
  { replaces = "Quivering palm", feature = "quivering-palm", by = ["touch-of-peace"] },
  { replaces = "Tongue of the sun and the moon", feature = "tongue-of-the-sun-and-moon", by = ["learned-master"] },
]
+++

Monks are warriors who hone their bodies into deadly weapons, but some monks eschew violence in
favor of a more peaceful philosophy. While a monk of the lotus realizes that combat cannot always be
avoided - and is more than capable in a fight - he understands that all creatures are connected, and
to harm another is to harm the self. Instead, he strives to find peaceful resolutions to conflicts,
and in doing so, hopes to achieve inner peace. A monk of the lotus has the following class features.

## Touch of Serenity (Su) {#touch-of-serenity}

At 1st level, a monk of the lotus gains [Touch of Serenity](ref/feat/touch-of-serenity) as a bonus
feat, even if he does not meet the prerequisites. At 6th level, and every six levels thereafter, the
duration of Touch of Serenity increases by 1 round. Each round on its turn, the target may attempt a
new Will save to end the effect. This duration does not stack; only the longest remaining duration
applies. This ability replaces Stunning Fist.

## Touch of Surrender (Su) {#touch-of-surrender}

At 12th level, a monk of the lotus makes a foe into a friend with a single show of mercy. As an
immediate action, when one of his melee attacks would reduce a creature to 0 or fewer hit points,
the monk can spend 6 _ki_ points to make the target of that attack surrender. When the target
surrenders, it is reduced to 0 hit points, becomes [disabled](ref/misc/disabled), and is charmed, as
if the monk had cast _[charm monster](ref/spell/charm-monster)_ with a caster level equal to the
monk's level. The target does not get a saving throw against this effect. This charm lasts until its
duration expires, until the monk dismisses it or uses it on another creature, or until the target is
again reduced to 0 or fewer hit points, whichever happens first. The monk can only have one creature
charmed with touch of surrender at a time. This is a mind-affecting charm effect. This ability
replaces abundant step.

## Touch of Peace (Su) {#touch-of-peace}

At 15th level, a monk of the lotus can set up vibrations within the body of another creature to win
over the creature's mind. The monk can use touch of peace once per day, and must announce his intent
before making his attack roll. On a successful hit, the attack deals no damage, but the target is
charmed as if the monk had cast _[charm monster](ref/spell/charm-monster)_ with a caster level equal
to the monk's level. The target does not get a saving throw against this effect. The creature is
charmed for 1 day per level. If the monk or his allies attack the charmed creature, or if the monk
asks or commands the charmed creature to take hostile actions, the effect ends. This is a
mind-affecting charm effect. This ability replaces quivering palm.

## Learned Master (Ex) {#learned-master}

At 17th level, a monk of the lotus gains all [Knowledge](ref/skill/knowledge-all) skills and the
[Linguistics](ref/skill/linguistics) skill as class skills. The monk uses Wisdom instead of
Intelligence as the key ability for these skills. This ability replaces tongue of the sun and the
moon.
