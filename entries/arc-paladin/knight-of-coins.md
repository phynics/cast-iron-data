+++
id = "ref/arc-paladin/knight-of-coins"
kind = "archetype"
title = "Knight of Coins"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Knight%20of%20Coins"
source_ids = ["merchants-manifest"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "knight_of_coins", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "merchants-manifest"
page = "28"

[fields]
kind = "archetype"
features = [
  { anchor = "eye-for-forgeries", level = 1 },
  { anchor = "blessing-of-prosperity", level = 3 },
]
trades = [
  { replaces = "Detect evil", feature = "detect-evil", by = ["eye-for-forgeries"] },
  { replaces = "The mercies gained at 3rd, 9th, and 15th levels", feature = "mercy", levels = [3, 9, 15], by = ["blessing-of-prosperity"] },
  { alters = "Skill ranks per level" },
  { alters = "Class skills" },
]
+++

Servants of gods who revere wealth, knights of coins promote fair trade and stable commerce between
cities and between nations. Many of these knights are Abadarans, and some have also taken the sacred
shield archetype (_Pathfinder RPG Ultimate Combat_ 65). Regardless, knights of coins know that a
prosperous city can uplift and enrich more people than pious prayers alone.

## Class Skills {#class-skills}

A knight of coins adds Appraise, Knowledge (local), Perception, and Use Magic Device to her list of
class skills. She gains a number of skill ranks equal to 4 + her Intelligence modifier at each
level, instead of a number of skill ranks equal to 2 + her Intelligence modifier.

This alters the paladin's class skills and skill ranks per level.

## Eye for Forgeries (Sp) {#eye-for-forgeries}

At will, a knight of coins can concentrate on a single item within 30 feet as a move action. When
she does, the knight of coins can detect if it is magical, as per the spell
_[detect magic](ref/spell/detect-magic)_. The knight of coins cannot concentrate on more than one
item in this way at a time.

This replaces _detect evil_.

## Blessing of Prosperity (Su) {#blessing-of-prosperity}

A knight of coins is a patron of wealth and seeks to even the playing field for those who have
unfair economic disadvantages. At 3rd level and every 6 levels thereafter, the paladin can select a
blessing (see Blessings below). By expending a use of lay on hands, the knight of coins can instead
grant a boon to herself or a creature touched as a standard action. These boons do not stack with
themselves or with blessings from another knight of coins. A blessing of prosperity lasts up to 1
hour, though the knight of coins who bestowed it can end a blessing's benefits early (whether it
affects her or another creature) as a free action. Using this ability requires only one free hand
and is a standard action, unless the knight of coins targets herself, in which case it is a swift
action.

If she knows multiple blessings of prosperity, the knight of coins can bestow multiple blessings on
a single target as part of the action and the expenditure of a use of lay on hands required to use
this ability. If she bestows multiple different blessings, these blessings are cumulative. For
example, a 9th-level knight of coins' blessing of prosperity ability might grant a +4 sacred bonus
on Appraise and Sense Motive checks as well as a +4 sacred bonus on Perception checks and to CMD
against [disarm](ref/rule/disarm) and [steal](ref/rule/steal) combat maneuvers.

A knight of coins who takes the [Extra Mercy](ref/feat/extra-mercy) feat can gain an extra blessing
of prosperity instead of an extra mercy. Once a blessing of prosperity is chosen, it can't be
changed. A character who has benefited from a blessing of prosperity cannot benefit from that same
blessing again (whether bestowed by the same knight of coins or another knight of coins) for 24
hours.

_Blessings:_ The following blessings are available to a knight of coins.

- The target adds an extra 10% to the gp value gained when selling off treasure (normally 50% of the
  item's original value). This blessing cannot result in selling treasure for more than 100% of its
  original value.
- The target gains a +4 sacred bonus on Appraise and Sense Motive checks.
- The target gains a +4 sacred bonus on Perception checks and to CMD against disarm and steal combat
  maneuvers.
- The target gains a +4 sacred bonus on Craft, Perform, and Profession checks.
- The target can use _[locate object](ref/spell/locate-object)_ as a
  [spell-like ability](ref/umr/spell-like-abilities) once, using the knight of coins' class level as
  the caster level.
- The target can treat one [settlement](ref/rule/settlements-in-play) as having its base value and
  purchase limit increased by 30%. The target must choose the affected settlement when the knight of
  coins bestows this blessing.
- The target can treat one settlement as being one size category larger for the purposes of
  determining available magic items. The target must choose the affected settlement when the knight
  of coins bestows this blessing.

This replaces the mercies gained at 3rd, 9th, and 15th levels.
