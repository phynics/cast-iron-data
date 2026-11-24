+++
id = "ref/arc-monk/monk-of-the-four-winds"
kind = "archetype"
title = "Monk of the Four Winds"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Monk%20of%20the%20Four%20Winds"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "monk_of_the_four_winds", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "advanced-players-guide"
page = "112"

[fields]
kind = "archetype"
features = [
  { anchor = "elemental-fist", level = 1 },
  { anchor = "slow-time", level = 12 },
  { anchor = "aspect-master", level = 17 },
  { anchor = "aspect-of-the-carp" },
  { anchor = "aspect-of-the-ki-rin" },
  { anchor = "aspect-of-the-monkey" },
  { anchor = "aspect-of-the-oni" },
  { anchor = "aspect-of-the-owl" },
  { anchor = "aspect-of-the-tiger" },
  { anchor = "immortality", level = 20 },
]
trades = [
  { replaces = "Stunning Fist", feature = "stunning-fist", by = ["elemental-fist"] },
  { replaces = "Abundant step", feature = "abundant-step", by = ["slow-time"] },
  { replaces = "Timeless body", feature = "timeless-body", by = ["aspect-master"] },
  { replaces = "Perfect self", feature = "perfect-self", by = ["immortality"] },
]
+++

The monk of the four winds is connected to the natural world in a way few other creatures - even
other monks - can hope to match. He can call upon the elements and the spirits of the world in times
of need, and as he nears his goal of perfection, he gains the ability to slow down time and even
defeat death itself. A monk of the four winds has the following class features.

## Elemental Fist (Su) {#elemental-fist}

At 1st level, a monk of the four winds gains [Elemental Fist](ref/feat/elemental-fist) as a bonus
feat, even if he does not meet the prerequisites. At 5th level, and every five levels thereafter,
the monk increases the damage of his Elemental Fist by 1d6 (2d6 at 5th level, 3d6 at 10th level, and
so on). This ability replaces Stunning Fist.

## Slow Time (Su) {#slow-time}

At 12th level, a monk of the four winds can use his _ki_ to slow time or quicken his movements,
depending on the observer. As a swift action, the monk can expend 6 _ki_ points to gain three
standard actions during his turn instead of just one. The monk can use these actions to do the
following: take a melee attack action, use a skill, use an extraordinary ability, or take a move
action. The monk cannot use these actions to cast spells or use
[spell-like abilities](ref/umr/spell-like-abilities), and cannot combine them to take full-attack
actions. Any move actions the monk makes this turn do not provoke attacks of opportunity. This
ability replaces abundant step.

## Aspect Master (Su) {#aspect-master}

At 17th level, a monk of the four winds must choose an aspect of one of the great spirits of the
world. Once made, this choice cannot be changed. This spirit grants the monk a new appearance and
new abilities, as well as changing or augmenting the monk's personality in some way. Once this
choice is made, it cannot be changed. The monk must abide by the alignment restrictions of the
aspect. If the monk ever changes his alignment to something outside the aspect's alignment
restrictions, he loses this ability and cannot regain it unless his alignment later changes again to
match that of the aspect. This ability replaces timeless body.

## Aspect of the Carp {#aspect-of-the-carp}

The monk's skin becomes a coat of golden, iridescent fish scales, his neck grows gills, and his
fingers become webbed. He can breathe water and gains a swim speed equal to his land speed. The carp
is heroic and adventurous—a monk must be nonevil to take on the aspect of the carp.

## Aspect of the Ki-Rin {#aspect-of-the-ki-rin}

The monk's skin takes on a golden luminescence, and a silvery mane that cannot be bound grows atop
his head. He gains a fly speed equal to his land speed, but he must end each turn on the ground. If
the monk does not land by the end of his turn, he falls from whatever height he has attained. The
ki-rin is honorable, honest, and self-sacrificing—a monk must be lawful good to take on the aspect
of the ki-rin.

## Aspect of the Monkey {#aspect-of-the-monkey}

The monk's face becomes that of a monkey, and he grows a prehensile tail. The monk can pick up
objects and make unarmed attacks with his tail (though the tail does not grant additional unarmed
attacks or natural attacks). In addition, the monk gains a climb speed equal to his land speed. The
monkey is a creature of whimsy and a lover of pranks—a monk of any alignment can take on the aspect
of the monkey.

## Aspect of the Oni {#aspect-of-the-oni}

The monk's skin becomes pitch black, and his hair turns white, black, red, or violet. He can assume
_[gaseous form](ref/spell/gaseous-form)_ (as the spell) as a standard action for 1 minute per day
per monk level. This duration does not need to be consecutive, but it must be spent in 1-minute
increments. The oni is treacherous and deceitful, and it hungers for the pain and death of living
creatures—a monk must be evil to take on the aspect of the oni.

## Aspect of the Owl {#aspect-of-the-owl}

The monk grows feathers, and his head becomes avian, with wide, unblinking eyes. He gains a fly
speed of 30 feet. The owl is a sage creature, deeply serious, and driven toward a single goal—a monk
of any alignment can take on the aspect of the owl.

## Aspect of the Tiger {#aspect-of-the-tiger}

Dark stripes appear on the monk's skin, and his face becomes more feline. His eyes become catlike,
with vertical pupils, and his canines enlarge. Once per hour, the monk can move at 10 times his
normal land speed when he makes a charge and is treated as if he had the [pounce](ref/umr/pounce)
ability. The tiger is swift, fierce, and deadly—a monk of any alignment can take on the aspect of
the tiger.

## Immortality (Su) {#immortality}

At 20th level, a monk of the four winds no longer ages. He remains in his current age category
forever. Even if the monk comes to a violent end, he spontaneously
_[reincarnates](ref/spell/reincarnate)_ (as the spell) 24 hours later in a place of his choosing
within 20 miles of the place he died. The monk must have visited the place in which he returns back
to life at least once. This ability replaces perfect self.
