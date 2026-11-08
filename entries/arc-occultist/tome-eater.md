+++
id = "ref/arc-occultist/tome-eater"
kind = "archetype"
title = "Tome Eater"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tome_eater", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]

[fields]
kind = "archetype"
replaces = ["Shift focus, 6th-level implement", "magic circles", "outside contact", "binding circles", "fast circles", "Aura sight"]
alters = ["Implements", "mental focus", "spellcasting", "implement mastery"]
+++

**Sources:** Occult Adventures pg 102\
Tome eaters have learned how to tap into the latent psychic energy of the written word by physically
devouring books and scrolls to create magical effects and gain mystical insights. They use their
bonded tomes to gain access to all sorts of magic, and as they grow in power, they gain an innate
sense of the books and writings around them.

**Bonded Tome (Su)**

**Ability:** As part of casting an occultist spell, a tome eater can expend 1 point of mental focus
tied to the appropriate school to increase the spell's caster level by 1 or increase the spell's DC
by 1.

**Alters:** Implements, mental focus, spellcasting, implement mastery

**Info:** A tome eater forms a supernatural bond with a specific book. She can replace her bonded
tome with another book at any time, though the tome eater must perform a 24-hour binding ritual to
attune herself to the new book.

**Gained:** At 1st Level

**Special:** The bonded tome starts as an implement for any two schools of magic at 1st level, and
it gains access to additional schools of magic at 2nd, 10th, 14th, and 18th levels, granting the
tome eater access to base focus powers and resonant powers accordingly. The tome eater's bonded tome
serves as her implement component to cast occultist spells of all schools she knows. However, she
must split her mental focus among the schools she knows for the purpose of determining resonant
powers and using focus powers, even though she possesses only one physical item as an implement.

**Usage:** 1 time/day + 1 per 5 occultist levels beyond 1st

**Devour Books and Scrolls (Sp)**

**Fullround:** A tome eater can devour books and scrolls in order to gain various benefits
(described below). A devoured book or scroll is absorbed into the tome eater's body and completely
destroyed.

**At 12th Level:** A tome eater can devour a book or scroll as a **move action**. Additionally,
whenever a tome eater successfully uses this ability to counter a spell being cast from a scroll,
she can choose to turn the spell back on its caster (as [spell turning](ref/spell/spell-turning))
instead of devouring the scroll. She can do this whether or not she has devoured a scroll or book
yet that day.

**At 16th Level:** The tome eater can use the spell-devouring ability as an **immediate action**
without readying an action

**At 4th Level:** Once per day a tome eater can devour a spell scroll or a book to regain mental
focus, which she can divide as she likes among her schools of magic, to a maximum of the amount of
mental focus she assigned to that school at the beginning of the day. If she devours a scroll, a
tome eater regains a number of points of mental focus equal to the spell level of the highest-level
spell contained on the scroll. If she devours a nonmagical book that contains at least 100 pages of
written text and is worth at least 25 gp, a tome eater regains 1 point of mental focus. If she
devours a magical book, she regains a number of points of mental focus equal to half the caster
level of the item. If the tome eater devours a spellbook with at least 50 pages of spells of 1st
level or higher, she regains 4 points of mental focus.

**At 6th Level:** A tome eater can [ready an action](ref/rule/ready) to devour an enemy's spell when
an enemy within 30 feet attempts to cast a spell from a scroll. This ability works as the
[counterspell](ref/rule/counterspells) action as if the tome eater were using
[dispel magic](ref/spell/dispel-magic), though the tome eater doesn't need to cast a spell to
counter the enemy's spell. A tome eater can use this ability a number of times per day equal to
[one-sixth](ref/misc/fractions-and-rounding) of her occultist level.

**At 8th Level:** A tome eater can devour a book or scroll as a **standard action**. Additionally,
whenever a tome eater successfully uses this ability to counter a spell being cast from a scroll,
she can devour the enemy's scroll without spending any additional actions if she hasn't devoured a
scroll or book yet that day.

**Gained:** At 4th Level

**Provokes attack of opportunity:** Yes

**Replaces:** Shift focus, 6th-level implement, magic circles, outside contact, binding circles,
fast circles

**Special:** If a tome eater readies an action to devour a spell and the readied action never
triggers, she doesn't expend a daily use of that ability.

**Word Sense (Sp, Su)**

**Ability:** If she spends 1 round concentrating on a text within 30 feet per 100 pages of the text,
she can gain a sense of a text's contents as if she had skimmed the text.

**Gained:** At 5th Level

**Passive:** A tome eater is constantly under the effect of [read magic](ref/spell/read-magic).
Additionally, she can automatically detect the general topic of a piece of writing, and whether that
writing is a magical scroll or tome, simply by looking at it.

**Replaces:** Aura sight
