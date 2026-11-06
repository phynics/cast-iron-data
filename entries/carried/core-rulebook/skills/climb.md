+++
id = "ref/carried/core-rulebook/skills/climb"
kind = "skill"
title = "Climb"
source_ids = ["core-rulebook"]
section = ["Skills"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Skills/Climb", path = "core_rulebook/skill/climb.json" },
]

[fields]
kind = "none"
+++

::: statblock
Key Ability: Str
Trained Only: Yes
Armor Check Penalty: Yes
:::

_You are skilled at scaling vertical surfaces, from smooth city walls to rocky cliffs._

## Check {#check}

With a successful Climb check, you can advance up, down, or across a slope, wall, or other steep
incline (or even across a ceiling, provided it has handholds) at one-quarter your normal speed. A
slope is considered to be any incline at an angle measuring less than 60 degrees; a wall is any
incline at an angle measuring 60 degrees or more.

A Climb check that fails by 4 or less means that you make no progress, and one that fails by 5 or
more means that you fall from whatever height you have already attained.

The DC of the check depends on the conditions of the climb. Compare the task with those on the
following table to determine an appropriate DC.

### Climb DC {#climb-dc}

::: table
head = [
  [
    { text = "Climb DC", header = true },
    { text = "Example Surface or Activity", header = true },
  ],
]
body = [
  [
    { text = "0" },
    { text = "A slope too steep to walk up, or a knotted rope with a wall to brace against." },
  ],
  [
    { text = "5" },
    { text = "A rope with a wall to brace against, or a knotted rope, or a rope affected by the _[rope trick](ref/spell/rope-trick)_ spell." },
  ],
  [
    { text = "10" },
    { text = "A surface with ledges to hold on to and stand on, such as a very rough wall or a ship's rigging." },
  ],
  [
    { text = "15" },
    { text = "Any surface with adequate handholds and footholds (natural or artificial), such as a very rough natural rock surface or a tree, or an unknotted rope, or pulling yourself up when dangling by your hands." },
  ],
  [
    { text = "20" },
    { text = "An uneven surface with narrow handholds and footholds, such as a typical wall in a dungeon." },
  ],
  [
    { text = "25" },
    { text = "A rough surface, such as a natural rock wall or a brick wall." },
  ],
  [
    { text = "30" },
    { text = "An overhang or ceiling with handholds only." },
  ],
  [
    { text = "—" },
    { text = "A perfectly smooth, flat vertical (or inverted) surface cannot be climbed." },
  ],
  [
    { text = "Climb DC Modifier\\*", header = true },
    { text = "Example Surface or Activity", header = true },
  ],
  [
    { text = "–10" },
    { text = "Climbing a chimney (artificial or natural) or other location where you can brace against two opposite walls." },
  ],
  [
    { text = "–5" },
    { text = "Climbing a corner where you can brace against perpendicular walls." },
  ],
  [
    { text = "+5" },
    { text = "Surface is slippery." },
  ],
]
foot = [
  [
    { text = "\\* These modifiers are cumulative; use all that apply.", colspan = 2 },
  ],
]
:::

You need both hands free to climb, but you may cling to a wall with one hand while you cast a spell
or take some other action that requires only one hand. While climbing, you can't move to avoid a
blow, so you lose your Dexterity bonus to AC (if any). You also can't use a shield while climbing.
Anytime you take damage while climbing, make a Climb check against the DC of the slope or wall.
Failure means you fall from your current height and sustain the appropriate falling damage.

### Accelerated Climbing {#accelerated-climbing}

You try to climb more quickly than normal. By accepting a –5 penalty, you can move half your speed
(instead of one-quarter your speed).

### Make Your Own Handholds and Footholds {#make-your-own-handholds-and-footholds}

You can make your own handholds and footholds by pounding pitons into a wall. Doing so takes 1
minute per piton, and one piton is needed per 5 feet of distance. As with any surface that offers
handholds and footholds, a wall with pitons in it has a DC of 15. In the same way, a climber with a
handaxe or similar implement can cut handholds in an ice wall.

### Catch Yourself When Falling {#catch-yourself-when-falling}

It's practically impossible to catch yourself on a wall while falling, yet if you wish to attempt
such a difficult task, you can make a Climb check (DC = wall's DC + 20) to do so. It's much easier
to catch yourself on a slope (DC = slope's DC + 10).

### Catch a Falling Character While Climbing {#catch-a-falling-character-while-climbing}

If someone climbing above you or adjacent to you falls, you can attempt to catch the falling
character if he or she is within your reach. Doing so requires a successful melee touch attack
against the falling character (though he or she can voluntarily forego any Dexterity bonus to AC if
desired). If you hit, you must immediately attempt a Climb check (DC = wall's DC + 10). Success
indicates that you catch the falling character, but his total weight, including equipment, cannot
exceed your heavy load limit or you automatically fall. If you fail your Climb check by 4 or less,
you fail to stop the character's fall but don't lose your grip on the wall. If you fail by 5 or
more, you fail to stop the character's fall and begin falling as well.

## Action {#action}

Climbing is part of movement, so it's generally part of a move action (and may be combined with
other types of movement in a move action). Each move action that includes any climbing requires a
separate Climb check. Catching yourself or another falling character doesn't take an action.

## Special {#special}

You can use a rope to haul a character upward (or lower a character) through sheer strength. You can
lift double your maximum load in this manner.

A creature with a climb speed has a +8 racial bonus on all Climb checks. The creature must make a
Climb check to climb any wall or slope with a DC higher than 0, but it can always choose to take 10,
even if rushed or threatened while climbing. If a creature with a climb speed chooses an accelerated
climb (see above), it moves at double its climb speed (or at its land speed, whichever is slower)
and makes a single Climb check at a –5 penalty. Such a creature retains its Dexterity bonus to Armor
Class (if any) while climbing, and opponents get no special bonus to their attacks against it. It
cannot, however, use the run action while climbing.

If you have the Athletic feat, you get a bonus on Climb checks (see Feats).
