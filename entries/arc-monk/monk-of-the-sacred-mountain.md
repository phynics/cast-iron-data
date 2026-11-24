+++
id = "ref/arc-monk/monk-of-the-sacred-mountain"
kind = "archetype"
title = "Monk of the Sacred Mountain"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Monk%20of%20the%20Sacred%20Mountain"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "monk_of_the_sacred_mountain", path = "json/archetypes_monk.json" },
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
  { anchor = "iron-monk", level = 2 },
  { anchor = "bastion-stance", level = 4 },
  { anchor = "iron-limb-defense", level = 5 },
  { anchor = "adamantine-monk", level = 9 },
  { anchor = "vow-of-silence", level = 17 },
]
trades = [
  { replaces = "Evasion", feature = "evasion", by = ["iron-monk"] },
  { replaces = "Slow fall", feature = "slow-fall", by = ["bastion-stance"] },
  { replaces = "High jump", feature = "high-jump", by = ["iron-limb-defense"] },
  { replaces = "Improved evasion", feature = "improved-evasion", by = ["adamantine-monk"] },
  { replaces = "Tongue of the sun and the moon", feature = "tongue-of-the-sun-and-moon", by = ["vow-of-silence"] },
]
+++

The monk of the sacred mountain finds strength and power in the earth beneath his feet. Rather than
spinning though the battlefield with the fluid motion of the river, he roots himself to the ground,
as immovable and unshakable as the stones of the mountain. A monk of the sacred mountain has the
following class features.

## Iron Monk (Ex) {#iron-monk}

At 2nd level, a monk of the sacred mountain gains [Toughness](ref/feat/toughness) as a bonus feat.
In addition, the monk gains a +1 natural armor bonus. This ability replaces evasion.

## Bastion Stance (Ex) {#bastion-stance}

At 4th level, a monk of the sacred mountain becomes like stone, nearly impossible to move when he
stands his ground. If the monk starts and ends his turn in the same space, he cannot be knocked
[prone](ref/rule/prone) or forcibly moved until the start of his next turn, except by mind-affecting
or teleportation effects. At 16th level, he is immune to any attempts to force him to move, even
mind-affecting and teleportation effects. This ability replaces slow fall.

## Iron Limb Defense (Ex) {#iron-limb-defense}

At 5th level, a monk of the sacred mountain can deflect blows with an active defense that
complements his bastion stance. If the monk starts and ends his turn in the same space, he gains a
+2 shield bonus to AC and CMD until the start of his next turn. As a swift action, he can spend 1
_ki_ point to increase this bonus to +4. This ability replaces high jump.

## Adamantine Monk (Ex) {#adamantine-monk}

At 9th level, a monk of the sacred mountain has muscles so strong and skin so resilient that he
gains DR 1/—. This DR increases by 1 for every three levels thereafter. As a swift action, the monk
can spend 1 _ki_ point to double his DR until the beginning of his next turn. This ability replaces
improved evasion.

## Vow of Silence (Su) {#vow-of-silence}

At 17th level, a monk of the sacred mountain becomes as impassive as stone, making a vow of silence
in exchange for greater abilities. The monk gains a +2 insight bonus to AC and CMD and a +4 bonus on
Sense Motive, Stealth, and Perception checks. The monk does not lose the capacity for speech, but if
he ever speaks, he loses this feature for 24 hours. This ability replaces tongue of the sun and the
moon.
