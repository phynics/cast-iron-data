+++
id = "ref/carried/core-rulebook/rules/using-skills/acquiring-skills"
kind = "rule"
title = "Acquiring Skills"
source_ids = ["core-rulebook"]
section = ["Rules", "Using Skills"]
parent = "ref/carried/core-rulebook/rules/using-skills"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Rules/Using Skills/Acquiring Skills", path = "core_rulebook/rules/using_skills.json" },
]

[fields]
kind = "none"
+++

Each level, your character gains a number of skill ranks dependent upon your class plus your
Intelligence modifier. Investing a rank in a skill represents a measure of training in that skill.
You can never have more ranks in a skill than your total number of Hit Dice. In addition, each class
has a number of favored skills, called class skills. It is easier for your character to become more
proficient in these skills, as they represent part of his professional training and constant
practice. You gain a +3 bonus on all class skills that you put ranks into. If you have more than one
class and both grant you a class skill bonus, these bonuses do not stack.

## Table: Skill Ranks {#table-skill-ranks}

::: table
caption = "Table: Skill Ranks"
head = [
  [
    { text = "Class", header = true },
    { text = "Skill Ranks per Level", header = true },
  ],
]
body = [
  [
    { text = "Barbarian" },
    { text = "4 + Int modifier" },
  ],
  [
    { text = "Bard" },
    { text = "6 + Int modifier" },
  ],
  [
    { text = "Cleric" },
    { text = "2 + Int modifier" },
  ],
  [
    { text = "Druid" },
    { text = "4 + Int modifier" },
  ],
  [
    { text = "Fighter" },
    { text = "2 + Int modifier" },
  ],
  [
    { text = "Monk" },
    { text = "4 + Int modifier" },
  ],
  [
    { text = "Paladin" },
    { text = "2 + Int modifier" },
  ],
  [
    { text = "Ranger" },
    { text = "6 + Int modifier" },
  ],
  [
    { text = "Rogue" },
    { text = "8 + Int modifier" },
  ],
  [
    { text = "Sorcerer" },
    { text = "2 + Int modifier" },
  ],
  [
    { text = "Wizard" },
    { text = "2 + Int modifier" },
  ],
]
:::

The number of skill ranks you gain when taking a level in one of the base classes is shown on Table:
Skill Ranks. Humans gain 1 additional skill rank per class level. Characters who take a level in a
favored class have the option of gaining 1 additional skill rank or an additional hit point. If you
select a level in a new class, all of its class skills are automatically added to your list of class
skills, and you gain a +3 bonus on these skills if you have ranks in them.

## Skill Checks {#skill-checks}

When your character uses a skill, he isn't guaranteed success. In order to determine success,
whenever you attempt to use a skill, you must make a skill check.

Each skill rank grants a +1 bonus on checks made using that skill. When you make a skill check, you
roll 1d20 and then add your ranks and the appropriate ability score modifier to the result of this
check. If the skill you're using is a class skill (and you have invested ranks into that skill), you
gain a +3 bonus on the check. If you are not trained in the skill (and if the skill may be used
untrained), you may still attempt the skill, but you use only the bonus (or penalty) provided by the
associated ability score modifier to modify the check. Skills can be further modified by a wide
variety of sources—by your race, by a class ability, by equipment, by spell effects or magic items,
and so on. See Table: Skill Check Bonuses for a summary of skill check bonuses.

### Table: Skill Check Bonuses {#table-skill-check-bonuses}

::: table
caption = "Table: Skill Check Bonuses"
head = [
  [
    { text = "Skill", header = true },
    { text = "Skill Check is Equal To\\*", header = true },
  ],
]
body = [
  [
    { text = "Untrained" },
    { text = "1d20 + ability modifier + racial modifier" },
  ],
  [
    { text = "Trained" },
    { text = "1d20 + skill ranks + ability modifier + racial modifier" },
  ],
  [
    { text = "Trained Class Skill" },
    { text = "1d20 + skill ranks + ability modifier + racial modifier + 3" },
  ],
]
foot = [
  [
    { text = "\\* Armor check penalty applies to all Strength- and Dexterity-based skill checks.", colspan = 2 },
  ],
]
:::

If the result of your skill check is equal to or greater than the difficulty class (or DC) of the
task you are attempting to accomplish, you succeed. If it is less than the DC, you fail. Some tasks
have varying levels of success and failure depending on how much your check is above or below the
required DC. Some skill checks are opposed by the target's skill check. When making an opposed skill
check, the attempt is successful if your check result exceeds the result of the target.

## Taking 10 and Taking 20 {#taking-10-and-taking-20}

A skill check represents an attempt to accomplish some goal, usually while under some sort of time
pressure or distraction. Sometimes, though, a character can use a skill under more favorable
conditions, increasing the odds of success.

### Taking 10 {#taking-10}

When your character is not in immediate danger or distracted, you may choose to take 10. Instead of
rolling 1d20 for the skill check, calculate your result as if you had rolled a 10. For many routine
tasks, taking 10 makes them automatically successful. Distractions or threats (such as combat) make
it impossible for a character to take 10. In most cases, taking 10 is purely a safety measure—you
know (or expect) that an average roll will succeed but fear that a poor roll might fail, so you
elect to settle for the average roll (a 10). Taking 10 is especially useful in situations where a
particularly high roll wouldn't help.

### Taking 20 {#taking-20}

When you have plenty of time, you are faced with no threats or distractions, and the skill being
attempted carries no penalties for failure, you can take 20. In other words, if you roll a d20
enough times, eventually you will get a 20. Instead of rolling 1d20 for the skill check, just
calculate your result as if you had rolled a 20.

Taking 20 means you are trying until you get it right, and it assumes that you fail many times
before succeeding. Taking 20 takes 20 times as long as making a single check would take (usually 2
minutes for a skill that takes 1 round or less to perform).

Since taking 20 assumes that your character will fail many times before succeeding, your character
would automatically incur any penalties for failure before he or she could complete the task (hence
why it is generally not allowed with skills that carry such penalties). Common “take 20” skills
include Disable Device (when used to open locks), Escape Artist, and Perception (when attempting to
find traps).

### Ability Checks and Caster Level Checks {#ability-checks-and-caster-level-checks}

The normal take 10 and take 20 rules apply for ability checks. Neither rule applies to concentration
checks or caster level checks.

## Aid Another {#aid-another}

You can help someone achieve success on a skill check by making the same kind of skill check in a
cooperative effort. If you roll a 10 or higher on your check, the character you're helping gets a +2
bonus on his or her check. (You can't take 10 on a skill check to aid another.) In many cases, a
character's help won't be beneficial, or only a limited number of characters can help at once.

In cases where the skill restricts who can achieve certain results, such as trying to open a lock
using Disable Device, you can't aid another to grant a bonus to a task that your character couldn't
achieve alone. The GM might impose further restrictions to aiding another on a case-by-case basis as
well.
