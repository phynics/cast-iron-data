+++
id = "ref/arc-rogue/shadow-walker"
kind = "archetype"
title = "Shadow Walker"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Shadow%20Walker"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_walker", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "blood-of-shadows"
page = "9"

[fields]
kind = "archetype"
features = [
  { anchor = "expanded-sight", level = 1 },
  { anchor = "illumination-control", level = 3 },
  { anchor = "favored-illumination", level = 4 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["expanded-sight"] },
  { replaces = "Rogue talent gained at 2nd level", feature = "rogue-talents", levels = [2], by = ["illumination-control"] },
  { replaces = "trap sense", feature = "trap-sense", by = ["illumination-control"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["favored-illumination"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["favored-illumination"] },
]
+++

Shadow walkers are comfortable in light, darkness, and the shadows in between. Fetchling rogues
naturally gravitate toward becoming shadow walkers, but shadow walkers exist among other creatures
both above and below the surface.

## Expanded Sight (Su) {#expanded-sight}

At 1st level, a shadow walker gains [darkvision](ref/rule/darkvision) with a range of 30 feet. If
she already has [darkvision](ref/rule/darkvision), the range of her darkvision increases by 10 feet.
When the shadow walker reaches 3rd level, and every 2 rogue levels thereafter, the range of her
darkvision increases by 10 feet. Also at 3rd level, the shadow walker loses the
[light sensitivity](ref/umr/light-sensitivity) weakness, if she has it. If she has
[light blindness](ref/umr/light-blindness), she instead treats it as light sensitivity.

This ability replaces trapfinding.

## Illumination Control (Sp) {#illumination-control}

At 3rd level, a shadow walker can manipulate nearby illumination. At the start of each day, a shadow
walker gains a number of illumination points equal to half her rogue level and can spend
illumination points to use certain [spell-like abilities](ref/umr/spell-like-abilities). As long as
she has at least 1 illumination point, she can cast _[light](ref/spell/light)_ at will. She can
spend 2 illumination points to cast _[darkness](ref/spell/darkness)_, and 3 illumination points to
cast _[daylight](ref/spell/daylight)_, _[deeper darkness](ref/spell/deeper-darkness)_, or
_[motes of dusk and dawn](ref/spell/motes-of-dusk-and-dawn)_ (see page 28). These
[spell-like abilities](ref/umr/spell-like-abilities) have a caster level equal to the shadow
walker's rogue level. Using these spell-like abilities does not hamper the shadow walker's vision;
for example, she can see through the _[deeper darkness](ref/spell/deeper-darkness)_ she creates, and
does not take penalties for light sensitivity in the area of her own
_[daylight](ref/spell/daylight)_.

This ability replaces the rogue talent gained at 2nd level and trap sense.

## Favored Illumination (Su) {#favored-illumination}

At 4th level, a shadow walker chooses one [illumination level](ref/rule/vision-and-light): bright
light, normal light, dim light, or darkness (including supernatural darkness). While she is within
her chosen illumination level, she gains a +2 bonus on initiative checks and Acrobatics, Perception,
and Sleight of Hand skill checks, and can take 10 on any Stealth check attempted within that
illumination level. When the shadow walker confirms a critical hit with a melee attack that deals
sneak attack damage while in her chosen illumination level, she regains 1 illumination point (to a
maximum of half her rogue level). Confirming a critical hit on a creature that has fewer Hit Dice
than half the shadow walker's character level doesn't restore illumination points. When the shadow
walker reaches 6th level, and every 3 rogue levels thereafter, the bonuses she gains within her
chosen illumination level increase by 1.

This ability replaces the rogue's uncanny dodge and improved uncanny dodge.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the shadow walker archetype: deft palm, gloom magic, greater
gloom magic, obscuring blow, surprise attack, umbral gear.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the shadow walker archetype: hide in plain sight,
see in darkness, slippery mind, unwitting ally, and weapon snatcher.
