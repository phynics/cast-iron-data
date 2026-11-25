+++
id = "ref/arc-hunter/courtly-hunter"
kind = "archetype"
title = "Courtly Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Courtly%20Hunter"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "courtly_hunter", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "64"

[fields]
kind = "archetype"
features = [
  { anchor = "courtly-companion" },
  { anchor = "refined-focus" },
  { anchor = "subtle-companion", level = 2 },
  { anchor = "skill-bond", level = 3 },
  { anchor = "alternate-form", level = 7 },
]
trades = [
  { replaces = "Precise companion", feature = "precise-companion", by = ["subtle-companion"] },
  { replaces = "Hunter tactics", feature = "hunter-tactics", by = ["skill-bond"] },
  { replaces = "the hunter's bonus teamwork feats", feature = "teamwork-feat", by = ["skill-bond"] },
  { replaces = "Bonus tricks", feature = "bonus-tricks", by = ["alternate-form"] },
  { alters = "Animal companion", feature = "animal-companion", by = ["courtly-companion"] },
  { alters = "Animal focus", feature = "animal-focus", by = ["refined-focus"] },
]
+++

While most hunters find themselves at ease in the wildest parts of the world, courtly hunters
instead make their homes in cultured urban environments. They and their animal companions are more
refined than typical hunters, using their skills to navigate the winding paths of courtly intrigue
as surely as other hunters find trails in the wilderness.

## Class Skills {#class-skills}

A courtly hunter adds Bluff, Diplomacy, and Sense Motive to her list of class skills, instead of
Knowledge (geography), Knowledge (nature), and Survival.

This alters the hunter's class skills.

## Courtly Companion {#courtly-companion}

A courtly hunter's animal companion was touched by either the fey or the nature spirits that form
leshys and answer to _[commune with nature](ref/spell/commune-with-nature)_, granting it its own
intelligence. The companion's type changes to [magical beast](ref/type/magical-beast)
([augmented](ref/subtype/augmented) animal), but this doesn't change any of its statistics and it
counts as an animal, not as a magical beast, for the purposes of determining all effects,
prerequisites, and so on. It does not learn tricks, but it does have an Intelligence score equal to
that of a [familiar](ref/sidekick/familiar) belonging to a [wizard](ref/class/wizard) of the courtly
hunter's hunter level. Levels in other classes that grant animal companions do not stack with levels
of courtly hunter for the purpose of determining the abilities of her courtly companion.

This ability alters animal companion.

## Refined Focus (Su) {#refined-focus}

A courtly hunter has access to a different set of animal [aspects](ref/ability/animal-foci) with her
animal focus. She does not gain access to the bear, bull, frog, monkey, snake, stag, tiger, or wolf
aspects. Instead, she gains access to the following aspects.

### Beaver {#beaver}

The creature gains a +4 competence bonus on Craft checks. This bonus increases to +6 at 8th level
and +8 at 15th level.

### Chameleon {#chameleon}

The creature gains a +4 competence bonus on Disguise checks. This bonus increases to +6 at 8th level
and +8 at 15th level.

### Eagle {#eagle}

The creature gains a +2 enhancement bonus to Charisma. This bonus increases to +4 at 8th level and
+6 at 15th level.

### Fox {#fox}

The creature gains a +4 competence bonus on Bluff checks. This bonus increases to +6 at 8th level
and +8 at 15th level.

### Frilled Lizard {#frilled-lizard}

The creature gains a +4 competence bonus on Intimidate checks. This bonus increases to +6 at 8th
level and +8 at 15th level.

### Octopus {#octopus}

The creature gains a +4 competence bonus on Escape Artist checks. This bonus increases to +6 at 8th
level and +8 at 15th level.

### Raccoon {#raccoon}

The creature gains a +4 competence bonus on Sleight of Hand checks. This bonus increases to +6 at
8th level and +8 at 15th level.

### Songbird {#songbird}

The creature gains a +4 competence bonus on Perform checks. This bonus increases to +6 at 8th level
and +8 at 15th level.

This ability alters animal focus.

## Subtle Companion (Su) {#subtle-companion}

At 2nd level, a courtly hunter can transform her animal companion into a similar Tiny animal to
allow it hide easily or even blend in and act as a spy. For instance, a tiger could be transformed
into a housecat, a wolf could be transformed into a Tiny dog, a dire bat could be transformed into a
Tiny flying fox, and so on. This functions as a polymorph effect, and the animal companion gains a
+2 size bonus to Dexterity and a -4 size penalty to Strength (use
[the polymorph table](ref/spelldef/polymorph) on page 212 of the _Pathfinder RPG Core Rulebook_ to
adjust its ability score if the animal companion is larger than Medium). As a standard action, the
courtly hunter can touch her animal companion to transform it.

This ability replaces precise companion.

## Skill Bond (Ex) {#skill-bond}

At 3rd level, a courtly hunter's animal companion gains the courtly hunter's class skills as class
skills. Her animal companion can use the courtly hunter's skill ranks in a skill in place of its
own, but only to a maximum of the courtly hunter's hunter level (for instance, if a character had 3
levels in courtly hunter and 5 ranks in Diplomacy, her animal companion could either share 3 ranks
with skill bond or use its own ranks, whichever would result in a higher total skill bonus).

This ability replaces hunter tactics and the hunter's bonus teamwork feats.

## Alternate Form (Su) {#alternate-form}

At 7th level, the courtly hunter's animal companion learns an additional subtle form. When the
courtly hunter gains this ability, she chooses a Tiny animal. When under the effects of the subtle
companion ability, the courtly hunter's animal companion can change between a shrunken, more
innocuous version of its original shape or the shape of the chosen animal as a standard action. When
it transforms, it loses abilities dependent on its original shape and gains abilities from its new
shape as _[beast shape II](ref/spell/beast-shape-2)_. At 13th and 19th levels, the courtly hunter
can select an additional form to add to the animal companion's list of choices while it is in its
polymorphed form.

This ability replaces bonus tricks.
