from collections import namedtuple
from enum import Enum
from itertools import zip_longest
from itertools import filterfalse

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))


def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
    inactive = []
    active = []
    
    inactive = list(filter(lambda a: a.category in (Condition.HEALTHY, Condition.DEAD), agent_listing))
    active = list(filterfalse(lambda a: a.category in (Condition.HEALTHY, Condition.DEAD), agent_listing))

    pairs = zip_longest(*(iter(active),) * 2)

    result = []

    for a1, a2 in pairs:
        result.extend(resolve_meeting(a1, a2))

    result.extend(inactive)

    return result


def resolve_meeting(a1: Agent, a2: Agent):
    if a1 is None or a2 is None:
        return [a1 or a2]

    if a1.category == Condition.CURE and a2.category != Condition.CURE:
        return [a1, improve_condition(a2)]
    if a2.category == Condition.CURE and a1.category != Condition.CURE:
        return [improve_condition(a1), a2]
    if a1.category == Condition.CURE and a2.category == Condition.CURE:
        return [a1, a2]

    return worsen_both(a1, a2)


def improve_condition(agent: Agent):
    if agent.category == Condition.DYING:
        return Agent(agent.name, Condition.SICK)
    if agent.category == Condition.SICK:
        return Agent(agent.name, Condition.HEALTHY)
    return agent


def worsen_condition(agent: Agent):
    if agent.category == Condition.SICK:
        return Agent(agent.name, Condition.DYING)
    if agent.category == Condition.DYING:
        return Agent(agent.name, Condition.DEAD)
    return agent


def worsen_both(a1: Agent, a2: Agent):
    return [worsen_condition(a1), worsen_condition(a2)]


if __name__ == '__main__':
    agents = (
        Agent("Adam", Condition.SICK),
        Agent("Cure0", Condition.CURE),
        Agent("Cure1", Condition.CURE),
        Agent("Bob", Condition.HEALTHY),
        Agent("Alice", Condition.DEAD),
        Agent("Charlie", Condition.DYING),
        Agent("Vaccine", Condition.SICK),
        Agent("Darlene", Condition.DYING),
        Agent("Emma", Condition.SICK),
        Agent("Cure2", Condition.CURE)
        )

    result = meetup(agents)

    for agent in result:
        print(agent)