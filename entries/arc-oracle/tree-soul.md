+++
id = "ref/arc-oracle/tree-soul"
kind = "archetype"
title = "Tree Soul"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Tree%20Soul"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tree_soul", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "69"

[fields]
kind = "archetype"
features = [
  { anchor = "tree-bound-curse", level = 1 },
  { anchor = "transform-wood", level = 1 },
  { anchor = "living-steel-dolls", level = 11 },
  { anchor = "tree-soul-revelation", level = 20 },
]
trades = [
  { replaces = "The class skills granted by the oracle's mystery and class skills", feature = "mystery", power = "class skills" },
  { replaces = "The oracle's mystery bonus spells at these levels", feature = "mystery", levels = [2, 10, 12, 14, 16, 18], power = "bonus spells" },
  { replaces = "Oracle's curse", feature = "oracle-s-curse", by = ["tree-bound-curse"] },
  { replaces = "Final revelation", feature = "final-revelation", by = ["tree-soul-revelation"] },
]
+++

Tree souls develop an affinity not just with trees but also with objects carved from them, feeling
the essence of the tree's spirit living within. By bonding to trees, they learn to manipulate the
trees' power to produce divine energy. The type of tree a tree soul oracle bonds to often seems to
influence the oracle's personality. A tree soul who is bound to a towering redwood may value
traditions and be slow to anger, while a tree soul bound to a smaller pine tree might be quick to
react and have a somewhat prickly personality. Regardless of the trees they form their metaphysical
attachment to, tree soul oracles tend to be steadfast and stubborn, having an aura of timelessness
even as the world changes around them.

## Class Skills {#class-skills}

A tree soul adds Acrobatics, Climb, Knowledge (nature), and Survival to her list of class skills.

This replaces the class skills granted by the oracle's mystery and class skills.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Tree souls are proficient with light and medium armor but are prohibited from wearing metal armor. A
tree soul can also wear wooden armor that has been altered by the _[ironwood](ref/spell/ironwood)_
spell so that it functions as though it were steel. Tree souls are proficient with shields (except
tower shields) but can use only those crafted from wood.

A tree soul who wears prohibited armor or uses a prohibited shield is unable to cast oracle spells
or use any of her supernatural or spell-like class abilities while doing so and for 24 hours
thereafter.

## Recommended Mysteries {#recommended-mysteries}

[Ancestor](ref/mystery/ancestor), [lore](ref/mystery/lore), [nature](ref/mystery/nature),
[wood](ref/mystery/wood).

## Bonus Spells {#bonus-spells}

_Warp wood_ (2nd), _tree stride_ (10th), _ironwood_ (12th), _changestaff_ (14th), _repel metal or
stone_ (16th), _greater siege of trees_ (18th). These bonus spells replace the oracle's mystery
bonus spells at these levels.

## Tree Bound Curse (Su) {#tree-bound-curse}

You bind your power to a specific tree. Any damage to the tree deals the same amount of damage to
you, overcoming DR, energy resistance, and immunities. Damage you take in this way cannot be healed
by normal or magical means until your bonded tree is healed or destroyed. The damage can reduce you
to 0 hit points but not below. If the tree is destroyed, you are considered to be
[staggered](ref/misc/staggered) and are unable to cast oracle spells or use supernatural or
spell-like class abilities until you bond with a new tree in a ceremony that takes 12 hours to
complete. Once per month, you can create a new bond with a different tree in a ceremony at that tree
that takes 12 hours to complete. You lose your bond with your previous tree in the process.

This replaces oracle's curse.

## Revelations {#revelations}

A tree soul oracle must take the following revelations at the listed levels.

## Transform Wood (Su) {#transform-wood}

At 1st level, as a standard action you can temporarily transform a number of 5-foot cubes of wood
each day equal to 1 + your Charisma modifier. The wood takes on the quality of
[darkwood](ref/eq-material/darkwood) for 1 minute per oracle level. At 11th level, you can have it
instead take on the quality of [living steel](ref/eq-material/living-steel) for the same duration.

## Living Steel Dolls (Ex) {#living-steel-dolls}

At 11th level, you add _[animate objects](ref/spell/animate-objects)_ to your list of spells known.
When you cast this spell on wooden objects, the objects' wooden parts immediately transform into
living steel. If the objects are destroyed or the duration ends, the wooden parts revert back to
their original material.

## Tree Soul Revelation (Su) {#tree-soul-revelation}

At 20th level, your skin takes on the appearance and properties of a tree trunk. This bark-like skin
grants you a +4 natural armor bonus to your Armor Class and DR 10/slashing. You also regrow any
severed limbs except your head within 24 hours as per _[regenerate](ref/spell/regenerate)_. Finally,
once a day as a standard action, you can assume the form of a [treant](ref/monster/treant), as per
_[plant shape III](ref/spell/plant-shape-3)_, for a number of minutes equal to 3 + your Charisma
modifier (minimum 1).

This replaces final revelation.
