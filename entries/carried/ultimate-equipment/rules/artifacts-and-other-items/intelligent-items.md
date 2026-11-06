+++
id = "ref/carried/ultimate-equipment/rules/artifacts-and-other-items/intelligent-items"
kind = "rule"
title = "Intelligent Items"
source_ids = ["ultimate-equipment"]
section = ["Rules", "Artifacts and Other Items"]
parent = "ref/carried/ultimate-equipment/rules/artifacts-and-other-items"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Equipment/Rules/Artifacts and Other Items/Intelligent Items", path = "ultimate_equipment/rules/artifacts_and_other_items.json" },
]

[fields]
kind = "none"
+++

Among the most miraculous of magic items are those that possess an intelligence of their own, those
wondrous treasures that step beyond the realm of mere tools to true allies. Magically imbued with
sentience, these items think and feel the same way characters do and warrant being treated like
NPCs. Intelligent items have extra abilities and sometimes extraordinary powers and special
purposes. Only permanent magic items (as opposed to single-use items or those with charges) can be
intelligent. (This means that potions, scrolls, and wands, among other items, are never
intelligent.) In general, less than 1% of magic items have intelligence.

Intelligent items can actually be considered creatures because they have Intelligence, Wisdom, and
Charisma scores and should be treated as constructs. They often have the ability to illuminate their
surroundings at will (as magic weapons do), and many cannot see otherwise.

Unlike most magic items, intelligent items can activate their own powers without waiting for a
command word from their owner. Intelligent items act during their owner's turn in the initiative
order.

## Designing an Intelligent Item {#designing-an-intelligent-item}

All intelligent magic items possess similar properties. All must have an alignment, mental ability
scores, languages, senses, and at least one other special ability. These statistics and abilities
can be improved during creation, increasing the item's overall cost. Many of these abilities add to
an item's Ego score. Intelligent items with high Ego scores are difficult to control and can
sometimes take control of their owners, making them dangerous to possess.

An intelligent magic item has a base price increase of 500 gp. When determining the total value of
an intelligent item, add this value to the sum of all its additional abilities's prices before
adding them to the magic item's base price.

## Intelligent Item Alignment {#intelligent-item-alignment}

Any item with intelligence has an alignment. Note that intelligent weapons already have alignments,
either stated or by implication. If you're generating a random intelligent weapon, that weapon's
alignment must fit with any alignment-oriented special abilities it has.

Any character whose alignment does not correspond to that of the item (except as noted by the
asterisks on the table below) gains one negative level if he so much as picks up the item. Although
this negative level never results in actual level loss, it remains as long as the item is in hand
and cannot be overcome in any way (including by restoration spells). this negative level is
cumulative with any other penalties the item might place on inappropriate wielders. items with ego
scores of 20 to 29 bestow two negative levels. items with ego scores of 30 or higher bestow three
negative levels.

### Intelligent Item Alignment {#intelligent-item-alignment-2}

::: table
caption = "Intelligent Item Alignment"
head = [
  [
    { text = "d%", header = true },
    { text = "Alignment of Item", header = true },
  ],
]
body = [
  [
    { text = "01–10" },
    { text = "Chaotic good" },
  ],
  [
    { text = "11–20" },
    { text = "Chaotic neutral\\*" },
  ],
  [
    { text = "21–35" },
    { text = "Chaotic evil" },
  ],
  [
    { text = "36–45" },
    { text = "Neutral evil\\*" },
  ],
  [
    { text = "46–55" },
    { text = "Lawful evil" },
  ],
  [
    { text = "56–70" },
    { text = "Lawful good" },
  ],
  [
    { text = "71–80" },
    { text = "Lawful neutral\\*" },
  ],
  [
    { text = "81–90" },
    { text = "Neutral good\\*" },
  ],
  [
    { text = "91–100" },
    { text = "Neutral" },
  ],
]
foot = [
  [
    { text = "\\* The item can also be used by any character whose alignment corresponds to the non-neutral portion of the item's alignment.", colspan = 2 },
  ],
]
:::

## Intelligent Item Ability Scores {#intelligent-item-ability-scores}

Intelligent magic items possess all three mental ability scores: Intelligence, Wisdom, and Charisma.
Each one of these ability scores begins at a value of 10, but can be increased to as high as 20. The
table below shows the cost to increase one of the item's ability scores. This cost must be paid for
each ability score raised above 10. For example, an intelligent magic item with a Intelligence 15,
Wisdom 12, and Charisma 10 would cost at least 2,400 gp more than the base item (including the 500
gp for being an intelligent item).

### Intelligent Item Ability Scores {#intelligent-item-ability-scores-2}

::: table
caption = "Intelligent Item Ability Scores"
head = [
  [
    { text = "Score", header = true },
    { text = "Base Price Modifier", header = true },
    { text = "Ego Modifier", header = true },
  ],
]
body = [
  [
    { text = "10" },
    { text = "—" },
    { text = "—" },
  ],
  [
    { text = "11" },
    { text = "+200 gp" },
    { text = "—" },
  ],
  [
    { text = "12" },
    { text = "+500 gp" },
    { text = "+1" },
  ],
  [
    { text = "13" },
    { text = "+700 gp" },
    { text = "+1" },
  ],
  [
    { text = "14" },
    { text = "+1,000 gp" },
    { text = "+2" },
  ],
  [
    { text = "15" },
    { text = "+1,400 gp" },
    { text = "+2" },
  ],
  [
    { text = "16" },
    { text = "+2,000 gp" },
    { text = "+3" },
  ],
  [
    { text = "17" },
    { text = "+2,800 gp" },
    { text = "+3" },
  ],
  [
    { text = "18" },
    { text = "+4,000 gp" },
    { text = "+4" },
  ],
  [
    { text = "19" },
    { text = "+5,200 gp" },
    { text = "+4" },
  ],
  [
    { text = "20" },
    { text = "+8,000 gp" },
    { text = "+5" },
  ],
]
:::

## Languages Spoken by Item {#languages-spoken-by-item}

Like a character, an intelligent item understands Common plus one additional language per point of
Intelligence bonus. Choose appropriate languages, taking into account the item's origin and
purposes. If the item does not possess speech, it can still read and understand the languages it
knows.

## Senses and Communication {#senses-and-communication}

Every intelligent magic item begins with the ability to see and hear within 30 feet, as well as the
ability to communicate emphatically with its owner. Empathy only allows the item to encourage or
discourage certain actions through urges and emotions. Additional forms of communication and better
senses increase the item's cost and Ego score.

### Empathy {#empathy}

::: statblock
Ability Type: Supernatural
:::

Empathy allows the item to encourage or discourage certain actions by communicating emotions and
urges. It does not allow for verbal communication.

### Speech {#speech}

::: statblock
Ability Type: Supernatural
:::

An intelligent item with this ability can speak out loud using any of the languages it knows.

### Telepathy {#telepathy}

::: statblock
Ability Type: Supernatural
:::

Telepathy allows an intelligent item to hold private mental conversations with its wielder,
regardless of their known languages. The wielder must be touching the item to communicate in this
way.

### Senses {#senses}

Senses allow an intelligent magic item to see and hear out to the listed distance. Adding
[darkvision](ref/rule/darkvision) or [blindsense](ref/rule/blindsight-and-blindsense) grants the use
of those senses at the same range.

### Read Languages {#read-languages}

::: statblock
Ability Type: Extraordinary
:::

The item can read script in any language, regardless of its known languages.

### Read Magic {#read-magic}

::: statblock
Ability Type: Spell-Like
:::

An intelligent magic item with this ability can read magical writings and scrolls as if through
_[read magic](ref/spell/read-magic). _This ability does not allow the magic item to activate scrolls
or other items. An intelligent magic item can suppress and resume this ability as a free action.

#### Intelligent Item Senses and Communication {#intelligent-item-senses-and-communication}

::: table
caption = "Intelligent Item Senses and Communication"
head = [
  [
    { text = "Ability", header = true },
    { text = "Base Price Modifier", header = true },
    { text = "Ego Modifier", header = true },
  ],
]
body = [
  [
    { text = "Empathy" },
    { text = "—" },
    { text = "—" },
  ],
  [
    { text = "Speech" },
    { text = "+500 gp" },
    { text = "—" },
  ],
  [
    { text = "Telepathy" },
    { text = "+1,000 gp" },
    { text = "+1" },
  ],
  [
    { text = "Senses (30 ft.)" },
    { text = "—" },
    { text = "—" },
  ],
  [
    { text = "Senses (60 ft.)" },
    { text = "+500 gp" },
    { text = "—" },
  ],
  [
    { text = "Senses (120 ft.)" },
    { text = "+1,000 gp" },
    { text = "—" },
  ],
  [
    { text = "[Darkvision](ref/rule/darkvision)" },
    { text = "+500 gp" },
    { text = "—" },
  ],
  [
    { text = "[Blindsense](ref/rule/blindsight-and-blindsense)" },
    { text = "+5,000 gp" },
    { text = "+1" },
  ],
  [
    { text = "Read languages" },
    { text = "+1,000 gp" },
    { text = "+1" },
  ],
  [
    { text = "_[Read magic](ref/spell/read-magic)_" },
    { text = "+2,000 gp" },
    { text = "+1" },
  ],
]
:::

## Intelligent Item Powers {#intelligent-item-powers}

Each intelligent item should possess at least one power, although some might possess a host of
powers. To find the item's specific powers, roll on or choose from the table below. All powers
function at the direction of the item, though intelligent items generally follow the wishes of their
owner. Activating a power or concentrating on an active one is a standard action for the item. The
caster level for these effects is equal to the item's caster level. Save DCs are based on the item's
highest mental ability score.

### Intelligent Item Powers {#intelligent-item-powers-2}

::: table
caption = "Intelligent Item Powers"
head = [
  [
    { text = "d%", header = true },
    { text = "Item Power", header = true },
    { text = "Base Price Modifer", header = true },
    { text = "Ego Modifier", header = true },
  ],
]
body = [
  [
    { text = "01–10" },
    { text = "Item can cast a 0-level spell at will" },
    { text = "+1,000 gp" },
    { text = "+1" },
  ],
  [
    { text = "11–20" },
    { text = "Item can cast a 1st-level spell 3/day" },
    { text = "+1,200 gp" },
    { text = "+1" },
  ],
  [
    { text = "21–25" },
    { text = "Item can use _[magic aura](ref/spell/magic-aura) _on itself at will" },
    { text = "+2,000 gp" },
    { text = "+1" },
  ],
  [
    { text = "26–35" },
    { text = "Item can cast a 2nd-level spell 1/day" },
    { text = "+2,400 gp" },
    { text = "+1" },
  ],
  [
    { text = "36–45" },
    { text = "Item has 5 ranks in one skill\\*" },
    { text = "+2,500 gp" },
    { text = "+1" },
  ],
  [
    { text = "46–50" },
    { text = "Item can sprout limbs and move with a speed of 10 feet" },
    { text = "+5,000 gp" },
    { text = "+1" },
  ],
  [
    { text = "51–55" },
    { text = "Item can cast a 3rd-level spell 1/day" },
    { text = "+6,000 gp" },
    { text = "+1" },
  ],
  [
    { text = "56–60" },
    { text = "Item can cast a 2nd-level spell 3/day" },
    { text = "+7,200 gp" },
    { text = "+1" },
  ],
  [
    { text = "61–70" },
    { text = "Item has 10 ranks in one skill\\*" },
    { text = "+10,000 gp" },
    { text = "+2" },
  ],
  [
    { text = "71–75" },
    { text = "Item can change shape into one other form of the same size" },
    { text = "+10,000 gp" },
    { text = "+2" },
  ],
  [
    { text = "76–80" },
    { text = "Item can_ [fly](ref/spell/fly), _as the spell, at a speed of 30 feet" },
    { text = "+10,000 gp" },
    { text = "+2" },
  ],
  [
    { text = "81–85" },
    { text = "Item can cast a 4th-level spell 1/day" },
    { text = "+11,200 gp" },
    { text = "+2" },
  ],
  [
    { text = "86–90" },
    { text = "Item can _[teleport](ref/spell/teleport)_ itself 1/day" },
    { text = "+15,000 gp" },
    { text = "+2" },
  ],
  [
    { text = "91–95" },
    { text = "Item can cast a 3rd-level spell 3/day" },
    { text = "+18,000 gp" },
    { text = "+2" },
  ],
  [
    { text = "96–100" },
    { text = "Item can cast a 4th-level spell 3/day" },
    { text = "+33,600 gp" },
    { text = "+2" },
  ],
]
foot = [
  [
    { text = "\\* Intelligent items can only possess Intelligence-, Wisdom-, or Charisma-based skills, unless they also possess some form of ability to move.", colspan = 4 },
  ],
]
:::

## Special Purpose Items {#special-purpose-items}

Some intelligent items have special purposes that guide their actions. Intelligent magic items with
a special purpose gain a +2 Ego bonus. An item's purpose must suit the type and alignment of the
item. A magic item with a purpose should be treated as an individual with a goal, not a fanatical
parody. For example, a purpose of "defeat/slay arcane spellcasters" doesn't mean that an intelligent
sword forces the wielder to kill every wizard she sees. Nor does it mean that the sword believes it
is possible to kill every wizard, sorcerer, and bard in the world. It does mean that the item hates
arcane spellcasters and wants to bring an end to the rule of a sorcerer-queen in a nearby land.
Likewise, a purpose of "defend elves" doesn't mean that if the wielder is an elf, he only wants to
help the wielder. It means that the item wants to be used in furthering the cause of elves, stamping
out their enemies and aiding their leaders. A purpose of "defeat/slay all" isn't just a matter of
self-preservation. It means that the item won't rest (or let its wielder rest) until it places
itself above all others.

The table below has a number of sample purposes that a magic item might possess. If the wielder
specifically ignores or goes against an intelligent item's special purpose, the item gains a +4
bonus to its Ego until the wielder cooperates. This is in addition to the +2 Ego bonus gained by
items with a special purpose.

### Intelligent Item Purpose {#intelligent-item-purpose}

::: table
caption = "Intelligent Item Purpose"
head = [
  [
    { text = "d%", header = true },
    { text = "Purpose", header = true },
    { text = "Ego Modifier", header = true },
  ],
]
body = [
  [
    { text = "01–20" },
    { text = "Defeat/slay diametrically opposed alignment\\*" },
    { text = "+2" },
  ],
  [
    { text = "21–30" },
    { text = "Defeat/slay arcane spellcasters (including spellcasting monsters and those that use [spell-like abilities](ref/umr/spell-like-abilities))" },
    { text = "+2" },
  ],
  [
    { text = "31–40" },
    { text = "Defeat/slay divine spellcasters (including divine entities and servitors)" },
    { text = "+2" },
  ],
  [
    { text = "41–50" },
    { text = "Defeat/slay nonspellcasters" },
    { text = "+2" },
  ],
  [
    { text = "51–55" },
    { text = "Defeat/slay a particular creature type (see the _[bane](ref/spell/bane)_ special ability for choices)" },
    { text = "+2" },
  ],
  [
    { text = "56–60" },
    { text = "Defeat/slay a particular race or kind of creature" },
    { text = "+2" },
  ],
  [
    { text = "61–70" },
    { text = "Defend a particular race or kind of creature" },
    { text = "+2" },
  ],
  [
    { text = "71–80" },
    { text = "Defeat/slay the servants of a specific deity" },
    { text = "+2" },
  ],
  [
    { text = "81–90" },
    { text = "Defend the servants and interests of a specific deity" },
    { text = "+2" },
  ],
  [
    { text = "91–95" },
    { text = "Defeat/slay all (other than the item and the wielder)" },
    { text = "+2" },
  ],
  [
    { text = "96–100" },
    { text = "Choose one" },
    { text = "+2" },
  ],
]
foot = [
  [
    { text = "\\* The purpose of the neutral (N) version of this item is to preserve the balance by defeating/slaying powerful beings of the extreme alignments (LG, LE, CG, CE).", colspan = 3 },
  ],
]
:::

## Dedicated Powers {#dedicated-powers}

A dedicated power operates only when an intelligent item is in pursuit of its special purpose. This
determination is always made by the item. Unlike its other powers, an intelligent item can refuse to
use its dedicated powers even if the owner is dominant (see Items Against Characters). The caster
level for these effects is equal to the item's caster level. Save DCs are based on the item's
highest mental ability score.

### Special Purpose Item Dedicated Powers {#special-purpose-item-dedicated-powers}

::: table
caption = "Special Purpose Item Dedicated Powers"
head = [
  [
    { text = "d%", header = true },
    { text = "Dedicated Power", header = true },
    { text = "Base Price Modifier", header = true },
    { text = "Ego Modifier", header = true },
  ],
]
body = [
  [
    { text = "01–20" },
    { text = "Item can detect any special purpose foes within 60 feet" },
    { text = "+10,000 gp" },
    { text = "+1" },
  ],
  [
    { text = "21–35" },
    { text = "Item can use a 4th-level spell at will" },
    { text = "+56,000 gp" },
    { text = "+2" },
  ],
  [
    { text = "36–50" },
    { text = "Wielder gets +2 luck bonus on attacks, saves, and checks" },
    { text = "+80,000 gp" },
    { text = "+2" },
  ],
  [
    { text = "51–65" },
    { text = "Item can use a 5th-level spell at will" },
    { text = "+90,000 gp" },
    { text = "+2" },
  ],
  [
    { text = "66–80" },
    { text = "Item can use a 6th-level spell at will" },
    { text = "+132,000 gp" },
    { text = "+2" },
  ],
  [
    { text = "81–95" },
    { text = "Item can use a 7th-level spell at will" },
    { text = "+182,000 gp" },
    { text = "+2" },
  ],
  [
    { text = "96–100" },
    { text = "Item can use _[true resurrection](ref/spell/true-resurrection)_ on wielder, once per month" },
    { text = "+200,000 gp" },
    { text = "+2" },
  ],
]
:::

## Item Ego {#item-ego}

Ego is a measure of the total power and force of personality that an item possesses. An item's Ego
score is the sum of all of its Ego modifiers plus an additional bonus for the cost of the base magic
item (excluding the cost of all of the intelligent item enhancements). An item's Ego score helps
determine whether the item or the character is dominant in their relationship, as detailed below.

### Ego Modifier by Base Value {#ego-modifier-by-base-value}

::: table
caption = "Ego Modifier by Base Value"
head = [
  [
    { text = "Base Magic Item Value", header = true },
    { text = "Ego Modifier", header = true },
  ],
]
body = [
  [
    { text = "Up to 1,000 gp" },
    { text = "—" },
  ],
  [
    { text = "1,001 gp to 5,000 gp" },
    { text = "+1" },
  ],
  [
    { text = "5,001 gp to 10,000 gp" },
    { text = "+2" },
  ],
  [
    { text = "10,001 gp to 20,000 gp" },
    { text = "+3" },
  ],
  [
    { text = "20,001 gp to 50,000 gp" },
    { text = "+4" },
  ],
  [
    { text = "50,001 gp to 100,000 gp" },
    { text = "+6" },
  ],
  [
    { text = "100,001 gp to 200,000 gp" },
    { text = "+8" },
  ],
  [
    { text = "200,001 gp and higher" },
    { text = "+12" },
  ],
]
:::

## Items against Characters {#items-against-characters}

When an item has an Ego of its own, it has a will of its own. The item is absolutely true to its
alignment. If the character who possesses the item is not true to that alignment's goals or the
item's special purpose, a personality conflict results—item against character. Similarly, any item
with an Ego score of 20 or higher always considers itself superior to any character, and a
personality conflict results if the possessor does not always agree with the item.

When a personality conflict occurs, the possessor must make a Will saving throw (DC = the item's
Ego). If the possessor succeeds, she is dominant. If she fails, the item is dominant. Dominance
lasts for 1 day or until a critical situation occurs (such as a major battle, a serious threat to
either the item or the character, and so on, as determined by the GM). Should an item gain
dominance, it resists the character's desires and demands concessions such as any of the following:

- Removal of associates or items whose alignment or personality is distasteful to the item.
- The character divesting herself of all other magic items or items of a certain type.
- Obedience from the character so the item can direct where they go for its own purposes.
- Immediate seeking out and slaying of creatures hateful to the item.
- Magical protections and devices to safeguard the item from molestation when it is not in use.
- That the character carry the item with her on all occasions.
- That the character relinquish the item to a more suitable possessor due to alignment differences
  or conduct.

In extreme circumstances, the item can resort to even harsher measures, such as the following:

- Force its possessor into combat.
- Refuse to strike opponents.
- Strike at its wielder or her associates.
- Force its possessor to surrender to an opponent.
- Cause itself to drop from the character's grasp.

Naturally, such actions are unlikely when harmony reigns between the character's and item's
alignments or when their purposes and personalities are well matched. Even so, an item might wish to
have a lesser character possess it in order to easily establish and maintain dominance over him, or
a higher-level possessor so as to better accomplish its goals.

All magic items with personalities desire to play an important role in whatever activity is under
way, particularly combat. Such items are natural rivals, even with others of the same alignment. No
intelligent item wants to share its wielder with other intelligent magic items. An intelligent item
is aware of the presence of any other intelligent item within 60 feet, and such an intelligent item
usually tries its best to mislead or distract its host so that she ignores or destroys the rival. Of
course, alignment might change this sort of behavior.

Items with personalities are never totally controlled or silenced by the characters that possess
them, even though they might never successfully control their possessors. They might be powerless to
force their demands, but most remain undaunted and continue to air their wishes and preferences.

### Intelligent Item Personality Quirks {#intelligent-item-personality-quirks}

Many intelligent items have personalities as quirky and robust as any other NPC. Roll on the
following table to determine one or more personality quirks for intelligent items.

::: table
caption = "Intelligent Item Personality Quirks"
head = [
  [
    { text = "d%", header = true },
    { text = "Personality Trait", header = true },
  ],
]
body = [
  [
    { text = "01" },
    { text = "Always agrees with people, but changes its mind quickly" },
  ],
  [
    { text = "02" },
    { text = "Is very noisy about treasure" },
  ],
  [
    { text = "03" },
    { text = "Act mysteriously and answers questions poetically" },
  ],
  [
    { text = "04" },
    { text = "Doesn't like new people" },
  ],
  [
    { text = "05" },
    { text = "Makes token bets about minor things" },
  ],
  [
    { text = "06" },
    { text = "Refers to itself in the third person" },
  ],
  [
    { text = "07" },
    { text = "Bargains for the use of some of its powers" },
  ],
  [
    { text = "08" },
    { text = "Constantly asks how things taste and smell" },
  ],
  [
    { text = "09" },
    { text = "Yells when it is excited" },
  ],
  [
    { text = "10" },
    { text = "Know-it-all" },
  ],
  [
    { text = "11" },
    { text = "Is polite but obviously insincere" },
  ],
  [
    { text = "12" },
    { text = "Constantly apologizes as a verbal tic" },
  ],
  [
    { text = "13" },
    { text = "Makes a lot of threats it cannot back up" },
  ],
  [
    { text = "14" },
    { text = "Very mellow; advises people to take a philosophical approach to both success and failure" },
  ],
  [
    { text = "15" },
    { text = "Says as little as possible" },
  ],
  [
    { text = "16" },
    { text = "Snickers or laughs at the misfortunes of others" },
  ],
  [
    { text = "17" },
    { text = "Calls people by the wrong name, though often consistently" },
  ],
  [
    { text = "18" },
    { text = "Prays a lot" },
  ],
  [
    { text = "19" },
    { text = "Is quick to praise people even for little things" },
  ],
  [
    { text = "20" },
    { text = "Often appears surprised and slightly offended when spoken to" },
  ],
  [
    { text = "21" },
    { text = "Does not like to make decisions" },
  ],
  [
    { text = "22" },
    { text = "Has a list of numbered rules or maxims covering different situations and quotes them when appropriate" },
  ],
  [
    { text = "23" },
    { text = "Tells people the \"real\" reason they are doing things" },
  ],
  [
    { text = "24" },
    { text = "Asks for advice or opinions about very unlikely situations" },
  ],
  [
    { text = "25" },
    { text = "Speaks with great formality; never uses contractions and employs bigger words than necessary" },
  ],
  [
    { text = "26" },
    { text = "Easily distracted by minor events in the area" },
  ],
  [
    { text = "27" },
    { text = "Usually needs someone to explain a joke or metaphor" },
  ],
  [
    { text = "28" },
    { text = "Has a particular core belief, potentially a rather odd one, and steadfastly looks at everything through the lens of that opinion" },
  ],
  [
    { text = "29" },
    { text = "Likes to count things and has fun with numbers" },
  ],
  [
    { text = "30" },
    { text = "Always tries to find compromise" },
  ],
  [
    { text = "31" },
    { text = "Is always talking to itself" },
  ],
  [
    { text = "32" },
    { text = "Very bad liar" },
  ],
  [
    { text = "33" },
    { text = "Asks rude questions without realizing they cause offense" },
  ],
  [
    { text = "34" },
    { text = "Grumbles and complains about its form and plight" },
  ],
  [
    { text = "35" },
    { text = "Very sensitive about criticism or conflict" },
  ],
  [
    { text = "36" },
    { text = "Absent-minded" },
  ],
  [
    { text = "37" },
    { text = "Blames a particular type of creature for its troubles" },
  ],
  [
    { text = "38" },
    { text = "Intellectual bully" },
  ],
  [
    { text = "39" },
    { text = "Makes allusions to events from history or mythology without bothering to explain them" },
  ],
  [
    { text = "40" },
    { text = "Hates a particular terrain type and complains loudly while within that terrain" },
  ],
  [
    { text = "41" },
    { text = "Constantly ask questions about things that are outside its vision" },
  ],
  [
    { text = "42" },
    { text = "Makes a list of things for its wearer or wielder to accomplish each day" },
  ],
  [
    { text = "43" },
    { text = "Cannot keep a secret" },
  ],
  [
    { text = "44" },
    { text = "Seems slightly surprised when anyone else has a good idea or does something productive" },
  ],
  [
    { text = "45" },
    { text = "Often whines" },
  ],
  [
    { text = "46" },
    { text = "Easily angered" },
  ],
  [
    { text = "47" },
    { text = "Constantly warns about the danger of disease" },
  ],
  [
    { text = "48" },
    { text = "Has a stock phrase" },
  ],
  [
    { text = "49" },
    { text = "Habitually mumbles a word that rhymes with the final word other people speak before they pause" },
  ],
  [
    { text = "50" },
    { text = "Delighted by puns and other sorts of word games" },
  ],
  [
    { text = "51" },
    { text = "Makes animal noises when feeling threatened or excited" },
  ],
  [
    { text = "52" },
    { text = "A lover or literature and poetry, it takes any opportunity to spout of a line or two of prose or verse" },
  ],
  [
    { text = "53" },
    { text = "Very superstitious" },
  ],
  [
    { text = "54" },
    { text = "Spurs on its wielder or wearer to brave or foolhardy acts" },
  ],
  [
    { text = "55" },
    { text = "Never uses one word when 10 will do" },
  ],
  [
    { text = "56" },
    { text = "Constantly asks to be destroyed, but panics if taken seriously" },
  ],
  [
    { text = "57" },
    { text = "Always has a reason why something will not work" },
  ],
  [
    { text = "58" },
    { text = "Claims to be in love with the bearer" },
  ],
  [
    { text = "59" },
    { text = "Tells boring stories about something mundane" },
  ],
  [
    { text = "60" },
    { text = "Constantly suggests ways to make activities more \"fun\" and \"exciting\"" },
  ],
  [
    { text = "61" },
    { text = "Collects words from languages it doesn't know, and uses them in place of words in the language it most commonly uses" },
  ],
  [
    { text = "62" },
    { text = "Dotes on its wearer or wielder" },
  ],
  [
    { text = "63" },
    { text = "Often ignores its wearer or wielder" },
  ],
  [
    { text = "64" },
    { text = "Loathes itself" },
  ],
  [
    { text = "65" },
    { text = "Occasionally chants annoying little rhymes" },
  ],
  [
    { text = "66" },
    { text = "Acts as if it is friends with, but obviously hates, its wearer or wielder" },
  ],
  [
    { text = "67" },
    { text = "Openly scornful of organized religion and believes all gods are selfish liars" },
  ],
  [
    { text = "68" },
    { text = "Gets angrier and more determined with each setback" },
  ],
  [
    { text = "69" },
    { text = "Thinks most objects are intelligent items" },
  ],
  [
    { text = "70" },
    { text = "Lacks a moral compass when making plans and often proposes horrific solutions to minor problems" },
  ],
  [
    { text = "71" },
    { text = "Falls quiet for stretches where it will not talk to anyone for days" },
  ],
  [
    { text = "72" },
    { text = "Believes it is losing its mind" },
  ],
  [
    { text = "73" },
    { text = "Constantly name-drops a famous past bearer" },
  ],
  [
    { text = "74" },
    { text = "Has terrible syntax and diction" },
  ],
  [
    { text = "75" },
    { text = "Never tires of learning new and interesting bits of information" },
  ],
  [
    { text = "76" },
    { text = "Complains about smells that no one else notices" },
  ],
  [
    { text = "77" },
    { text = "Wants to be dipped in ale, wine, or other forms of alcohol, and when it is, acts drunk" },
  ],
  [
    { text = "78" },
    { text = "Loves to sing but is tone deaf" },
  ],
  [
    { text = "79" },
    { text = "Blames everyone else for its plight" },
  ],
  [
    { text = "80" },
    { text = "Is a seemingly endless font of gossip—though most details are fabricated" },
  ],
  [
    { text = "81" },
    { text = "Treats all others as lesser forms of intelligence" },
  ],
  [
    { text = "82" },
    { text = "Very cheerful; tries to raise downcast spirits with song, jokes, and uplifting stories" },
  ],
  [
    { text = "83" },
    { text = "Grows more and more relaxed the worse things get; conversely, on edge and nervous when things seem to go well" },
  ],
  [
    { text = "84" },
    { text = "Constantly remembers details wrong" },
  ],
  [
    { text = "85" },
    { text = "Makes up stories" },
  ],
  [
    { text = "86" },
    { text = "Avoids speaking with creatures other than its wielder or wearer" },
  ],
  [
    { text = "87" },
    { text = "Has a need for constant attention" },
  ],
  [
    { text = "88" },
    { text = "Is a little unhinged when away from its wielder or wearer" },
  ],
  [
    { text = "89" },
    { text = "Questions others about their background in order to determine if they are \"suitable\"" },
  ],
  [
    { text = "90" },
    { text = "Is often confused by the deeds of others and regularly asks about the reason for certain actions" },
  ],
  [
    { text = "91" },
    { text = "Very jealous and possessive about its wielder or wearer" },
  ],
  [
    { text = "92" },
    { text = "Continually mentions a heroic battle it participated in and how nothing else compares" },
  ],
  [
    { text = "93" },
    { text = "Diagnoses everyone with a mania, fixation, or curse, but is often wrong" },
  ],
  [
    { text = "94" },
    { text = "Explains simple things that don't need explanations" },
  ],
  [
    { text = "95" },
    { text = "Wishes it was free from its item and seeks someone who can perform such a task" },
  ],
  [
    { text = "96" },
    { text = "Believe it is a trapped god" },
  ],
  [
    { text = "97" },
    { text = "Has an imaginary ethereal friend" },
  ],
  [
    { text = "98" },
    { text = "Is afraid of the dark" },
  ],
  [
    { text = "99" },
    { text = "Admonishes people for using profanity" },
  ],
  [
    { text = "100" },
    { text = "Rarely talks but frequently emits a drone of insane giggles" },
  ],
]
:::

## Specific Intelligent Items {#specific-intelligent-items}

The following are examples of specific intelligent items that can be crafted or found in treasure
hoards.

::: entry-link
target = "ref/magic-armor/armor-of-the-shadow-lord"
title = "Armor of the Shadow Lord"
:::

::: entry-link
target = "ref/magic-wondrous/chomper"
title = "Chomper"
:::

::: entry-link
target = "ref/magic-weapon/hammer-of-enemies"
title = "Hammer of Enemies"
:::

::: entry-link
target = "ref/magic-rod/harbinger-rod"
title = "harbinger rod"
:::

::: entry-link
target = "ref/magic-wondrous/headband-of-the-sage"
title = "Headband of the sage"
:::

::: entry-link
target = "ref/magic-wondrous/helmet-of-the-golden-general"
title = "Helmet of the Golden General"
:::

::: entry-link
target = "ref/magic-weapon/lightning-bow"
title = "Lightning Bow"
:::

::: entry-link
target = "ref/magic-wondrous/lute-of-discord"
title = "Lute of Discord"
:::

::: entry-link
target = "ref/magic-rod/metamagicians-apprentice"
title = "metamagician's apprentice"
:::

::: entry-link
target = "ref/magic-ring/obsession-ring"
title = "Obsession Ring"
:::

::: entry-link
target = "ref/magic-rod/rod-that-should-not-be-lesser"
title = "Rod that Should Not Be (Lesser)"
:::

::: entry-link
target = "ref/magic-rod/rod-that-should-not-be-greater"
title = "Rod that Should Not Be (Greater)"
:::

::: entry-link
target = "ref/magic-armor/shield-of-the-mage"
title = "Shield of the Mage"
:::

::: entry-link
target = "ref/magic-weapon/singing-sword"
title = "Singing Sword"
:::
